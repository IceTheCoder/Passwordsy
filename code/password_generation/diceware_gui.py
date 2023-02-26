import tkinter as tk

import password_generation.diceware_logic as logic


def create_diceware_frame(frame):
    roll_dice_button = tk.Button(frame, text='Roll dice', command=logic.roll_dice)
    roll_dice_button.grid(row=0, column=0)

    word_widget = tk.Text(frame)
    number_widget = tk.Text(frame)
