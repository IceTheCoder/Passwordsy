import tkinter as tk

import password_generation.diceware_logic as logic


def create_diceware_frame(frame):
    roll_dice_button = tk.Button(frame, text='Roll dice', command=lambda: display_words(logic.roll_dice()))
    roll_dice_button.grid(row=0, column=0)

    word_widget = tk.Text(frame)
    number_widget = tk.Text(frame)
    word_widget.grid(row=1, column=0)
    def display_words(pair):
        word_widget.configure(state='normal')
        word_widget.delete('1.0', 'end')
        word_widget.insert('1.0', pair)
        word_widget.configure(state='disabled')
