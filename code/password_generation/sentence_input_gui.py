import tkinter as tk


def create_sentence_input_frame(frame):
    instruction_label = tk.Label(frame, text='Input a sentence')
    instruction_label.grid(row=0, column=0)

    input_box = tk.Entry(frame)
    input_box.grid(row=1, column=0)

    def display_password():
        pass

    input_box.bind('<KeyRelease', display_password)
