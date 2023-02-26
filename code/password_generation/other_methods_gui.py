import tkinter as tk
from PIL import ImageTk, Image

from password_generation import diceware_gui as diceware


def create_other_methods_window():
    other_methods_window = tk.Toplevel()

    window_title = 'Try other methods...'

    other_methods_window.iconphoto(False, tk.PhotoImage(file='../logo.png'))
    other_methods_window.title(window_title)

    diceware_frame = tk.LabelFrame(other_methods_window, text='Diceware')
    diceware_frame.grid(row=0, column=0)

    sentence_input_frame = tk.LabelFrame(other_methods_window, text='Input a sentence')
    sentence_input_frame.grid(row=0, column=1)

    diceware.create_diceware_frame(diceware_frame)
    

    # Expand some widgets' rows and columns to take up the entire window
    other_methods_window.rowconfigure(0, weight=1)
    other_methods_window.columnconfigure(0, weight=1)
    other_methods_window.columnconfigure(1, weight=1)
