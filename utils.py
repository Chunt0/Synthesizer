import numpy as np
import scipy.io.wavfile
from oscillator import Oscillator
from dataclasses import dataclass

def ADSREnvelope(waveform: Oscillator, ADSR: list) -> None:
    """ADSR Generator
    Creates a list of coefficients that act as an ADSR envelope. This array is then multiplied by the input
    waveform."""
    #######################
    # Declare our variables
    envelope = np.array([1.0 for _ in range(waveform.num_samples)])
    
    clock = 0
    coefficient = 0

    attack_length = int(ADSR[0] * waveform.num_samples)
    decay_length = int(ADSR[1] * waveform.num_samples)
    sustain_length = int(ADSR[2] * waveform.num_samples)
    
    ###############################
    # Shape the attack coefficients
    for sample in range(clock, attack_length):
        envelope[sample] = coefficient * envelope[sample]
        coefficient += 1/attack_length
    clock += attack_length

    #############################
    # Shape the decay coefficient
    for sample in range(clock, decay_length+clock):
        if coefficient > 0:
            envelope[sample] = coefficient * envelope[sample]
            coefficient -= (1-ADSR[3])*(1/decay_length)
        else:
            coefficient = 0
            envelope[sample] =  coefficient * envelope[sample]
    clock += decay_length

    ###############################
    # Shape the sustain coefficient
    for sample in range(clock, sustain_length+clock):
        envelope[sample] = coefficient * envelope[sample]
    clock += sustain_length

    ###############################
    # Shape the release coefficient
    release_length = waveform.num_samples - clock
    for sample in range(clock, waveform.num_samples):
        if coefficient > 0:
            envelope[sample] = coefficient * envelope[sample]
            coefficient -= (ADSR[3])/release_length
        else:
            coefficient = 0
            envelope[sample] = coefficient * envelope[sample]

    ############################################
    # Multiply our amplitude by our coefficients
    waveform.set_wave_form(waveform.wave_form * envelope)

###############################################################################

def NWindowEnvelope(waveform: Oscillator, windows: list[float]) -> None:
    """
    Creates an amplitude envelope made of N-windows.
    The List, windows, is of size N and each value corresponds to an amplitude
    coefficient between 0-1.

    An nd.array will be created the same length as the waveform and the windows 
    list will be used to generate the corresponding coefficient values to be
    stored in the envelope. Each window will be of length N/num_samples.
    """
    envelope = np.array([0.0 for _ in waveform.wave_form])

    window_size = int(waveform.num_samples/len(windows))

    position = 0

    for window_number, coefficient in enumerate(windows):
        if window_number == len(windows)-1:
            for index in range(position, waveform.num_samples):
                envelope[index] = coefficient
        else:
            for index in range(position, position+window_size):
                envelope[index] = coefficient
            position += window_size

    waveform.set_wave_form(waveform.wave_form * envelope)

###############################################################################

def oscGenerator(n: int, input_params: list, function: str) -> Oscillator:
    """
    A function that has various branches to allow user to define algorithms
    and then access them to build a complex oscillator
    """
    osc_list = []
    if function == "square_wave":
        coefficient = 1
        for _ in range(n):
            osc_params = []
            osc_params.append(input_params[0]*coefficient)
            osc_params.append(input_params[1]/coefficient)
            osc_params.append(input_params[2])
            osc_params.append(input_params[3])
            osc_params.append("sine")
            osc_list.append(osc_params)
            coefficient += 2
    if function == "even":
        coefficient = 1
        osc_params = []
        osc_params.append(input_params[0]*coefficient)
        osc_params.append(input_params[1]/coefficient)
        osc_params.append(input_params[2])
        osc_params.append(input_params[3])
        osc_params.append("sine")
        osc_list.append(osc_params)
        coefficient += 1
        for _ in range(n):
            osc_params = []
            osc_params.append(input_params[0]*coefficient)
            osc_params.append(input_params[1]/coefficient)
            osc_params.append(input_params[2])
            osc_params.append(input_params[3])
            osc_params.append("sine")
            osc_list.append(osc_params)
            coefficient += 2
    if function == "phase_cycle":
        phase = 0
        for _ in range(n):
            osc_params = []
            osc_params.append(input_params[0])
            osc_params.append(input_params[1])
            osc_params.append(input_params[2]+phase)
            osc_params.append(input_params[3])
            osc_params.append(input_params[4])
            osc_list.append(osc_params)
            phase += 30

    osc = polyOsc(osc_list)

    return osc

