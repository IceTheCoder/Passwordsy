import tkinter as tk
from PIL import ImageTk, Image

import password_generation.diceware_logic as logic

global roll_dice_btn_image
global number_of_dicerolls

word_font = 'Helvetica 12'


def create_diceware_frame(frame):
    """
    Called upon loading the pop-up window,
    this function prepares the diceware frame for when the user decides to try other methods of password generations,
    by setting up a Tkinter frame with a button, an entry box, and a text widget.

    Parameters
    ----------
    frame: tk.Frame
        The frame upon which the elements of dice ware shall be.
    """
    global number_of_dicerolls
    number_of_dicerolls = 0

    global roll_dice_btn_image
    roll_dice_btn_image = ImageTk.PhotoImage(Image.open('textures/roll_dice_btn.png'))

    roll_dice_button = tk.Button(frame, image=roll_dice_btn_image, borderwidth=0,
                                 command=lambda: display_words(logic.roll_dice()))
    roll_dice_button.grid(row=0, column=0, columnspan=5)

    def display_words(pair):
        """
        Called when the user clicks the 'roll dice' button,
        this function displays the pairs of dice rolls and words to the user.

        Parameters
        ----------
        pair: dict
            Contains the pairs of dice roll numbers and related words according to the dice ware wordlist.
        """
        global number_of_dicerolls
        number_of_dicerolls += 1
        (diceroll, word), = pair.items()

        diceroll_widget = tk.Text(frame, font=word_font, height=1, width=len(word))
        diceroll_widget.grid(row=2 + 2 * ((number_of_dicerolls - 1) // 5), column=(-1 + number_of_dicerolls) % 5)
        diceroll_widget.configure(state='normal')
        diceroll_widget.delete('1.0', 'end')
        diceroll_widget.insert('1.0', str(diceroll))
        diceroll_widget.configure(state='disabled')

        word_widget = tk.Text(frame, font=word_font, height=1, width=len(word))
        word_widget.grid(row=3 + 2 * ((number_of_dicerolls - 1) // 5), column=(-1 + number_of_dicerolls) % 5)
        word_widget.configure(state='normal')
        word_widget.delete('1.0', 'end')
        word_widget.insert('1.0', str(word))
        word_widget.configure(state='disabled')
