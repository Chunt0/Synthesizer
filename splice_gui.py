import tkinter as tk
import utils
import os

class SpliceGui(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create main label
        label = tk.Label(self, text="SPLICE WAV", relief="groove", font=("helvetica", 18, "bold"))
        label.grid(row=0, column=0)

        # Create frame for input widgets
        frame = tk.Frame(self)

        # Create wav input 1 widgets
        label1 = tk.Label(frame, text="IMPORT WAV 1:", font=("helvetica",12,"bold"))
        self.entry1 = tk.Entry(frame, width=10) 
        label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)

        # Create wav input 2 widgets
        label2 = tk.Label(frame, text="IMPORT WAV 2:", font=("helvetica",12,"bold"))
        self.entry2 = tk.Entry(frame, width=10) 
        label2.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)
        
        # Create N input widgets
        label3 = tk.Label(frame, text="N:", font=("helvetica",12,"bold"))
        self.entry3 = tk.Entry(frame, width=10) 
        label3.grid(row=2, column=0)
        self.entry3.grid(row=2, column=1)

        # Create execute button
        self.execute_button = tk.Button(frame, text="EXECUTE", command=self.splice)
        self.execute_button.grid(row=3, column=0)

        # Place input frame on main frame
        frame.grid(row=1, column=0)

    def splice(self):
        try:
            osc1 = utils.import_wav(self.entry1.get())
            osc2 = utils.import_wav(self.entry2.get())
            if osc1.num_samples < osc2.num_samples:
                osc2.set_wave_form(osc2.wave_form[:osc1.num_samples])
            if osc2.num_samples < osc1.num_samples:
                osc1.set_wave_form(osc1.wave_form[:osc2.num_samples])

            window_list1 = utils.createNWindowList(n=int(self.entry3.get()),coefficient_func="on/off")
            window_list2 = utils.createNWindowList(n=int(self.entry3.get()),coefficient_func="off/on")
            utils.NWindowEnvelope(osc1, window_list1)
            utils.NWindowEnvelope(osc2, window_list2)

            # Some bug occurs when a WAV file is created in some outside program,
            # exporting then re-importing seems to fix it. Might have to do with metatags?
            # I'm sure there is a better way but I don't know what it is right now.
            temp_path = "./tmp.wav"
            osc1.write_wav(temp_path)
            osc1 = utils.import_wav(temp_path)
            osc2.write_wav(temp_path)
            osc2 = utils.import_wav(temp_path)
            os.remove(temp_path)

            osc = utils.oscAdder([osc1,osc2])
            osc.write_wav(self.entry1.get())
        
        except:
            print("ERROR")
            return