###############################################################################

def oscAdder(osc: list[Oscillator]) -> Oscillator:
    """
    Combines oscillators into one through addition and the set_wave_form 
    Oscillator method. Done to make adding oscillators more readable for the
    user. This function is probably slower than it needs to be - likely becomes
    inefficient at scale.
    """
    carrier = osc[0]
    try:
        for signal in osc[1:]:
            carrier.set_wave_form(carrier.wave_form+signal.wave_form)
        return carrier
    except:
        return carrier

###############################################################################

def polyOsc(osc: list[list]) -> Oscillator:
    """Takes a list of Oscillator parameters and adds them together. Returns an 
    Oscillator. Similar to the oscAdder() but does so with parameters rather than
    existing Oscillatlors."""
    carrier = Oscillator(freq=osc[0][0],amp=osc[0][1],phase=osc[0][2], time=osc[0][3], wave_type=osc[0][4])
    for index in range(1,len(osc)):
        temp = Oscillator(freq=osc[index][0], amp=osc[index][1], phase=osc[index][2], time=osc[index][3], wave_type=osc[index][4])
        carrier.set_wave_form(carrier.wave_form+temp.wave_form)
    return carrier

###############################################################################

def createNWindowList(n: int=1, in_params: list=[], coefficient_func: str ="on/off") -> list:
    """
    Allows user an interface to easilly write algorithms that build NWindow
    lists and then later access them easilly. Can be expanded as new functions
    are built.
    """
    window_list = []
    if coefficient_func == "on/off":
        coefficient = 1
        for _ in range(n):
            window_list.append(coefficient)
            if coefficient == 1:
                coefficient = 0
            else:
                coefficient = 1
    if coefficient_func == "off/on":
        coefficient = 0
        for _ in range(n):
            window_list.append(coefficient)
            if coefficient == 1:
                coefficient = 0
            else:
                coefficient = 1
    if coefficient_func == "random":
        window_list = np.random.random_sample(n)
    if coefficient_func == "random10":
        window_list = np.rint(np.random.random_sample(n))
    if coefficient_func == "inverse":
        for value in in_params:
            value = 1-value
            window_list.append(value)

    return window_list

###############################################################################

def wavMul(osc1: Oscillator, osc2: Oscillator):
    osc1_waveform = osc1.wave_form
    osc2_waveform = osc2.wave_form
    for sample in range(osc1_waveform.size-1, 0, -1):
        sqrt = np.sqrt(sample)
        if sqrt % 1 == 0:
            break
    sqrt = int(sqrt)
    osc1_waveform, osc2_waveform = osc1_waveform[:sample], osc2_waveform[:sample]
    osc1_waveform = osc1_waveform.reshape((sqrt,sqrt))
    osc2_waveform = osc2_waveform.reshape((sqrt,sqrt))
    new_wave = np.matmul(osc1_waveform,osc2_waveform)
    new_wave = new_wave.reshape((sample,))
    osc1.set_wave_form(new_wave)
    
    return osc1

###############################################################################

def wavInv(osc: Oscillator):
    osc_waveform = osc.wave_form
    for sample in range(osc_waveform.size-1, 0, -1):
        sqrt = np.sqrt(sample)
        if sqrt % 1 == 0:
            break
    sqrt = int(sqrt)
    osc_waveform = osc_waveform[:sample]
    osc_waveform = osc_waveform.reshape((sqrt,sqrt))
    osc_waveform = np.linalg.inv(osc_waveform)
    osc_waveform = osc_waveform.reshape((sample,))
    osc.set_wave_form(osc_waveform)

    return osc

###############################################################################

