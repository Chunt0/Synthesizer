import tkinter as tk
import dx7_gui as DX
import nenvelope_gui as NEnv
import splice_gui as Splice
import lfo_gui as LFO

class MenuBar(tk.Menu):
    """
    A tkinter menu bar that contains a File menu and a Help menu.

    Parameters
    ----------
    parent: tkinter Menu object
        The parent menu that the MenuBar object will be contained within.

    Attributes
    ----------
    file_menu: tkinter Menu object
        A submenu for the File menu.
    help_menu: tkinter Menu object
        A submenu for the Help menu.
    """
    def __init__(self, parent):
        super().__init__(parent)
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="New", command=self.new_sample)
        file_menu.add_command(label="Exit", command=parent.destroy)
        self.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(self, tearoff=0)
        help_menu.add_command(label="Help", command=self.help_menu)
        self.add_cascade(label="Help", menu=help_menu)
    
    def new_sample(self):
        pass
    
    def help_menu(self):
        help_window = tk.Tk()
        help_window.title("Help")
        help_text = "This is a DX7 emulator. TIME, FREQ, AMP, and FDEV must all be a number. ADSR must\n \
            be values between 0 - 1, the sum of the first three entries must equal 1, the fourth\n \
            entry is the decay level and must be between 0 - 1. Export path must be exact. \n \
            Example: ./path/to/file.wav"
        help_label = tk.Label(help_window, text=help_text)
        help_label.grid(row=0,column=0)

class SynthRoot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sample Generator/Manipulator")
        self.menu_bar = MenuBar(self)
        self.config(menu=self.menu_bar)
        
        self.DX7_button = tk.Button(self, text="DX7 Emulator", command=self.open_DX7)
        self.DX7_button.grid(row=0,column=0)

        self.NENV_button = tk.Button(self, text="N Window Env", command=self.open_NENV)
        self.NENV_button.grid(row=1,column=0)
        
        self.Splice_button = tk.Button(self, text="Splice Wav", command=self.open_Splice)
        self.Splice_button.grid(row=2,column=0)

        self.LFO_button = tk.Button(self, text="LFO Generator", command=self.open_LFO)
        self.LFO_button.grid(row=3,column=0)
        
        self.mainloop() 

    def open_DX7(self):
        window = tk.Toplevel(self)
        window.title("DX7 Emulator")
        gui = DX.DX7Gui(window)
        gui.grid(row=0,column=0)

    def open_NENV(self):
        window = tk.Toplevel(self)
        window.title("N WINDOW ENVELOPE")
        gui = NEnv.NEnvGui(window)
        gui.grid(row=0,column=0)
    
    def open_Splice(self):
        window = tk.Toplevel(self)
        window.title("Splice WAV")
        gui = Splice.SpliceGui(window)
        gui.grid(row=0,column=0)
    
    def open_LFO(self):
        window = tk.Toplevel(self)
        window.title("LFO Generator")
        gui = LFO.LFOGui(window)
        gui.grid(row=0,column=0)