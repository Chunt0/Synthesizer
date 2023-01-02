import numpy as np
from oscillator import Oscillator
osc1 = Oscillator(freq=0,amp=0,phase=0,time=1)
osc2 = Oscillator(freq=0,amp=0,phase=0,time=1)


osc1.import_wav_file("./wav/dog.wav")
osc2.import_wav_file("./wav/scream.wav")

osc1.set_wave_form(osc1.wave_form[:250000])
osc2.set_wave_form(osc2.wave_form[:250000])

arr1 = osc1.wave_form.reshape((500,500))
arr2 = osc2.wave_form.reshape((500,500))

arr = np.matmul(arr1,arr2)

osc1.set_wave_form(arr.reshape(250000,))

osc1.write_wav("./wav/dogscream.wav")