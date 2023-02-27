"""
Called upon app startup, this module prepares the 'Try other methods...' window of the program for the user.
"""
import tkinter as tk

from password_generation import diceware_gui as diceware
from password_generation import sentence_input_gui as sentence_input


def create_other_methods_window() -> None:
    """
    Called upon app startup, this function prepares the other methods window for the user,
    by creating 2 frames: 1 for diceware, and 1 for sentence input.
    """
    other_methods_window = tk.Toplevel()

    window_title = 'Try other methods...'

    other_methods_window.iconphoto(False, tk.PhotoImage(file='textures/logo.png'))
    other_methods_window.title(window_title)

    diceware_frame = tk.LabelFrame(other_methods_window, text='Diceware')
    diceware_frame.grid(row=0, column=0)

    sentence_input_frame = tk.LabelFrame(other_methods_window, text='Input a sentence')
    sentence_input_frame.grid(row=0, column=1)

    diceware.create_diceware_frame(diceware_frame)
    sentence_input.create_sentence_input_frame(sentence_input_frame)

    # Expand some widgets' rows and columns to take up the entire window
    other_methods_window.rowconfigure(0, weight=1)
    other_methods_window.columnconfigure(0, weight=1)
    other_methods_window.columnconfigure(1, weight=1)

    other_methods_window.mainloop()
