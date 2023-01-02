import tkinter as tk
import dx7_algo as FM
import utils

class OPFrame(tk.Frame):
    """
    A tkinter frame that contains widgets to input and set parameters for a single operator in a DX7 synthesizer.

    Parameters
    ----------
    parent: tkinter Frame object
        The parent frame that the OPFrame object will be contained within.
    op: int
        The operator number, used to label the OPFrame object.

    Attributes
    ----------
    entries: list
        A list of tkinter Entry objects and lists of tkinter Scale objects for each operator parameter.
    freq: tkinter Entry object
        An entry widget for the operator frequency.
    amp: tkinter Entry object
        An entry widget for the operator amplitude.
    fdev: tkinter Entry object
        An entry widget for the operator frequency deviation.
    wave: tkinter StringVar object
        A string variable for the operator waveform type.
    wavetype: tkinter OptionMenu object
        A dropdown menu for selecting the operator waveform type.
    adsr_val: tkinter BooleanVar object
        A boolean variable for the operator ADSR usage.
    adsr_checkbox: tkinter Checkbutton object
        A checkbox for enabling or disabling the operator ADSR.
    attack: tkinter DoubleVar object
        A double variable for the operator ADSR attack time.
    attack_scale: tkinter Scale object
        A scale widget for adjusting the operator ADSR attack time.
    decay: tkinter DoubleVar object
        A double variable for the operator ADSR decay time.
    decay_scale: tkinter Scale object
        A scale widget for adjusting the operator ADSR decay time.
    sustain: tkinter DoubleVar object
        A double variable for the operator ADSR sustain level.
    sustain_scale: tkinter Scale object
        A scale widget for adjusting the operator ADSR sustain level.
    decay_level: tkinter DoubleVar object
    decay_level: tkinter DoubleVar object
        A double variable for the operator ADSR decay level.
    decay_level_scale: tkinter Scale object
        A scale widget for adjusting the operator ADSR decay level.
    """
    def __init__(self, parent, op):
        super().__init__(parent)

        # Create main label
        label = tk.Label(self, text=f"OP{op}", relief="groove", font=("helvetica", 18, "bold"))
        label.grid(row=0, column=0)

        # Create frequency input widgets
        label1 = tk.Label(self, text="FREQ:", font=("helvetica", 12, "bold"))
        self.freq = tk.Entry(self, width=10)
        label1.grid(row=1, column=0)
        self.freq.grid(row=1, column=1)

        # Create amplitude input widgets
        label2 = tk.Label(self, text="AMP:", font=("helvetica", 12, "bold"))
        self.amp = tk.Entry(self, width=10)
        label2.grid(row=2, column=0)
        self.amp.grid(row=2, column=1)

        # Create frequency deviation input widgets
        label3 = tk.Label(self, text="FDEV:", font=("helvetica", 12, "bold"))
        self.fdev = tk.Entry(self, width=10)
        label3.grid(row=3, column=0)
        self.fdev.grid(row=3, column=1)

        # Create wave type input widgets
        label4 = tk.Label(self, text="WAVE:", font=("helvetica", 12, "bold"))
        wavetype_list = ["cosine","sine","square","smooth square","saw","triangle"]
        self.wave = tk.StringVar(self)
        self.wave.set(wavetype_list[0])
        self.wavetype = tk.OptionMenu(self, self.wave, *wavetype_list)
        label4.grid(row=4, column=0)
        self.wavetype.grid(row=4, column=1)

        # Create ADSR input widgets
        self.adsr_val = tk.BooleanVar(self)
        self.adsr_checkbox = tk.Checkbutton(self, variable=self.adsr_val, text="ADSR:", justify="left", font=("helvetica", 12, "bold"))
        self.adsr_checkbox.grid(row=5,column=0)

        label5 = tk.Label(self, text="ATTACK:", font=("helvetica", 12, "bold"))
        self.attack = tk.DoubleVar(self)
        self.attack_scale = tk.Scale(self, variable=self.attack, from_=0, to=1, orient="horizontal", resolution=0.01)
        label5.grid(row=6,column=0)
        self.attack_scale.grid(row=6,column=1)

        label6 = tk.Label(self, text="DECAY:", font=("helvetica", 12, "bold"))
        self.decay = tk.DoubleVar(self)
        self.decay_scale = tk.Scale(self, variable=self.decay, from_=0, to=1, orient="horizontal", resolution=0.01)
        label6.grid(row=7,column=0)
        self.decay_scale.grid(row=7,column=1)

        label7 = tk.Label(self, text="SUSTAIN:", font=("helvetica", 12, "bold"))
        self.sustain = tk.DoubleVar(self)
        self.sustain_scale = tk.Scale(self, variable=self.sustain, from_=0, to=1, orient="horizontal", resolution=0.01)
        label7.grid(row=8,column=0)
        self.sustain_scale.grid(row=8,column=1)

        label8 = tk.Label(self, text="LEVEL:", font=("helvetica", 12, "bold"))
        self.decay_level = tk.DoubleVar(self)
        self.decay_level_scale = tk.Scale(self, variable=self.decay_level, from_=0, to=1, orient="horizontal", resolution=0.01)
        label8.grid(row=9,column=0)
        self.decay_level_scale.grid(row=9,column=1)

        self.entries = [self.freq, self.amp, self.fdev, self.wave, [self.adsr_val, self.attack, self.decay, self.sustain, self.decay_level]]

