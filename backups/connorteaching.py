from oscillator import Oscillator
from utils import oscAdder, oscGenerator

TIME = 100
BEAT = 160/60


osc1 = oscGenerator(100,[BEAT/2,.8,0,TIME,"sine"],"square_wave")
osc2 = oscGenerator(100,[BEAT,.8,90,TIME,"sine"],"square_wave")
osc3 = oscGenerator(100,[BEAT/4,1,30,TIME,"sine"],"square_wave")
osc4 = oscGenerator(100,[BEAT/8,.5,0,TIME,"sine"],"square_wave")
osc = oscAdder([osc1,osc2,osc3,osc4])

carrier = Oscillator(freq=200,amp=osc.wave_form,phase=0,time=TIME)
path = "./wav/11_29_2022_2.wav"
carrier.write_wav(path)