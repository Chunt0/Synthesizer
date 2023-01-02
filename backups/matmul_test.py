import numpy as np
from oscillator import Oscillator
import utils as u
import dx7_algo as FM

TIME = 100

clapping = u.import_wav("./wav/clap.wav")

clapping.trim(0,TIME)

osc1 = Oscillator(freq=440, amp = clapping.wave_form, phase=0, time=TIME)

clapping.write_wav("./wav/inv_clap.wav")
