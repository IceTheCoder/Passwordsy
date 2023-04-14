"""
This module prepares the password strength for the user upon app startup.
"""
import tkinter as tk
from tkinter.font import Font
import customtkinter

from password_strength import password_strength_logic as logic

input_password_msg = 'Please input a password.'

copy_button_y_offset = 30


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

        self.paste = tk.Menu(self, tearoff=False)
        self.paste.add_command(label='Paste', command=logic.paste_text)

        instruction_label = customtkinter.CTkLabel(master=self, text='Type your password to check its strength',
                                                   font=title_font)
        instruction_label.grid(column=0, row=0)

        first_label = customtkinter.CTkLabel(master=self, font=warning_font, text=input_password_msg)

        second_label = customtkinter.CTkLabel(master=self, font=warning_font, text='')

        third_label = customtkinter.CTkLabel(master=self, font=warning_font, text='')

        fourth_label = customtkinter.CTkLabel(master=self, font=warning_font, text='')

        self.labels = [first_label, second_label, third_label, fourth_label]

        for label in self.labels:
            label.grid(column=0, row=2 + self.labels.index(label), sticky='n')

        self.input_box = customtkinter.CTkEntry(self, width=250, corner_radius=8)
        self.input_box.grid(column=0, row=1)
        # https://stackoverflow.com/questions/66035176/entry-widget-in-tkinter-with-key-bind
        self.input_box.bind('<KeyRelease>', lambda a: display_warnings(self.input_box, self.labels))
        self.input_box.bind('<Button-3>', lambda event: display_paste_button(event, self.paste))



def display_paste_button(event, paste_menu) -> None:
    """
    Called when the user right-clicks on the input_box,
    this function uses the Tkinter module to display a contextual menu
    containing a 'paste' button on the x and y coordinates of the user's cursor,
    with the y coordinates adjusted by 30 pixels.

    Parameters
    ----------
    event: tkinter.event
        Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
    paste_menu: tkinter.Menu
        The contextual menu containing the paste button.
    """
    paste_menu.tk_popup(event.x_root, event.y_root - copy_button_y_offset)


def display_warnings(entry_box, w_labels, event=None) -> None:
    """
    Called as the user types
    (when they release a key),
    this function clears all labels,
    gets a list of warnings through check_password_strength from password_strength_logic.py,
    and adequately displays them to the user.

    Parameters
    ----------
    entry_box: tkinter.Entry
        The input box of the password.
    w_labels: list
        Warning labels.
    event: tkinter.event
        Necessary for initiating the function as the user types.
    """
    for label in w_labels:
        label.configure(text='')

    warnings = logic.check_password_strength(entry_box.get(), input_password_msg)

    if warnings == input_password_msg:
        w_labels[0].configure(text=warnings)
        w_labels[0].grid(column=0, row=2, sticky='n')
    else:
        for index, warning in enumerate(warnings):
            w_labels[index].configure(text=warning)
        for label in w_labels:
            label.grid(column=0, row=2 + w_labels.index(label), sticky='w')
