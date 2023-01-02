import tkinter as tk
import utils

class NEnvGui(tk.Frame):
    """
    A tkinter frame that contains widgets to input and set parameters for an N window envelope and a button to execute it.

    Parameters
    ----------
    parent: tkinter Frame object
        The parent frame that the NEnvGui object will be contained within.

    Attributes
    ----------
    label: tkinter Label object
        A label for the NEnvGui frame.
    frame: tkinter Frame object
        A frame for the input widgets.
    label1: tkinter Label object
        A label for the N entry widget.
    entry1: tkinter Entry object
        An entry widget for the N value.
    label2: tkinter Label object
        A label for the envelope dropdown menu.
    envelope: tkinter StringVar object
        A string variable for the selected envelope type.
    entry2: tkinter OptionMenu object
        A dropdown menu for selecting the envelope type.
    label3: tkinter Label object
        A label for the wave file path entry widget.
    entry3: tkinter Entry object
        An entry widget for the wave file path.
    button: tkinter Button object
        A button to execute the N window envelope.
    """
    def __init__(self, parent):
        super().__init__(parent)

        # Create main label
        label = tk.Label(self, text="N WINDOW ENVELOPE", relief="groove", font=("helvetica", 18, "bold"))
        label.grid(row=0, column=0)

        # Create frame for input widgets
        frame = tk.Frame(self)

        # Create wav input widgets
        label1 = tk.Label(frame, text="IMPORT WAV:", font=("helvetica",12,"bold"))
        self.entry1 = tk.Entry(frame, width=10) 
        label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)

        # Create N input widgets
        label2 = tk.Label(frame, text="N:", font=("helvetica",12,"bold"))
        self.entry2 = tk.Entry(frame, width=10) 
        label2.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)

        # Create envelope input widgets
        label3 = tk.Label(frame, text="ENVELOPE:", font=("helvetica",12,"bold"))
        self.envelope = tk.StringVar(self)
        options = ["on/off", "off/on", "random"]
        entry3 = tk.OptionMenu(frame, self.envelope, *options)
        label3.grid(row=2, column=0)
        entry3.grid(row=2, column=1)

        # Create execute button
        self.execute_button = tk.Button(frame, text="EXECUTE", command=self.n_window_env)
        self.execute_button.grid(row=3, column=0)

        # Place input frame on main frame
        frame.grid(row=1, column=0)

    def n_window_env(self):
        selection = self.envelope.get()
        try:
            window_list = utils.createNWindowList(n=int(self.entry2.get()),coefficient_func=selection)
            osc = utils.import_wav(self.entry1.get())
            utils.NWindowEnvelope(osc, window_list)
            osc.write_wav(self.entry1.get())
        except:
            print("ERROR")
            return