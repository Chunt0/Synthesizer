from oscillator import Oscillator
from utils import NWindowEnvelope
from PIL import Image

path = "./art.jpg"
image = Image.open(path, 'r')

image_data = list(image.getdata())

image_R = []
image_G = []
image_B = []

for value in image_data:
    image_R.append(value[0]/255)
    image_G.append(value[1]/255)
    image_B.append(value[2]/255)


TIME = 100
lfo1 = Oscillator(freq=180/60, amp=.8, phase=90, time=TIME, wave_type="square")
lfo2 = Oscillator(freq=1/3*lfo1.wave_form, amp=lfo1.wave_form, phase=45, time=TIME, wave_type="sine")
lfo3 = Oscillator(freq=1/2*lfo2.wave_form, amp=lfo1.wave_form, phase=30, time=TIME)
osc1 = Oscillator(freq=40, amp=lfo3.wave_form, phase=0, time=TIME)
osc2 = Oscillator(freq=409, amp=lfo3.wave_form, phase=0, time=TIME)
osc3 = Oscillator(freq=209, amp=1, phase=0, time=TIME)

window1 = [.05,.45,.68,.30,.92,.12,.5,.05,.45,.68,.30,.92,.12,.5,.05,.45,.68,.30,.92,.12,.5,.05,.45,.68,.30,.92,.12,.5,.05,.45,.68,.30,.92,.12,.5,.05,.45,.68,.30,.92,.12,.5,.05,.45,.68,.30,.92,.12,.5,.05,.45,.68,.30,.92,.12,.5]
window2 = [.23,.87,.45,.87,.5,.23,.87,.45,.87,.5,.23,.87,.45,.87,.5,.23,.87,.45,.87,.5,.23,.87,.45,.87,.5]
window3 = [.23,.87,.45,.87,.5,.23,.87,.45,.87,.5,.23,.87,.45,.68,.30,.92]


NWindowEnvelope(osc1, image_R[100:125])
NWindowEnvelope(osc1, window1)
NWindowEnvelope(osc2, image_G[100:200])
NWindowEnvelope(osc2, window2)
NWindowEnvelope(osc3, image_B[100:150])
NWindowEnvelope(osc3, window3)

osc1.set_wave_form(osc1.wave_form+osc2.wave_form+osc3.wave_form)

osc1.write_wav("./wav/11_17_2022.wav")
osc1.plot_signal()
