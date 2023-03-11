"""
This module prepares the other_methods_window for the user when they click the 'try other methods...' button.
"""
import tkinter as tk
from tkinter.font import Font
import customtkinter

from password_generation import diceware_gui as diceware
from password_generation import sentence_input_gui as sentence_input


class OtherMethodsWindow(customtkinter.CTkToplevel):
    """
    This class contains the creation of the 'other methods' Toplevel window
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        medium_button_font = customtkinter.CTkFont(family='Roboto', size=24)
        title_font = customtkinter.CTkFont(family='Roboto', size=36)

        self.deiconify()

        self.window_title = 'Try other methods...'

        self.iconbitmap('textures/logo.ico')
        self.geometry('800x300')
        self.title(self.window_title)

        self.frame_title = customtkinter.CTkLabel(master=self, text='How would you like to generate a password?',
                                                  font=title_font)
        self.frame_title.grid(column=0, row=0, columnspan=2)

        self.diceware_btn = customtkinter.CTkButton(self, text='From the diceware wordlist', command=self.open_diceware,
                                                    font=medium_button_font, border_width=2,
                                                    border_color='black', fg_color='blue', hover_color='gray')
        self.diceware_btn.grid(row=1, column=0)

        self.sentence_input_btn = customtkinter.CTkButton(self, text='From a sentence',
                                                          command=self.open_sentence_input,
                                                          font=medium_button_font, border_width=2,
                                                          border_color='black', fg_color='blue', hover_color='gray')
        self.sentence_input_btn.grid(row=1, column=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # self.diceware_frame = diceware.DicewareFrame(master=self)
        # self.diceware_frame.grid(row=0, column=0, sticky='nsew')

        # self.sentence_input_frame = tk.LabelFrame(self, text='Input a sentence', font=title_font)
        # self.sentence_input_frame.grid(row=0, column=1, sticky='nsew')

        # self.sentence_input.create_sentence_input_frame(sentence_input_frame)

        self.after(200, self.show_icon)

        self.diceware_window = None

    def open_diceware(self):
        """
        Called when the user clicks on the 'From the diceware' button,
        this function opens the diceware Toplevel window.
        """
        self.withdraw()
        if self.diceware_window is None or not self.diceware_window.winfo_exists():
            self.diceware_window = diceware.DicewareToplevel(self)
        else:
            self.diceware_window.focus()

    def open_sentence_input(self):
        """
        Called when the user clicks on the 'From a sentence' button,
        this function opens the sentence input Toplevel window.
        """
        pass

    def show_icon(self):
        """
        This function shows the icon of the toplevel window.
        """
        self.iconbitmap('textures/logo.ico')
