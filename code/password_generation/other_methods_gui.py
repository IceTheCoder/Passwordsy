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
        self.button_border_width = 2
        self.button_fg_color = 'blue'
        self.button_hover_color = 'gray'
        self.button_border_color = 'black'

        self.medium_button_font = customtkinter.CTkFont(family='Roboto', size=24)
        self.title_font = customtkinter.CTkFont(family='Roboto', size=36)

        self.window_title = 'Try other methods...'

        self.iconbitmap('textures/logo.ico')
        self.geometry('700x250')
        self.title(self.window_title)

        self.frame_title = customtkinter.CTkLabel(master=self, text='How to generate a password?',
                                                  font=self.title_font)
        self.frame_title.grid(column=0, row=0, columnspan=3)

        self.question_mark = customtkinter.CTkLabel(master=self, text='❓', font=self.title_font)
        self.question_mark.grid(column=0, row=1, sticky='e', padx=10)

        self.diceware_btn = customtkinter.CTkButton(self,
                                                    text='From the diceware wordlist',
                                                    command=self.open_diceware,
                                                    font=self.medium_button_font,
                                                    border_width=self.button_border_width,
                                                    border_color=self.button_border_color,
                                                    fg_color=self.button_fg_color,
                                                    hover_color=self.button_hover_color)
        self.diceware_btn.grid(row=1, column=1, pady=10, sticky='w')

        self.sentence_input_btn = customtkinter.CTkButton(self,
                                                          text='From a sentence',
                                                          command=self.open_sentence_input,
                                                          font=self.medium_button_font,
                                                          border_width=self.button_border_width,
                                                          border_color=self.button_border_color,
                                                          fg_color=self.button_fg_color,
                                                          hover_color=self.button_hover_color)
        self.sentence_input_btn.grid(row=1, column=2, pady=10, sticky='w')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1, uniform='column')

        self.diceware_window = None
        self.sentence_input_window = None

        self.withdraw()
        self.after(200, self.show_icon)

    def show_icon(self):
        """
        This function shows the icon of the toplevel window.
        """
        self.deiconify()
        self.iconbitmap('textures/logo.ico')

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
        self.withdraw()
        if self.sentence_input_window is None or not self.sentence_input_window.winfo_exists():
            self.sentence_input_window = sentence_input.SentenceInputToplevel(self)
        else:
            self.sentence_input_window.focus()