def clipSmooth(osc: Oscillator, threshold):
    osc_waveform = osc.wave_form/np.max(osc.wave_form)
    clip = True
    while clip:
        clip = False
        for index in range(1, osc_waveform.size):
            curr = osc_waveform[index]
            prev = osc_waveform[index-1]
            diff = curr - prev
            if np.abs(diff) > threshold:
                # Is the wave trending positive or negative at this point?
                samples_to_add = int(np.abs(diff)*10)
                smoothing_vals = []
                for x in range(samples_to_add):
                    val = ((diff/samples_to_add)*x)+osc_waveform[index-1]
                    smoothing_vals.append(val)
                osc_waveform = np.concatenate([osc_waveform[:index], np.array(smoothing_vals), osc_waveform[index+1:]])
                clip = True
    osc.set_wave_form(osc_waveform)
    return osc

###############################################################################

def import_wav(path):
    osc = Oscillator(freq=0, amp=0, phase=0, time=0)
    osc.sample_rate, osc.wave_form = scipy.io.wavfile.read(path)
    osc.num_samples = osc.wave_form.size
    osc.time = osc.wave_form.size/osc.sample_rate

    return osc

###############################################################################

def isfloat(value):
    try:
        value = float(value)
        return True
    except:
        return False

@dataclass
class Notes():
    """
    Simple dataclass that contains all of the frequencies of the western 
    musical scale.
    """
    C0 = 16.35
    Cs0 = 17.32
    D0 = 18.35
    Ds0 = 19.45
    E0 = 20.6
    F0 = 21.83
    Fs0 = 23.12
    G0 = 24.5
    Gs0 = 25.96
    A0 = 27.5
    As0 = 29.14
    B0 = 30.87
    C1 = 32.7
    Cs1 = 34.65
    D1 = 36.71
    Ds1 = 38.89
    E1 = 41.2
    F1 = 43.65
    Fs1 = 46.25
    G1 = 49
    Gs1 = 51.91
    A1 = 55
    As1 = 58.27
    B1 = 61.74
    C2 = 65.41
    Cs2 = 69.3
    D2 = 73.42
    Ds2 = 77.78
    E2 = 82.41
    F2 = 87.31
    Fs2 = 92.5
    G2 = 98
    Gs2 = 103.83
    A2 = 110
    As2 = 116.54
    B2 = 123.47
    C3 = 130.81
    Cs3 = 138.59
    D3 = 146.83
    Ds3 = 155.56
    E3 = 164.81
    F3 = 174.61
    Fs3 = 185
    G3 = 196
    Gs3 = 207.65
    A3 = 220
    As3 = 233.08
    B3 = 246.94
    C4 = 261.63
    Cs4 = 277.18
    D4 = 293.66
    Ds4 = 311.13
    E4 = 329.63
    F4 = 349.23
    Fs4 = 369.99
    G4 = 392
    Gs4 = 415.3
    A4 = 440
    As4 = 466.16
    B4 = 493.88
    C5 = 523.25
    Cs5 = 554.37
    D5 = 587.33
    Ds5 = 622.25
    E5 = 659.25
    F5 = 698.46
    Fs5 = 739.99
    G5 = 783.99
    Gs5 = 830.61
    A5 = 880
    As5 = 932.33
    B5 = 987.77
    C6 = 1046.5
    Cs6 = 1108.73
    D6 = 1174.66
    Ds6 = 1244.51
    E6 = 1318.51
    F6 = 1396.91
    Fs6 = 1479.98
    G6 = 1567.98
    Gs6 = 1661.22
    A6 = 1760
    As6 = 1864.66
    B6 = 1975.53
    C7 = 2093
    Cs7 = 2217.46
    D7 = 2349.32
    Ds7 = 2489.02
    E7 = 2637.02
    F7 = 2793.83
    Fs7 = 2959.96
    G7 = 3135.96
    Gs7 = 3322.44
    A7 = 3520
    As7 = 3729.31
    B7 = 3951.07
    C8 = 4186.01
    Cs8 = 4434.92
    D8 = 4698.63
    Ds8 = 4978.03
    E8 = 5274.04
    F8 = 5587.65
    Fs8 = 5919.91
    G8 = 6271.93
    Gs8 = 6644.88
    A8 = 7040
    As8 = 7458.62
    B8 = 7902.13