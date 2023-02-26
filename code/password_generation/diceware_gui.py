import tkinter as tk

import password_generation.diceware_logic as logic


def create_diceware_frame(frame):
    roll_dice_button = tk.Button(frame, text='Roll dice', command=lambda: display_words(logic.roll_dice()))
    roll_dice_button.grid(row=0, column=0)

    pair_widget = tk.Text(frame)
    pair_widget.grid(row=1, column=0)

    def display_words(pair):
        pair_widget.configure(state='normal')
        pair_widget.delete('1.0', 'end')
        pair_widget.insert('1.0', pair)
        pair_widget.configure(state='disabled')
