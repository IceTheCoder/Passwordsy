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
        # title_font = Font(family='Roboto', size=24)

        self.focus()

        self.geometry('1195x520')
        self.window_title = 'Try other methods...'

        self.iconphoto(False, tk.PhotoImage(file='textures/logo.png'))
        self.title(self.window_title)

        self.diceware_frame = diceware.DicewareFrame(master=self)
        self.diceware_frame.grid(row=0, column=0, sticky='nsew')

        # self.sentence_input_frame = tk.LabelFrame(self, text='Input a sentence', font=title_font)
        # self.sentence_input_frame.grid(row=0, column=1, sticky='nsew')

        # self.sentence_input.create_sentence_input_frame(sentence_input_frame)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
