import tkinter as tk

import password_generation.sentence_input_logic as logic


def create_sentence_input_frame(frame):
    instruction_label = tk.Label(frame, text='Input a sentence')
    instruction_label.grid(row=0, column=0)

    input_box = tk.Entry(frame)
    input_box.grid(row=1, column=0)

    def display_password():
        logic.produce_password(str(input_box.get()))

    input_box.bind('<KeyRelease>', lambda e: display_password())
