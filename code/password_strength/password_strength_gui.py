"""
This module prepares the password strength for the user upon app startup.
"""
import tkinter
import tkinter as tk
from tkinter.font import Font
import customtkinter
from pynput.keyboard import Key, Controller

from password_strength import password_strength_logic as logic
import diacritics_fix as fix

input_password_msg = 'Please input a password.'

copy_button_y_offset = 30

keyboard = Controller()


class PasswordStrengthFrame(customtkinter.CTkFrame):
    """
    Called upon starting the program,
    this class creates the 'password strength' frame with a label for instructions,
    an entry box for password input, and four warning labels to display the strength of the password.
    It also creates a menu for pasting text, which is triggered by a right-click on the input box.
    """
    def __init__(self, master: customtkinter.CTkFrame, **kwargs) -> None:
        super().__init__(master, **kwargs)
        title_font = customtkinter.CTkFont(family='Roboto', size=36)
        warning_font = customtkinter.CTkFont(family='Roboto', size=24)

        self.paste = tk.Menu(self, tearoff=False)
        self.paste.add_command(label='Paste', command=paste_text)

        self.instruction_label = customtkinter.CTkLabel(master=self, text='Type your password to check its strength',
                                                        font=title_font)
        self.instruction_label.grid(column=0, row=0)

        self.first_label = customtkinter.CTkLabel(master=self, font=warning_font, text=input_password_msg)

        self.second_label = customtkinter.CTkLabel(master=self, font=warning_font, text='')

        self.third_label = customtkinter.CTkLabel(master=self, font=warning_font, text='')

        self.fourth_label = customtkinter.CTkLabel(master=self, font=warning_font, text='')

        self.labels = [self.first_label, self.second_label, self.third_label, self.fourth_label]

        for label in self.labels:
            label.grid(column=0, row=2 + self.labels.index(label), sticky='n')

        self.input_box = customtkinter.CTkEntry(self, width=250, corner_radius=8)
        self.input_box.grid(column=0, row=1)

        all_ui = [self.paste, self.instruction_label, self.input_box] + self.labels

        # https://stackoverflow.com/questions/66035176/entry-widget-in-tkinter-with-key-bind
        self.input_box.bind('<KeyRelease>', lambda a: display_warnings(self.input_box, self.labels))
        self.input_box.bind('<Button-3>', lambda event: display_paste_button(event, self.paste))
        self.input_box.bind('<KeyPress>', fix.on_key_press)
        # https://stackoverflow.com/questions/75846986/certain-characters-like-%c8%9b-and-%c8%99-become-question-marks-as-i-type-them-in-a-tkin/76015278#76015278

        for ui in all_ui:
            ui.bind('<Button-1>', lambda a: display_warnings(self.input_box, self.labels))
            ui.bind('<Button-3>', lambda a: display_warnings(self.input_box, self.labels))


def display_paste_button(event: tkinter.Event, paste_menu: tkinter.Menu) -> None:
    """
    Called when the user right-clicks on the input_box,
    this function uses the Tkinter module to display a contextual menu
    containing a 'paste' button on the x and y coordinates of the user's cursor,
    with the y coordinates adjusted by 30 pixels.

    Parameters
    ----------
    event: tkinter.Event
        Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
    paste_menu: tkinter.Menu
        The contextual menu containing the paste button.

    Returns
    -------
    None
    """
    paste_menu.tk_popup(event.x_root, event.y_root - copy_button_y_offset)


def display_warnings(entry_box: customtkinter.CTkEntry, w_labels: list, event: tkinter.Event = None) -> None:
    """
    Called as the user types
    (when they release a key),
    this function clears all labels,
    gets a list of warnings through check_password_strength from password_strength_logic.py,
    and adequately displays them to the user.

    Parameters
    ----------
    entry_box: customtkinter.CTkEntry
        The input box of the password.
    w_labels: list
        Warning labels.
    event: tkinter.Event
        Necessary for initiating the function as the user types.

    Returns
    -------
    None
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


def paste_text() -> None:
    """
    Called upon pressing the paste button,
    this function uses the keyboard module to simulate pressing CTRL and V to paste text into the input_box.

    Returns
    -------
    None
    """
    # https://youtu.be/DTnz8wA6wpw
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)
    keyboard.release('v')
