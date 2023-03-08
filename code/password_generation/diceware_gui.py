"""
Called upon opening the other methods' window,
this module prepares the diceware frame of the window,
with a set of functions for the GUI part of rolling dice and getting words from the diceware wordlist.
"""
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from PIL import ImageTk, Image
import customtkinter

import password_generation.diceware_logic as logic

global number_of_dicerolls
global clear_btn_image


class DicewareFrame(customtkinter.CTkFrame):
    """
    This class creates the diceware frame.
    """

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1, uniform='row')
        self.grid_rowconfigure(1, weight=1, uniform='row')
        self.grid_rowconfigure(2, weight=1, uniform='row')
        self.grid_rowconfigure(3, weight=1, uniform='row')
        self.grid_rowconfigure(4, weight=1, uniform='row')
        self.grid_rowconfigure(5, weight=1, uniform='row')
        self.grid_rowconfigure(6, weight=1, uniform='row')
        self.grid_rowconfigure(7, weight=1, uniform='row')
        self.grid_rowconfigure(8, weight=1, uniform='row')
        self.grid_rowconfigure(9, weight=1, uniform='row')
        self.grid_rowconfigure(10, weight=1, uniform='row')
        self.grid_rowconfigure(11, weight=1, uniform='row')
        self.grid_rowconfigure(12, weight=1, uniform='row')
        self.grid_rowconfigure(13, weight=1, uniform='row')
        self.grid_rowconfigure(14, weight=1, uniform='row')
        self.grid_rowconfigure(15, weight=1, uniform='row')
        self.grid_columnconfigure(0, weight=1, uniform='column')
        self.grid_columnconfigure(1, weight=1, uniform='column')
        self.grid_columnconfigure(2, weight=1, uniform='column')
        self.grid_columnconfigure(3, weight=1, uniform='column')
        self.grid_columnconfigure(4, weight=1, uniform='column')
        self.word_font = Font(family='Roboto', size=12)

        self.output_widgets = []

        button_font = customtkinter.CTkFont(family='Roboto', size=24)

        global number_of_dicerolls
        number_of_dicerolls = 0

        self.roll_dice_button = customtkinter.CTkButton(self, border_width=2, border_color='black', text='ROLL DICE',
                                                        font=button_font, fg_color='blue', hover_color='gray',
                                                        command=lambda: display_words(logic.roll_dice()))
        self.roll_dice_button.grid(row=0, column=0, columnspan=5, pady=0, sticky='n')

        def clear_frame():
            """
            This function does nothing.
            """
            global number_of_dicerolls

            for widget in self.output_widgets:
                widget.destroy()

            self.output_widgets = []
            number_of_dicerolls = 0

        global clear_btn_image
        clear_btn_image = ImageTk.PhotoImage(Image.open('textures/clear_btn.png'))
        self.clear_button = customtkinter.CTkButton(self, border_width=2, border_color='black', text='CLEAR',
                                                    font=button_font, fg_color='blue', hover_color='gray',
                                                    command=clear_frame)
        self.clear_button.grid(row=1, column=0, columnspan=5, pady=0, sticky='n')

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

                self.diceroll_widget = tk.Text(self, font=self.word_font, height=1, width=len(word))
                self.diceroll_widget.grid(row=2 + 2 * ((number_of_dicerolls - 1) // 5),
                                          column=(-1 + number_of_dicerolls) % 5)
                self.diceroll_widget.configure(state='normal')
                self.diceroll_widget.delete('1.0', 'end')
                self.diceroll_widget.insert('1.0', str(diceroll))
                self.diceroll_widget.configure(state='disabled')
                self.output_widgets.append(self.diceroll_widget)

                self.word_widget = tk.Text(self, font=self.word_font, height=1, width=len(word))
                self.word_widget.grid(row=3 + 2 * ((number_of_dicerolls - 1) // 5),
                                      column=(-1 + number_of_dicerolls) % 5,
                                      sticky='n')
                self.word_widget.configure(state='normal')
                self.word_widget.delete('1.0', 'end')
                self.word_widget.insert('1.0', str(word))
                self.word_widget.configure(state='disabled')
                self.output_widgets.append(self.word_widget)
            else:
                tk.messagebox.showwarning('Dice roll limit reached',
                                          'You have reached the maximum limit of 35 dice rolls.', parent=master)
