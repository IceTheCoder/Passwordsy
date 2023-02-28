"""
This module contains everything related to the GUI part of generating a password passed on an inputted sentence.
"""
import tkinter as tk
from tkinter.font import Font

import password_generation.sentence_input_logic as logic


def create_sentence_input_frame(frame):
    """
    Called upon starting the app,
    this function prepares the 'input sentence' frame for when
    the user wants to try other methods of password generation
    by creating a basic Tkinter configuration, with an instruction, input, and a way to display the produced password.

    Parameters
    ----------
    frame: tk.Frame
        The 'input sentence' frame
    """
    instruction_font = Font(family='Roboto', size=16)
    word_font = Font(family='Roboto', size=12)

    instruction_label = tk.Label(frame, text='Input a sentence', font=instruction_font)
    instruction_label.grid(row=0, column=0)

    input_box = tk.Entry(frame)
    input_box.grid(row=1, column=0, pady=10)

    password_label = tk.Text(frame, font=word_font)
    password_label.grid(row=2, column=0)

    def display_password():
        """
        Called as the user types,
        this function calls the produce_password function of sentence_input_logic.py
        to get a password based on the user's sentence,
        and displays it on the screen.
        """
        password_label.configure(state='normal')
        password_label.delete('1.0', 'end')
        password_label.insert('1.0', logic.produce_password(str(input_box.get())))
        password_label.configure(state='disabled')

    input_box.bind('<KeyRelease>', lambda e: display_password())
