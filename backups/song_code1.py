import numpy as np
from oscillator import Oscillator
from utils import ADSREnvelope

TIME = 100

def main():
    
    osc = Oscillator(freq=3, amp=1, phase=0, time=TIME, wave_type="square")
    lfo = Oscillator(freq=1/4*osc.wave_form, amp=1, phase=np.pi/6, time=TIME)
    carrier = Oscillator(freq=239, amp=lfo.wave_form, phase=0, time=TIME)
    
    osc1 = Oscillator(freq=3, amp=1, phase=0, time=TIME, wave_type="square")
    lfo1 = Oscillator(freq=1/4*osc1.wave_form, amp=1, phase=np.pi/6, time=TIME)
    add1 = Oscillator(freq=230, amp=lfo1.wave_form**22, phase=0, time=TIME)
    
    osc2 = Oscillator(freq=1/3, amp=1, phase=0, time=TIME, wave_type="square")
    lfo2 = Oscillator(freq=osc2.wave_form, amp=1, phase=np.pi/6, time=TIME)
    add2 = Oscillator(freq=564, amp=lfo2.wave_form**5, phase=np.pi*add1.wave_form, time=TIME)
    ADSREnvelope(add2, [.5,.5,0,0])
    
    osc2_1 = Oscillator(freq=1/3, amp=1, phase=0, time=TIME, wave_type="square")
    lfo2_1 = Oscillator(freq=osc2_1.wave_form, amp=1, phase=np.pi/6, time=TIME)
    add2_1 = Oscillator(freq=164, amp=lfo2_1.wave_form, phase=np.pi, time=TIME)
    ADSREnvelope(add2_1, [.8,.2,0,0])
    add2.set_wave_form(add2.wave_form+add2_1.wave_form)
    
    osc3 = Oscillator(freq=3, amp=1, phase=0, time=TIME, wave_type="square")
    lfo3 = Oscillator(freq=1/4*osc3.wave_form, amp=1, phase=np.pi/6, time=TIME)
    add3 = Oscillator(freq=340, amp=lfo3.wave_form, phase=np.pi/4, time=TIME)
    
    carrier.set_wave_form((carrier.wave_form + add1.wave_form + add2.wave_form + add3.wave_form)/10)
    carrier.write_wav("./wav/crazy_wave.wav")



if __name__ == "__main__":
    main()
