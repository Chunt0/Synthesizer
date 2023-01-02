"""
YAMAHA DX7 Algorithms
"""
from oscillator import Oscillator
from utils import ADSREnvelope, oscAdder

"""

Input Params:

Time - int

Operator Params:
    - Freq, Amp, FM coefficient, wave_type, envelope

feedback - bool

Output:

Oscillator object
"""
def dx7_1(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op5_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc])
    return output

###############################################################################

def dx7_2(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op5_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
        feedback_osc = feedback_osc.wave_form
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*feedback_osc,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc])
    return output

###############################################################################

def dx7_3(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])

    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op5_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*op3_osc.wave_form,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op4_osc])
    return output

###############################################################################

def dx7_4(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        if op6[4]:
            ADSREnvelope(op6_osc, op6[4])
    
        op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
        if op5[4]:
            ADSREnvelope(op5_osc, op5[4])
    
        op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op5_osc.wave_form,time=TIME,wave_type=op4[3])
        if op4[4]:
            ADSREnvelope(op4_osc, op4[4])

        feedback_osc = op4_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op5_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*op3_osc.wave_form,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op4_osc])
    return output

###############################################################################

def dx7_5(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc,op5_osc])
    return output

###############################################################################

def dx7_6(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        if op6[4]:
            ADSREnvelope(op6_osc, op6[4])
    
        op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
        if op5[4]:
            ADSREnvelope(op5_osc, op5[4])
        feedback_osc = op5_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc,op5_osc])
    return output

###############################################################################

def dx7_7(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form
    
    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*(op4_osc.wave_form+op5_osc.wave_form),time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc])
    return output

###############################################################################

def dx7_8(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
        feedback_osc = feedback_osc.wave_form

    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*(op5_osc.wave_form+feedback_osc),time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc])
    return output

###############################################################################

def dx7_9(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*(op4_osc.wave_form+op5_osc.wave_form),time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
        feedback_osc= feedback_osc.wave_form

    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*feedback_osc,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc])
    return output

###############################################################################

def dx7_10(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*(op6_osc.wave_form+op5_osc.wave_form),time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
        feedback_osc = feedback_osc.wave_form

    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*feedback_osc,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*op3_osc.wave_form,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op4_osc])
    return output

###############################################################################

def dx7_11(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0 
    if feedback:
        feedback_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*(op6_osc.wave_form+op5_osc.wave_form),time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*op3_osc.wave_form,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op4_osc])
    return output

###############################################################################

def dx7_12(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*(op6_osc.wave_form+op5_osc.wave_form+op4_osc.wave_form),time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
        feedback_osc = feedback_osc.wave_form

    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*feedback_osc,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc])
    return output

###############################################################################

def dx7_13(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*(op6_osc.wave_form+op5_osc.wave_form+op4_osc.wave_form),time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc])
    return output

###############################################################################

def dx7_14(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*(op6_osc.wave_form+op5_osc.wave_form),time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc])
    return output

###############################################################################

def dx7_15(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*(op6_osc.wave_form+op5_osc.wave_form),time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
        feedback_osc = feedback_osc.wave_form
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*feedback_osc,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc])
    return output

###############################################################################

def dx7_16(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*(op2_osc.wave_form+op3_osc.wave_form+op4_osc.wave_form),time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = op1_osc
    return output

###############################################################################

def dx7_17(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
        feedback_osc = feedback_osc.wave_form

    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*feedback_osc,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*(op2_osc.wave_form+op3_osc.wave_form+op5_osc.wave_form),time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = op1_osc
    return output

###############################################################################

def dx7_18(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op5_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
        feedback_osc = feedback_osc.wave_form

    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*feedback_osc,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*(op2_osc.wave_form+op3_osc.wave_form+op4_osc.wave_form),time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = op1_osc
    return output

###############################################################################

def dx7_19(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op6_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*op3_osc.wave_form,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op4_osc, op5_osc])
    return output

###############################################################################

def dx7_20(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*(op6_osc.wave_form+op5_osc.wave_form),time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
        feedback_osc = feedback_osc.wave_form

    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*feedback_osc,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*op3_osc.wave_form,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op3_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op2_osc,op4_osc])
    return output

###############################################################################

def dx7_21(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op6_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
        feedback_osc = feedback_osc.wave_form

    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*feedback_osc,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*op3_osc.wave_form,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op3_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op2_osc,op4_osc,op5_osc])
    return output

