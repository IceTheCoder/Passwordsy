"""
This module prepares the password strength for the user upon app startup.
"""
import tkinter as tk
from tkinter.font import Font
import customtkinter
from pynput.keyboard import Key, Controller

from password_strength import password_strength_logic as logic

keyboard = Controller()

input_password_msg = 'Please input a password.'

copy_button_y_offset = 30

global paste
global input_box
global labels


class PasswordStrengthFrame(customtkinter.CTkFrame):
    """
    Called upon starting the program,
    this class creates the 'password strength' frame with a label for instructions,
    an entry box for password input, and four warning labels to display the strength of the password.
    It also creates a menu for pasting text, which is triggered by a right-click on the input box.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        title_font = customtkinter.CTkFont(family='Roboto', size=36)
        warning_font = customtkinter.CTkFont(family='Roboto', size=24)

        global paste
        paste = tk.Menu(self, tearoff=False)
        paste.add_command(label='Paste', command=logic.paste_text)

        instruction_label = customtkinter.CTkLabel(master=self, text='Type your password to check its strength',
                                                   font=title_font)
        instruction_label.grid(column=0, row=0)

        global input_box
        input_box = customtkinter.CTkEntry(self, width=250, corner_radius=8)
        input_box.grid(column=0, row=1)
        input_box.bind('<KeyRelease>', display_warnings)
        input_box.bind('<Button-3>', display_paste_button)

        first_label = customtkinter.CTkLabel(master=self, font=warning_font, text=input_password_msg)

        second_label = customtkinter.CTkLabel(master=self, font=warning_font, text='')

        third_label = customtkinter.CTkLabel(master=self, font=warning_font, text='')

        fourth_label = customtkinter.CTkLabel(master=self, font=warning_font, text='')

        global labels
        labels = [first_label, second_label, third_label, fourth_label]

        for label in labels:
            label.grid(column=0, row=2 + labels.index(label), sticky='n')


def display_paste_button(event) -> None:
    """
    Called when the user right-clicks on the input_box,
    this function uses the Tkinter module to display a contextual menu
    containing a 'paste' button on the x and y coordinates of the user's cursor,
    with the y coordinates adjusted by 30 pixels.

    Parameters
    ----------
    event: tkinter.event
        Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
    """
    paste.tk_popup(event.x_root, event.y_root - copy_button_y_offset)


def display_warnings(event) -> None:
    """
    Called as the user types
    (when they release a key),
    this function clears all labels,
    gets a list of warnings through check_password_strength from password_strength_logic.py,
    and adequately displays them to the user.

    Parameters
    ----------
    event:
        Necessary for initiating the function as the user types.
    """
    for label in labels:
        label.configure(text='')

    warnings = logic.check_password_strength(input_box.get(), input_password_msg)

    if warnings == input_password_msg:
        labels[0].configure(text=warnings)
        labels[0].grid(column=0, row=2, sticky='n')
    else:
        for index, warning in enumerate(warnings):
            labels[index].configure(text=warning)
        for label in labels:
            label.grid(column=0, row=2 + labels.index(label), sticky='w')
