
import tkinter as tk

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
    instruction_label = tk.Label(frame, text='Input a sentence')
    instruction_label.grid(row=0, column=0)

    input_box = tk.Entry(frame)
    input_box.grid(row=1, column=0)

    def display_password():
        """

        """
        logic.produce_password(str(input_box.get()))

    input_box.bind('<KeyRelease>', lambda e: display_password())
