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
    frame.grid_rowconfigure(0, weight=1, uniform='row')
    frame.grid_rowconfigure(1, weight=1, uniform='row')
    frame.grid_rowconfigure(2, weight=1, uniform='row')
    frame.grid_rowconfigure(3, weight=1, uniform='row')
    frame.grid_rowconfigure(4, weight=1, uniform='row')
    frame.grid_columnconfigure(0, weight=1, uniform='column')

    instruction_font = Font(family='Roboto', size=16)
    warning_font = Font(family='Roboto', size=14)
    word_font = Font(family='Roboto', size=12)

    instruction_label = customtkinter.CTkLabel(master=frame, text='Input a sentence', font=instruction_font)
    instruction_label.grid(row=0, column=0)

    input_box = tk.Entry(frame)
    input_box.grid(row=1, column=0, pady=10)

    password_label = tk.Text(frame, font=word_font, width=50, height=1)
    password_label.grid(row=2, column=0)

    warning_label_1 = customtkinter.CTkLabel(master=frame, font=warning_font)
    warning_label_2 = customtkinter.CTkLabel(master=frame, font=warning_font)
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
            start_index = input_box.get().index(word)
            letters_to_be_coloured[f'1.{start_index}'] = f'1.{start_index + 1}'

        for i in range(len(input_box.get())):
            character = input_box.get()[i]
            if character in string.digits + string.punctuation:
                # Find the start index of the character
                start_index = i
                # Iterate over the remaining characters in the sentence to find any additional occurrences
                for j in range(i + 1, len(input_box.get())):
                    if input_box.get()[j] == character:
                        # Add the start and end indices of the character to the dictionary
                        letters_to_be_coloured[f'1.{start_index}'] = f'1.{j + 1}'
                # Add the start and end indices of the character to the dictionary for the first occurrence
                if f'1.{start_index}' not in letters_to_be_coloured:
                    letters_to_be_coloured[f'1.{start_index}'] = f'1.{start_index + 1}'

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

        for letter in letters_to_be_coloured:
            password_label.tag_add('red', letter, letters_to_be_coloured[letter])

    input_box.bind('<Return>', lambda e: display_password())
