import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
import scipy.io.wavfile
from scipy.signal import sawtooth, square


class Oscillator():
    """
    Oscillator Class:
    This can be used to generate a specific waveform or be used
    in modulation functions as a control variable
    """

    def __init__(self, freq, amp, phase, time, sample_rate: int = 44100, wave_type: str = "sine"):
        """Initializes values"""
        self.freq = freq
        self.amp = amp
        self.phase = phase*(np.pi/180) # Degree to Radians
        self.sample_rate= sample_rate
        self.time = time
        self.num_samples = int(self.sample_rate * self.time)
        self.dur = np.linspace(0,self.time, self.num_samples) 
        self.wave_form = self.generate_wave_form(wave_type)

    def generate_wave_form(self, wave_type):
        """
        Generates an np.array that contains the waveform, each index relates
        to the corresponding sample in time and the value is the amplitude at that
        point.
        """
        if wave_type ==  "sine":
            wave = np.array(self.amp * np.sin(2* np.pi * self.freq * self.dur + self.phase))
            return wave
        if wave_type ==  "cosine":
            wave = np.array(self.amp * np.cos(2* np.pi * self.freq * self.dur + self.phase))
            return wave
        if wave_type == "square":
            wave = np.array(self.amp * square(2 * np.pi * self.freq * self.dur + self.phase))
            return wave
        if wave_type == "saw":
            wave = np.array(self.amp * sawtooth(2 * np.pi * self.freq * self.dur + self.phase))
            return wave
        if wave_type == "triangle":
            wave = np.array(self.amp * sawtooth(2 * np.pi * self.freq * self.dur + self.phase, 0.5))
            return wave
        if wave_type == "smooth square":
            wave = np.array([np.float64(0) for _ in range(self.num_samples)])
            coefficient = 1
            for _ in range(100):
                wave += np.array((self.amp/coefficient) * np.sin(2* np.pi * (self.freq*coefficient) * self.dur + self.phase))
                coefficient += 2
            return wave


    def set_wave_form(self, wave):
        self.wave_form = wave
        self.num_samples = self.wave_form.size
        self.time = self.num_samples/self.sample_rate

    def plot_signal(self):
        """Plots oscillator object."""
        plt.plot(self.dur, self.wave_form)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.xlim(0, self.time)
        plt.show()

    def write_wav(self, path):
        """Writes the wave form to a wav file."""
        self.wave_form = (3/4)*(self.wave_form/np.max(self.wave_form))
        scipy.io.wavfile.write(path, self.sample_rate, self.wave_form)

    def trim(self, start, end):
        self.time = (end-start)
        self.num_samples = (self.time * self.sample_rate)
        start = start * self.sample_rate
        end = end * self.sample_rate
        self.wave_form = self.wave_form[start:end]
