"""
This module contains everything related to the GUI part of generating a password passed on an inputted sentence.
"""
import tkinter as tk
import customtkinter
import string

import password_generation.sentence_input_logic as logic


class SentenceInputToplevel(customtkinter.CTkToplevel):
    """
    This class creates the sentence input toplevel
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        """
        Called upon starting the app,
        this function prepares the 'input sentence' frame for when
        the user wants to try other methods of password generation
        by creating a basic Tkinter configuration, with an instruction, input,
        and a way to display the produced password.
        """
        self.grid_rowconfigure(0, weight=1, uniform='row')
        self.grid_rowconfigure(1, weight=1, uniform='row')
        self.grid_rowconfigure(2, weight=1, uniform='row')
        self.grid_rowconfigure(3, weight=1, uniform='row')
        self.grid_rowconfigure(4, weight=1, uniform='row')
        self.grid_columnconfigure(0, weight=1, uniform='column')

        self.instruction_font = customtkinter.CTkFont(family='Roboto', size=24)
        self.warning_font = customtkinter.CTkFont(family='Roboto', size=20)
        self.word_font = customtkinter.CTkFont(family='Roboto', size=14)

        self.instruction_label = customtkinter.CTkLabel(master=self, text='Input a sentence', font=self.instruction_font)
        self.instruction_label.grid(row=0, column=0)

        self.input_box = customtkinter.CTkEntry(self, width=500, corner_radius=8.5)
        self.input_box.grid(row=1, column=0)

        self.password_label = customtkinter.CTkTextbox(self, font=self.word_font, width=500, height=50)
        self.password_label.grid(row=2, column=0)

        self.warning_label_1 = customtkinter.CTkLabel(master=self, font=self.warning_font)
        self.warning_label_2 = customtkinter.CTkLabel(master=self, font=self.warning_font)
        self.warning_labels = [self.warning_label_1, self.warning_label_2]

        self.password_label.tag_config('red', foreground='red')

        def display_password():
            """
            Called as the user types,
            this function calls the produce_password function of sentence_input_logic.py
            to get a password based on the user's sentence,
            and displays it on the screen.
            """
            password_output = logic.produce_password(self.input_box.get())

            split_full_sentence = self.input_box.get().split(' ')
            letters_to_be_coloured = {}

            for word in split_full_sentence:
                start_index = self.input_box.get().index(word)
                letters_to_be_coloured[f'1.{start_index}'] = f'1.{start_index + 1}'

            for i in range(len(self.input_box.get())):
                character = self.input_box.get()[i]
                if character in string.digits + string.punctuation:
                    # Find the start index of the character
                    start_index = i
                    # Iterate over the remaining characters in the sentence to find any additional occurrences
                    for j in range(i + 1, len(self.input_box.get())):
                        if self.input_box.get()[j] == character:
                            # Add the start and end indices of the character to the dictionary
                            letters_to_be_coloured[f'1.{start_index}'] = f'1.{j + 1}'
                    # Add the start and end indices of the character to the dictionary for the first occurrence
                    if f'1.{start_index}' not in letters_to_be_coloured:
                        letters_to_be_coloured[f'1.{start_index}'] = f'1.{start_index + 1}'

            if password_output != '':
                self.password_label.configure(state='normal')
                self.password_label.delete('1.0', 'end')
                self.password_label.insert('1.0', self.input_box.get())
                self.password_label.configure(state='disabled')

                for index, warning in enumerate(logic.check_password_strength(None, password_output)):
                    self.warning_labels[index].configure(text=warning)
                    self.warning_labels[index].grid(row=3 + index, column=0, padx=10)
            else:
                for label in self.warning_labels:
                    label.configure(text='')
                    self.password_label.configure(state='normal')
                    self.password_label.delete('1.0', 'end')
                    self.password_label.configure(state='disabled')

            for letter in letters_to_be_coloured:
                self.password_label.tag_add('red', letter, letters_to_be_coloured[letter])

        self.input_box.bind('<Return>', lambda e: display_password())
