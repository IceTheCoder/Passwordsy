"""This module deals with the logical part of generating a random secure password from the diceware wordlist."""
import secrets
import clipboard
from tkinter import TclError

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


def roll_dice() -> dict:
    """
    Called when the user clicks the 'dice roll' of the diceware frame,
    this function returns a random pair of the number formed by 5 dice rolls
    and the associated word with that number, according to the diceware wordlist.
    """
    final_pairs = {}
    dice_roll = ''

    i = 0
    while i < 5:
        dice_roll += str(secrets.choice(numbers))
        i += 1

    final_pairs[dice_roll] = wordlist[dice_roll]
    return final_pairs


def copy_selected_text(labels) -> None:
    """
    Called upon pressing the copy button,
    this function copies the selected text,
    and focuses the keyboard on the input_box to deselect the text.
    """
    try:
        for label in labels:
            selected_text = str(label.selection_get())
            clipboard.copy(selected_text)
    except (ValueError, TclError):
        # There is no need to warn the user when they try to copy nothing as it does not have any effect on the app
        pass


def copy_selections(checkboxes_text_boxes) -> None:
    """
    This function will copy the selected text boxes to the clipboard.
    """
    text_to_be_copied = ''
    for key, value in checkboxes_text_boxes.items():
        if value.get() == 1:
            text_to_be_copied += key.get('1.0', 'end')
    # Get rid of line-breaks and spaces
    text_to_be_copied = text_to_be_copied.replace("\n", "").replace(" ", "")
    clipboard.copy(text_to_be_copied)
