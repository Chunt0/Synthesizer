import tkinter as tk
import utils
from oscillator import Oscillator
class OscFrame(tk.Frame):
    def __init__(self, parent, op):
        super().__init__(parent)
        value_frame = tk.Frame(self)

        # Create main label
        label = tk.Label(value_frame, text=f"OSC{op}", relief="groove", font=("helvetica", 18, "bold"))
        label.grid(row=0, column=0)

        # Create frequency input widgets
        label1 = tk.Label(value_frame, text="FREQ:", font=("helvetica", 12, "bold"))
        self.freq = tk.Entry(value_frame, width=10)
        label1.grid(row=1, column=0)
        self.freq.grid(row=1, column=1)

        # Create amplitude input widgets
        label2 = tk.Label(value_frame, text="AMP:", font=("helvetica", 12, "bold"))
        self.amp = tk.Entry(value_frame, width=10)
        label2.grid(row=2, column=0)
        self.amp.grid(row=2, column=1)

        # Create frequency deviation input widgets
        label3 = tk.Label(value_frame, text="PHASE:", font=("helvetica", 12, "bold"))
        self.phase = tk.DoubleVar(self)
        self.phase_scale = tk.Scale(value_frame, variable=self.phase, from_=0, to=360, orient="horizontal", resolution=1)
        label3.grid(row=3, column=0)
        self.phase_scale.grid(row=3, column=1)

        # Create wave type input widgets
        label4 = tk.Label(value_frame, text="WAVE:", font=("helvetica", 12, "bold"))
        wave_type_list = ["cosine", "sine", "square", "smooth square", "saw", "triangle"]
        self.wave = tk.StringVar(self)
        self.wave.set(wave_type_list[0])
        self.wave_type = tk.OptionMenu(value_frame, self.wave, *wave_type_list)
        label4.grid(row=4, column=0)
        self.wave_type.grid(row=4, column=1)

        # Create ADSR input widgets
        self.adsr_val = tk.BooleanVar(self)
        self.adsr_checkbox = tk.Checkbutton(value_frame, variable=self.adsr_val, text="ADSR:", justify="left", font=("helvetica", 12, "bold"))
        self.adsr_checkbox.grid(row=5, column=0)

        label5 = tk.Label(value_frame, text="ATTACK:", font=("helvetica", 12, "bold"))
        self.attack = tk.DoubleVar(self)
        self.attack_scale = tk.Scale(value_frame, variable=self.attack, from_=0, to=1, orient="horizontal", resolution=0.01)
        label5.grid(row=6,column=0)
        self.attack_scale.grid(row=6, column=1)

        label6 = tk.Label(value_frame, text="DECAY:", font=("helvetica", 12, "bold"))
        self.decay = tk.DoubleVar(self)
        self.decay_scale = tk.Scale(value_frame, variable=self.decay, from_=0, to=1, orient="horizontal", resolution=0.01)
        label6.grid(row=7,column=0)
        self.decay_scale.grid(row=7, column=1)

        label7 = tk.Label(value_frame, text="SUSTAIN:", font=("helvetica", 12, "bold"))
        self.sustain = tk.DoubleVar(self)
        self.sustain_scale = tk.Scale(value_frame, variable=self.sustain, from_=0, to=1, orient="horizontal", resolution=0.01)
        label7.grid(row=8,column=0)
        self.sustain_scale.grid(row=8, column=1)

        label8 = tk.Label(value_frame, text="LEVEL:", font=("helvetica", 12, "bold"))
        self.decay_level = tk.DoubleVar(self)
        self.decay_level_scale = tk.Scale(value_frame, variable=self.decay_level, from_=0, to=1, orient="horizontal", resolution=0.01)
        label8.grid(row=9, column=0)
        self.decay_level_scale.grid(row=9, column=1)

        self.entries = [self.freq, self.amp, self.phase, self.wave, [self.adsr_val, self.attack, self.decay, self.sustain, self.decay_level]]

        value_frame.grid(row=0, column=0)


class LFOGui(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create operator frame objects
        self.osc1 = OscFrame(self, 1)
        self.osc2 = OscFrame(self, 2)
        self.osc3 = OscFrame(self, 3)
        self.osc4 = OscFrame(self, 4)
        self.osc5 = OscFrame(self, 5)
        self.osc6 = OscFrame(self, 6)
        self.oscs = [self.osc1, self.osc2, self.osc3, self.osc4, self.osc5, self.osc6]
        self.osc1.grid(row=0, column=0, padx=10, pady=10)
        self.osc2.grid(row=0, column=1, padx=10, pady=10)
        self.osc3.grid(row=0, column=2, padx=10, pady=10)
        self.osc4.grid(row=1, column=0, padx=10, pady=10)
        self.osc5.grid(row=1, column=1, padx=10, pady=10)
        self.osc6.grid(row=1, column=2, padx=10, pady=10)

        # Create time input frame and widgets
        self.time_frame = tk.Frame(self)
        self.time = tk.Label(self.time_frame, text="TIME:", font=("helvetica", 12, "bold"))
        self.time_entry = tk.Entry(self.time_frame, width=5)
        self.time.grid(row=2,column=0, pady=5)
        self.time_entry.grid(row=2, column=1)
        self.time_frame.grid(row=2, column=0, pady=15)

        # Create export path frame and widgets
        self.export_path_frame = tk.Frame(self)
        self.export_path = tk.Label(self.export_path_frame, text="EXPORT PATH:", font=("helvetica", 12, "bold"))
        self.export_path_entry = tk.Entry(self.export_path_frame)
        self.export_path.grid(row=0, column=0)
        self.export_path_entry.grid(row=0, column=1)
        self.export_path_frame.grid(row=2, column=1, pady=15)

        # Create export button
        self.export_button = tk.Button(self, text="EXPORT SAMPLE", command=self.export_sample)
        self.export_button.grid(row=2, column=2)
    
    def export_sample(self):
        path = self.export_path_entry.get()
        t = int(self.time_entry.get())
        osc_list = []
        for osc_vals in self.oscs:
            if len(osc_vals.entries[0].get()) == 0:
                pass
            else:
                f = float(osc_vals.entries[0].get())
                a = float(osc_vals.entries[1].get())
                p = float(osc_vals.entries[2].get())
                wave = str(osc_vals.entries[3].get())
                osc = Oscillator(freq=f, amp=a, phase=p, time=t, wave_type=wave)
                if osc_vals.entries[4][0].get():
                    ADSR_list = []
                    for val in osc_vals.entries[4][1:]:
                        ADSR_list.append(float(val.get()))
                    utils.ADSREnvelope(osc,ADSR_list)
                osc_list.append(osc)
        osc = utils.oscAdder(osc_list)
        osc.write_wav(path)
