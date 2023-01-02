from oscillator import Oscillator
import dx7_algo as FM
from utils import oscGenerator, oscAdder

def fileParse(input_file):

    output_list = []
    with open(input_file) as file:
        for index,line in enumerate(file):
            line = line.replace("\n","")
            if index == 0:
                line = float(line)
            elif index > 0 and index < 7:
                if line != "none":
                    line = line.split(' ')
                    for index1, val in enumerate(line):
                        if index1 < 3:
                            line[index1] = float(val)
                        if index1 == 4 and val == "none":
                            line[index1] = None
                        elif index1 > 3 and line[index1]:
                            line[index1] = line[index1].split(",")
                            for index2, num in enumerate(line[index1]):
                                line[index1][index2] = float(num)
                else:
                    line = [0,0,0,"cosine",None]
            elif index == 7:
                if line == "true":
                    line = True
                else:
                    line = False
            output_list.append(line)
    return output_list

path = "./dx7_input.txt"

out_list = fileParse(path)

print(out_list)

"""
TIME = 2
FREQ = 200

lfo = Oscillator(freq=1, amp=1, phase=0, time=TIME)
lfo1 = Oscillator(freq=1, amp=lfo.wave_form, phase=90, time=TIME)

input_params = [TIME,\
    [FREQ,1,50,"cosine",[.01,.3,.4,.4]],\
    [FREQ/2,lfo.wave_form,25,"sine",[.65,.2,.15,.3]],\
    [76,lfo1.wave_form,35,"sine",None],\
    [FREQ*5,.5,50,"sine",[.8,.2,0,0]],\
    [FREQ*3,.3,50,"sine",None],\
    [FREQ*1,lfo.wave_form,15,"sine",None],\
    True
    ]



osc1 = FM.dx7_1(input_params)
osc1.write_wav("./wav/dx_7_test1.wav")

osc1 = FM.dx7_2(input_params)
osc1.write_wav("./wav/dx_7_test2.wav")


osc1 = FM.dx7_3(input_params)
osc1.write_wav("./wav/dx_7_test3.wav")


osc1 = FM.dx7_4(input_params)
osc1.write_wav("./wav/dx_7_test4.wav")


osc1 = FM.dx7_5(input_params)
osc1.write_wav("./wav/dx_7_test5.wav")


osc1 = FM.dx7_6(input_params)
osc1.write_wav("./wav/dx_7_test6.wav")


osc1 = FM.dx7_7(input_params)
osc1.write_wav("./wav/dx_7_test7.wav")


osc1 = FM.dx7_8(input_params)
osc1.write_wav("./wav/dx_7_test8.wav")


osc1 = FM.dx7_9(input_params)
osc1.write_wav("./wav/dx_7_test9.wav")


osc1 = FM.dx7_10(input_params)
osc1.write_wav("./wav/dx_7_test10.wav")


osc1 = FM.dx7_11(input_params)
osc1.write_wav("./wav/dx_7_test11.wav")


osc1 = FM.dx7_12(input_params)
osc1.write_wav("./wav/dx_7_test12.wav")


osc1 = FM.dx7_13(input_params)
osc1.write_wav("./wav/dx_7_test13.wav")


osc1 = FM.dx7_14(input_params)
osc1.write_wav("./wav/dx_7_test14.wav")


osc1 = FM.dx7_15(input_params)
osc1.write_wav("./wav/dx_7_test15.wav")


osc1 = FM.dx7_16(input_params)
osc1.write_wav("./wav/dx_7_test16.wav")


osc1 = FM.dx7_17(input_params)
osc1.write_wav("./wav/dx_7_test17.wav")


osc1 = FM.dx7_18(input_params)
osc1.write_wav("./wav/dx_7_test18.wav")


osc1 = FM.dx7_19(input_params)
osc1.write_wav("./wav/dx_7_test19.wav")


osc1 = FM.dx7_20(input_params)
osc1.write_wav("./wav/dx_7_test20.wav")


osc1 = FM.dx7_21(input_params)
osc1.write_wav("./wav/dx_7_test21.wav")


osc1 = FM.dx7_22(input_params)
osc1.write_wav("./wav/dx_7_test22.wav")


osc1 = FM.dx7_23(input_params)
osc1.write_wav("./wav/dx_7_test23.wav")


osc1 = FM.dx7_24(input_params)
osc1.write_wav("./wav/dx_7_test24.wav")


osc1 = FM.dx7_25(input_params)
osc1.write_wav("./wav/dx_7_test25.wav")


osc1 = FM.dx7_26(input_params)
osc1.write_wav("./wav/dx_7_test26.wav")


osc1 = FM.dx7_27(input_params)
osc1.write_wav("./wav/dx_7_test27.wav")


osc1 = FM.dx7_28(input_params)
osc1.write_wav("./wav/dx_7_test28.wav")


osc1 = FM.dx7_29(input_params)
osc1.write_wav("./wav/dx_7_test29.wav")


osc1 = FM.dx7_30(input_params)
osc1.write_wav("./wav/dx_7_test30.wav")


osc1 = FM.dx7_31(input_params)
osc1.write_wav("./wav/dx_7_test31.wav")


osc1 = FM.dx7_32(input_params)
osc1.write_wav("./wav/dx_7_test32.wav")
"""