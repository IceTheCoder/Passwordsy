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


class DicewareToplevel(customtkinter.CTkToplevel):
    """
    This class creates the diceware toplevel.
    """

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry('1100x650')
        self.iconbitmap('textures/logo.ico')
        self.title('Diceware')

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
        self.word_font = customtkinter.CTkFont(family='Roboto', size=12)

        self.output_widgets = []

        button_font = customtkinter.CTkFont(family='Roboto', size=24)

        global number_of_dicerolls
        number_of_dicerolls = 0

        self.roll_dice_button = customtkinter.CTkButton(self, border_width=2, border_color='black', text='ROLL DICE',
                                                        font=button_font, fg_color='blue', hover_color='gray',
                                                        command=lambda: display_words(logic.roll_dice()))
        self.roll_dice_button.grid(row=0, column=0, columnspan=5, pady=0, sticky='n')

        self.copy_menu = tk.Menu(self, tearoff=False)
        self.copy_menu.add_command(label='Copy',
                                   command=lambda: logic.copy_selected_text(self.output_widgets))

        def show_copy_menu(event) -> None:
            """
            Called when the user releases a mouse button on a password label,
            this function uses the Tkinter module to display a contextual menu containing a 'copy' button
            for copying the password to the clipboard on the x and y coordinates of the user's cursor,
            where the y coordinates are adjusted by 30 pixels.

            Parameters
            ----------
            event: tkinter.event
                Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
            """
            print('Hello, world!')
            self.copy_menu.tk_popup(event.x_root, event.y_root - 30)

        def clear_window():
            """
            This function clears the window of any output widgets.
            """
            global number_of_dicerolls

            for widget in self.output_widgets:
                widget.destroy()

            self.output_widgets = []
            number_of_dicerolls = 0

        self.clear_button = customtkinter.CTkButton(self, border_width=2, border_color='black', text='CLEAR',
                                                    font=button_font, fg_color='blue', hover_color='gray',
                                                    command=clear_window)
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

                self.diceroll_widget = customtkinter.CTkTextbox(self, font=self.word_font, height=1)
                self.diceroll_widget.grid(row=2 + 2 * ((number_of_dicerolls - 1) // 5),
                                          column=(-1 + number_of_dicerolls) % 5,
                                          pady=(5, 0), padx=10)
                self.diceroll_widget.configure(state='normal')
                self.diceroll_widget.delete('1.0', 'end')
                self.diceroll_widget.insert('1.0', str(diceroll))
                self.diceroll_widget.configure(state='disabled')
                self.diceroll_widget.bind('<Button-3>', show_copy_menu)
                self.output_widgets.append(self.diceroll_widget)

                self.word_widget = customtkinter.CTkTextbox(self, font=self.word_font, height=1)
                self.word_widget.grid(row=3 + 2 * ((number_of_dicerolls - 1) // 5),
                                      column=(-1 + number_of_dicerolls) % 5,
                                      sticky='n', pady=(0, 5), padx=10)
                self.word_widget.configure(state='normal')
                self.word_widget.delete('1.0', 'end')
                self.word_widget.insert('1.0', str(word))
                self.word_widget.configure(state='disabled')
                self.word_widget.bind('<Button-3>', show_copy_menu)

                self.output_widgets.append(self.word_widget)
            else:
                answer = tk.messagebox.askquestion('Dice roll limit reached',
                                                   'You have reached the maximum limit of 35 dice rolls. Do you want '
                                                   'to clear the screen?', parent=self)
                if answer == 'yes':
                    clear_window()

        self.after(200, self.show_icon)

        def close_second_window():
            """
            This function destroys the window when it is closed.
            """
            self.destroy()
            self.master.deiconify()

        self.protocol("WM_DELETE_WINDOW", close_second_window)

    def show_icon(self):
        """
        This function shows the icon of the toplevel window.
        """
        self.iconbitmap('textures/logo.ico')
