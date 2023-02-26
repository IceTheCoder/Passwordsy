import tkinter as tk
import secrets

numbers = [1, 2, 3, 4, 5, 6]

# The wordlist is from https://github.com/ulif/diceware
diceware_wordlist = open('password_generation\wordlist_en_eff.txt', 'r')
diceware_wordlist_read = diceware_wordlist.readlines()
wordlist = {}

# Make a 'wordlist' dictionary, where the key is the dice roll numbers, and the value is the specific word.
for line in diceware_wordlist_read:
    # Split the line into a list of dice roll numbers and the corresponding word
    line_parts = line.strip().split('\t')
    dice_rolls = line_parts[0]
    word = line_parts[1]

    # Add the dice roll numbers and word to the dictionary
    wordlist[dice_rolls] = word

def create_diceware_frame(frame):
    def roll_dice():
        dice_roll = ''
        i = 0
        while i < 5:
            dice_roll += str(secrets.choice(numbers))
            i += 1


    roll_dice_button = tk.Button(frame, text='Roll dice', command=roll_dice)
    roll_dice_button.grid(row=0,column=0)
