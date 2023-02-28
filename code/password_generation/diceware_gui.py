"""
Called upon opening the other methods' window,
this module prepares the diceware frame of the window,
with a set of functions for the GUI part of rolling dice and getting words from the diceware wordlist.
"""
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

import password_generation.diceware_logic as logic

global number_of_dicerolls
global roll_dice_btn_image
global clear_btn_image
global output_widgets

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
    global output_widgets
    output_widgets = []

    global number_of_dicerolls
    number_of_dicerolls = 0

    global roll_dice_btn_image
    roll_dice_btn_image = ImageTk.PhotoImage(Image.open('textures/roll_dice_btn.png'))

    roll_dice_button = tk.Button(frame, image=roll_dice_btn_image, borderwidth=0,
                                 command=lambda: display_words(logic.roll_dice()))
    roll_dice_button.grid(row=0, column=0, columnspan=5, pady=10)

    def clear_frame():
        """
        This function does nothing.
        """
        global output_widgets
        global number_of_dicerolls

        for widget in output_widgets:
            widget.destroy()

        output_widgets = []
        number_of_dicerolls = 0

    global clear_btn_image
    clear_btn_image = ImageTk.PhotoImage(Image.open('textures/clear_btn.png'))
    clear_button = tk.Button(frame, image=clear_btn_image, borderwidth=0, command=clear_frame)
    clear_button.grid(row=1, column=0, columnspan=5, pady=10)

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
        if number_of_dicerolls < 35:
            number_of_dicerolls += 1
            (diceroll, word), = pair.items()

            diceroll_widget = tk.Text(frame, font=word_font, height=1, width=len(word))
            diceroll_widget.grid(row=2 + 2 * ((number_of_dicerolls - 1) // 5), column=(-1 + number_of_dicerolls) % 5)
            diceroll_widget.configure(state='normal')
            diceroll_widget.delete('1.0', 'end')
            diceroll_widget.insert('1.0', str(diceroll))
            diceroll_widget.configure(state='disabled')
            output_widgets.append(diceroll_widget)

            word_widget = tk.Text(frame, font=word_font, height=1, width=len(word))
            word_widget.grid(row=3 + 2 * ((number_of_dicerolls - 1) // 5), column=(-1 + number_of_dicerolls) % 5)
            word_widget.configure(state='normal')
            word_widget.delete('1.0', 'end')
            word_widget.insert('1.0', str(word))
            word_widget.configure(state='disabled')
            output_widgets.append(word_widget)
        else:
            tk.mess