class DX7Gui(tk.Frame):
    """
    A tkinter frame that contains widgets to input and set parameters for a DX7 synthesizer, as well as a button to export the resulting sample.

    Parameters
    ----------
    parent: tkinter Frame object
        The parent frame that the DX7Gui object will be contained within.

    Attributes
    ----------
    OP1-OP6: tkinter OPFrame object
        Instances of the OPFrame class for each operator in the DX7 synthesizer.
    operators: list
        A list of the OPFrame instances.
    time_frame: tkinter Frame object
        A frame for widgets related to the duration of the sample.
    time: tkinter Label object
        A label for the duration entry widget.
    time_entry: tkinter Entry object
        An entry widget for the duration of the sample.
    feedback_val: tkinter BooleanVar object
        A boolean variable for the feedback usage in the sample.
    feedback_checkbox: tkinter Checkbutton object
        A checkbox for enabling or disabling feedback in the sample.
    algo_label: tkinter Label object
        A label for the algorithm dropdown menu.
    algo_val: tkinter IntVar object
        An integer variable for the selected algorithm number.
    dropdown: tkinter OptionMenu object
        A dropdown menu for selecting the algorithm number.
    export_path_frame: tkinter Frame object
        A frame for widgets related to the export path for the sample.
    export_path: tkinter Label object
        A label for the export path entry widget.
    export_path_entry: tkinter Entry object
        An entry widget for the export path of the sample.
    export_button: tkinter Button object
        A button to trigger the sample export.
    """

    def __init__(self, parent):
        super().__init__(parent)

        # Create operator frame objects
        self.OP1 = OPFrame(self,1)
        self.OP2 = OPFrame(self,2)
        self.OP3 = OPFrame(self,3)
        self.OP4 = OPFrame(self,4)
        self.OP5 = OPFrame(self,5)
        self.OP6 = OPFrame(self,6)
        self.operators = [self.OP1, self.OP2, self.OP3, self.OP4, self.OP5, self.OP6]
        self.OP1.grid(row=0,column=0, padx=10, pady=10)
        self.OP2.grid(row=0,column=1, padx=10, pady=10)
        self.OP3.grid(row=0,column=2, padx=10, pady=10)
        self.OP4.grid(row=1,column=0, padx=10, pady=10)
        self.OP5.grid(row=1,column=1, padx=10, pady=10)
        self.OP6.grid(row=1,column=2, padx=10, pady=10)

        # Create time input frame and widgets
        self.time_frame = tk.Frame(self)
        self.time = tk.Label(self.time_frame, text="TIME:", font=("helvetica", 12, "bold"))
        self.time_entry = tk.Entry(self.time_frame, width=5)
        self.time.grid(row=2,column=0, pady=5)
        self.time_entry.grid(row=2,column=1) 
        
        self.feedback_val = tk.BooleanVar()
        self.feedback_checkbox = tk.Checkbutton(self.time_frame, text="FEEDBACK", justify="left", font=("helvetica", 12, "bold") ,variable=self.feedback_val)
        self.feedback_checkbox.grid(row=0,column=1, pady=5)
        
        self.algo_label = tk.Label(self.time_frame, text="ALGORITHM", font=("helvetica", 12, "bold"))
        self.algo_label.grid(row=1,column=0)
        self.algo_val = tk.IntVar(self.time_frame)
        self.algo_val.set("1")
        
        self.dropdown = tk.OptionMenu(self.time_frame, self.algo_val, *range(1, 33))
        self.dropdown.grid(row=1,column=1)
        self.time_frame.grid(row=2,column=0,pady=15)

        # Create export path frame and widgets
        self.export_path_frame = tk.Frame(self)
        self.export_path = tk.Label(self.export_path_frame, text="EXPORT PATH:", font=("helvetica", 12, "bold"))
        self.export_path_entry = tk.Entry(self.export_path_frame)
        self.export_path.grid(row=0,column=0)
        self.export_path_entry.grid(row=0,column=1) 
        self.export_path_frame.grid(row=2,column=1,pady=15)

        # Create export button
        self.export_button = tk.Button(self, text="EXPORT SAMPLE", command=self.export_sample)
        self.export_button.grid(row=2, column=2)
    
    def export_sample(self):
        # Initialize input_params list with time value
        try:
            if len(self.time_entry.get()) == 0:
                input_params = [0]
            else:
                input_params = [float(self.time_entry.get())]
        except:
            print("Time must be a number.")
            return

        # Iterate through operator frames and extract values
        for op in self.operators:
            op_list = []
            ADSR_list = []
            for index, entry in enumerate(op.entries):
                if index < 3:
                    try:
                        val = entry.get()
                        if len(val) == 0:
                            op_list.append(0)
                        elif utils.isfloat(val):
                            op_list.append(float(val))
                        else:
                            trim = int(input_params[0]*44100)
                            osc = utils.import_wav(val)
                            osc.set_wave_form(osc.wave_form[:trim])
                            op_list.append(osc.wave_form)
                    except:
                        print(f"FREQ, AMP, and FDEV must be numbers.\n{entry.get()}")
                        return
                if index == 3:
                    try:
                        op_list.append(entry.get())
                    except:
                        print("Some error occured with the wavetype menu.")
                        return
                if index == 4:
                    if entry[0].get():
                        try:
                            for scale in entry[1:]:
                                ADSR_list.append(float(scale.get()))
                        except:
                            print("ADSR values must be between 0 - 1")
                            return
                    else:
                        ADSR_list = None
            op_list.append(ADSR_list)
            input_params.append(op_list)
        input_params.append(self.feedback_val.get())

        # Print input_params for debugging purposes
        print(input_params)

        # Retrieve chosen algorithm from FM.algos()
        algorithm = FM.algos()
        algorithm = algorithm.algos[self.algo_val.get()-1]

        # Create oscillator object with input_params
        osc = algorithm(input_params)

        # Write wav file to specified path
        osc.write_wav(self.export_path_entry.get())