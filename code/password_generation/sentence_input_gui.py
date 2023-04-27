"""
This module contains everything related to the GUI part of generating a password passed on an inputted sentence.
"""
import tkinter as tk
from PIL import ImageTk, Image
import customtkinter
import string

import password_generation.sentence_input_logic as logic


class SentenceInputToplevel(customtkinter.CTkToplevel):
    """
    This class creates the sentence input toplevel
    """
    def __init__(self, master: customtkinter.CTkToplevel, **kwargs) -> None:
        super().__init__(master, **kwargs)
        """
        Called upon starting the app,
        this function prepares the 'input sentence' frame for when
        the user wants to try other methods of password generation
        by creating a basic Tkinter configuration, with an instruction, input,
        and a way to display the produced password.
        """
        self.geometry('900x300')
        self.title('Sentence input')
        self.iconbitmap('textures/logo.ico')

        i = 0
        while i <= 4:
            self.grid_rowconfigure(i, weight=1, uniform='row')
            i += 1
        self.grid_columnconfigure(0, weight=1, uniform='column')

        self.instruction_font = customtkinter.CTkFont(family='Roboto', size=24)
        self.warning_font = customtkinter.CTkFont(family='Roboto', size=20)
        self.word_font = customtkinter.CTkFont(family='Roboto', size=14)
        self.password_font = customtkinter.CTkFont(family='Consolas', size=18)

        self.instruction_label = customtkinter.CTkLabel(master=self, text='Input a sentence',
                                                        font=self.instruction_font)
        self.instruction_label.place(relx=0.5, rely=0.075, anchor='center')

        self.input_box = customtkinter.CTkEntry(self, width=700, corner_radius=8, font=self.word_font)
        self.input_box.place(relx=0.5, rely=0.2, anchor='center')

        def show_copy_menu(event: tk.Event) -> None:
            """
            Called when the user releases a mouse button on a password label,
            this function uses the Tkinter module to display a contextual menu containing a 'copy' button
            for copying the password to the clipboard on the x and y coordinates of the user's cursor,
            where the y coordinates are adjusted by 30 pixels.

            Parameters
            ----------
            event: tk.Event
                Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
            """
            self.copy_menu.tk_popup(event.x_root, event.y_root - 30)

        self.password_label = customtkinter.CTkTextbox(self, state='disabled', height=25, width=500,
                                                       font=self.password_font)
        self.password_label.place(relx=0.5, rely=0.35, anchor='center')
        self.password_label.bind('<Button-3>', show_copy_menu)

        self.sentence_label = customtkinter.CTkTextbox(self, font=self.word_font, width=500, height=50, wrap='word',
                                                       state='disabled')

        self.sentence_label.place(relx=0.5, rely=0.55, anchor='center')
        self.sentence_label.bind('<Button-3>', show_copy_menu)

        self.text_labels = [self.password_label, self.sentence_label]

        self.warning_label_1 = customtkinter.CTkLabel(master=self, font=self.warning_font)
        self.warning_label_2 = customtkinter.CTkLabel(master=self, font=self.warning_font)
        self.warning_labels = [self.warning_label_1, self.warning_label_2]

        # https://www.tutorialspoint.com/how-to-change-the-color-of-certain-words-in-a-tkinter-text-widget
        self.sentence_label.tag_config('red', foreground='red')

        self.copy_menu = tk.Menu(self, tearoff=False)
        self.copy_menu.add_command(label='Copy',
                                   command=lambda: logic.copy_selected_text(self.text_labels))

        def highlight_sentence(event: tk.Event):
            """
            Called as the user types,
            this function calls the produce_password function of sentence_input_logic.py
            to get a password based on the user's sentence,
            and displays it on the screen.

            Parameters
            ----------
            event: tk.Event
                Necessary for running the function as the user types.
            """
            char_dict = {}

            self.sentence_label.configure(state='normal')

            self.sentence_label.delete('1.0', 'end')
            self.sentence_label.insert('1.0', self.input_box.get())

            for index, char in enumerate(self.input_box.get()):
                if char.isspace():
                    char_dict[index] = "space"
                else:
                    char_dict[index] = char

            characters_to_be_highlighted = logic.produce_password(char_dict)[0].items()
            password = logic.produce_password(char_dict)[1]

            for key, value in characters_to_be_highlighted:
                self.sentence_label.tag_add('red', key, value)

            display_warnings(logic.check_password_strength(password))
            show_password(password)
            self.sentence_label.configure(state='disabled')

        def show_password(password: str) -> None:
            """
            This function shows the password generated from a sentence.

            Parameters
            ----------
            password: str
                The password to be shown generated from the sentence.
            """
            self.password_label.configure(state='normal')
            self.password_label.delete('1.0', 'end')
            self.password_label.insert('1.0', password)
            self.password_label.configure(state='disabled')

        def display_warnings(warnings: list) -> None:
            """
            Called as the user types,
            this function displays the adequate warnings/tips for the user to get a more secure password.

            Parameters
            ----------
            warnings: list
                List of the tips for the user's password.
            """
            self.warning_label_1.configure(text=warnings[0])
            self.warning_label_1.place(relx=0.5, rely=0.75, anchor='center')
            self.warning_label_2.configure(text=warnings[1])
            self.warning_label_2.place(relx=0.5, rely=0.9, anchor='center')

        self.input_box.bind('<Key>', highlight_sentence)
        self.input_box.bind('<KeyRelease>', highlight_sentence)
        self.input_box.bind('<KeyPress>', fix.on_key_press)
        # https://stackoverflow.com/questions/75846986/certain-characters-like-%c8%9b-and-%c8%99-become-question-marks-as-i-type-them-in-a-tkin/76015278#76015278

        self.withdraw()
        self.after(200, self.show_icon)

        def close_second_window() -> None:
            """
            This function destroys the window when it is closed.
            """
            self.destroy()
            self.master.deiconify()

        self.protocol("WM_DELETE_WINDOW", close_second_window)

    def show_icon(self) -> None:
        """
        This function shows the icon of the toplevel window.
        """
        self.deiconify()
        self.iconbitmap('textures/logo.ico')
