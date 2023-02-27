import tkinter as tk
from PIL import ImageTk, Image

import password_generation.diceware_logic as logic

global roll_dice_btn_image


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
    print('Hello, wordl!')
    global roll_dice_btn_image
    roll_dice_btn_image = ImageTk.PhotoImage(Image.open('textures/roll_dice_btn.png'))

    roll_dice_button = tk.Button(frame, image=roll_dice_btn_image, borderwidth=0,
                                 command=display_words(logic.roll_dice))
    roll_dice_button.grid(row=0, column=0)

    pair_widget = tk.Text(frame)
    pair_widget.grid(row=2, column=0)

    def display_words(pair):
        """
        Called when the user clicks the 'roll dice' button,
        this function displays the pairs of dice rolls and words to the user.

        Parameters
        ----------
        pair: dict
            Contains the pairs of dice roll numbers and related words according to the dice ware wordlist.
        """
        pair_widget.configure(state='normal')
        pair_widget.delete('1.0', 'end')
        pair_widget.insert('1.0', str(pair))
        pair_widget.configure(state='disabled')
