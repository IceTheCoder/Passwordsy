import tkinter as tk
import secrets

numbers = [1, 2, 3, 4, 5, 6]


def create_diceware_frame(frame):
    def roll_dice():
        dice_roll = ''
        i = 0
        while i < 5:
            dice_roll += str(secrets.choice(numbers))
            i += 1
        print(dice_roll)


    roll_dice_button = tk.Button(frame, text='Roll dice', command=roll_dice)
    roll_dice_button.grid(row=0,column=0)
