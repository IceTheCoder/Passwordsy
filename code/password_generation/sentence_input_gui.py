"""
This module contains everything related to the GUI part of generating a password passed on an inputted sentence.
"""
import tkinter as tk
from tkinter.font import Font
import string

import password_generation.sentence_input_logic as logic


def create_sentence_input_frame(frame):
    """
    Called upon starting the app,
    this function prepares the 'input sentence' frame for when
    the user wants to try other methods of password generation
    by creating a basic Tkinter configuration, with an instruction, input, and a way to display the produced password.

    Parameters
    ----------
    frame: tk.Frame
        The 'input sentence' frame
    """
    instruction_font = Font(family='Roboto', size=16)
    warning_font = Font(family='Roboto', size=14)
    word_font = Font(family='Roboto', size=12)

    instruction_label = tk.Label(frame, text='Input a sentence', font=instruction_font)
    instruction_label.grid(row=0, column=0)

    input_box = tk.Entry(frame)
    input_box.grid(row=1, column=0, pady=10)

    password_label = tk.Text(frame, font=word_font, width=50, height=1)
    password_label.grid(row=2, column=0)

    warning_label_1 = tk.Label(frame, font=warning_font)
    warning_label_2 = tk.Label(frame, font=warning_font)
    warning_labels = [warning_label_1, warning_label_2]

    password_label.tag_config('red', foreground='red')

    def display_password():
        """
        Called as the user types,
        this function calls the produce_password function of sentence_input_logic.py
        to get a password based on the user's sentence,
        and displays it on the screen.
        """
        password_output = logic.produce_password(input_box.get())

        split_full_sentence = input_box.get().split(' ')
        letters_to_be_coloured = {}

        for word in split_full_sentence:
            letter_taken = False
            for character in word:
                if character in string.digits or character in string.punctuation:
                    letters_to_be_coloured[f'1.{str(input_box.get().index(character))}'] = f'1.{str(input_box.get().index(character) + 1)}'
                elif not letter_taken:
                    letters_to_be_coloured[f'1.{str(input_box.get().index(character))}'] = f'1.{str(input_box.get().index(character) + 1)}'
                    letter_taken = True

        if password_output != '':
            password_label.configure(state='normal')
            password_label.delete('1.0', 'end')
            password_label.insert('1.0', input_box.get())
            password_label.configure(state='disabled')

            for index, warning in enumerate(logic.check_password_strength(None, password_output)):
                warning_labels[index].configure(text=warning)
                warning_labels[index].grid(row=3 + index, column=0)
        else:
            for label in warning_labels:
                label.configure(text='')
                password_label.configure(state='normal')
                password_label.delete('1.0', 'end')
                password_label.configure(state='disabled')

        print(letters_to_be_coloured)
        for letter in letters_to_be_coloured:
            print(letter)

    input_box.bind('<Return>', lambda e: display_password())
