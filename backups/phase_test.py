import numpy as np
from oscillator import Oscillator
from utils import \
    polyOsc, \
    oscAdder, \
    oscGenerator, \
    createNWindowList, \
    ADSREnvelope, \
    wavMul, \
    wavInv 

TIME = 100
SWEEP1 = [.5,.5,0,0]
SWEEP2 = [.2,.8,0,0]

baseband1 = Oscillator(freq=2,amp=1,phase=90,time=TIME)
ADSREnvelope(baseband1,SWEEP1)
baseband2 = Oscillator(freq=800,amp=1, phase=90*baseband1.wave_form,time=TIME)
ADSREnvelope(baseband2,SWEEP2)
baseband2 = wavMul(baseband1,baseband2)


baseband2.write_wav("./wav/inv_test_2.wav")