###############################################################################

def dx7_22(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op6_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op6_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc,op4_osc,op5_osc])
    return output

###############################################################################

def dx7_23(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op6_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*op3_osc.wave_form,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*0,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op2_osc,op4_osc,op5_osc])
    return output

###############################################################################

def dx7_24(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op6_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op6_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*0,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op2_osc,op3_osc,op4_osc,op5_osc])
    return output

###############################################################################

def dx7_25(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op6_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op2_osc,op3_osc,op4_osc,op5_osc])
    return output

###############################################################################

def dx7_26(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*(op6_osc.wave_form+op5_osc.wave_form),time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op2_osc,op4_osc])
    return output

###############################################################################

def dx7_27(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*(op6_osc.wave_form+op5_osc.wave_form),time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
        feedback_osc = feedback_osc.wave_form
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*feedback_osc,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*op3_osc.wave_form,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*0,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op2_osc,op4_osc])
    return output

###############################################################################

def dx7_28(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
        feedback_osc = feedback_osc.wave_form

    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*feedback_osc,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op5_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*op2_osc.wave_form,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op3_osc,op6_osc])
    return output

###############################################################################

def dx7_29(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*0,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op2_osc,op3_osc,op5_osc])
    return output

###############################################################################

def dx7_30(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
        feedback_osc = feedback_osc.wave_form
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*feedback_osc,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*op5_osc.wave_form,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*op4_osc.wave_form,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*0,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op2_osc,op3_osc,op6_osc])
    return output

###############################################################################

def dx7_31(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]
    
    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form

    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*op6_osc.wave_form,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*0,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op2_osc,op3_osc,op4_osc,op5_osc])
    return output

###############################################################################

def dx7_32(input_params):
    TIME = input_params[0]
    op1 = input_params[1]
    op2 = input_params[2]
    op3 = input_params[3]
    op4 = input_params[4]
    op5 = input_params[5]
    op6 = input_params[6]
    feedback = input_params[7]

    feedback_osc = 0
    if feedback:
        feedback_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*0,time=TIME,wave_type=op6[3])
        feedback_osc = feedback_osc.wave_form


    op6_osc = Oscillator(freq=op6[0],amp=op6[1],phase=op6[2]*feedback_osc,time=TIME,wave_type=op6[3])
    if op6[4]:
        ADSREnvelope(op6_osc, op6[4])
    
    op5_osc = Oscillator(freq=op5[0],amp=op5[1],phase=op5[2]*0,time=TIME,wave_type=op5[3])
    if op5[4]:
        ADSREnvelope(op5_osc, op5[4])
    
    op4_osc = Oscillator(freq=op4[0],amp=op4[1],phase=op4[2]*0,time=TIME,wave_type=op4[3])
    if op4[4]:
        ADSREnvelope(op4_osc, op4[4])
    
    op3_osc = Oscillator(freq=op3[0],amp=op3[1],phase=op3[2]*0,time=TIME,wave_type=op3[3])
    if op3[4]:
        ADSREnvelope(op3_osc, op3[4])
    
    op2_osc = Oscillator(freq=op2[0],amp=op2[1],phase=op2[2]*0,time=TIME,wave_type=op2[3])
    if op2[4]:
        ADSREnvelope(op2_osc, op2[4])
    
    op1_osc = Oscillator(freq=op1[0],amp=op1[1],phase=op1[2]*0,time=TIME,wave_type=op1[3])
    if op1[4]:
        ADSREnvelope(op1_osc, op1[4])
    
    output = oscAdder([op1_osc,op2_osc,op3_osc,op4_osc,op5_osc,op6_osc])
    return output

###############################################################################

class algos():
    def __init__(self) -> None:
        self.algos = [dx7_1,\
            dx7_2,\
            dx7_3,\
            dx7_4,\
            dx7_5,\
            dx7_6,\
            dx7_7,\
            dx7_8,\
            dx7_9,\
            dx7_10,\
            dx7_11,\
            dx7_12,\
            dx7_13,\
            dx7_14,\
            dx7_15,\
            dx7_16,\
            dx7_17,\
            dx7_18,\
            dx7_19,\
            dx7_20,\
            dx7_21,\
            dx7_22,\
            dx7_23,\
            dx7_24,\
            dx7_25,\
            dx7_26,\
            dx7_27,\
            dx7_28,\
            dx7_29,\
            dx7_30,\
            dx7_31,\
            dx7_32,\
                ]