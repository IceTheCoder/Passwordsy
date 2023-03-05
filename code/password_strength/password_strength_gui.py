"""
This module prepares the password strength for the user upon app startup.
"""
import tkinter as tk
from tkinter.font import Font
import customtkinter
from pynput.keyboard import Key, Controller

from password_strength import password_strength_logic

keyboard = Controller()

input_password_msg = 'Please input a password.'

copy_button_y_offset = 30

global paste
global input_box
global labels


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


def paste_text() -> None:
    """
    Called upon pressing the paste button,
    this function uses the keyboard module to simulate pressing CTRL and V to paste text into the input_box.
    """
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)
    keyboard.release('v')


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

    warnings = password_strength_logic.check_password_strength(None, input_box.get(), input_password_msg)

    if warnings == input_password_msg:
        labels[0].configure(text=warnings)
        labels[0].grid(column=0, row=2, sticky='n')
    else:
        for index, warning in enumerate(warnings):
            labels[index].configure(text=warning)
        for label in labels:
            label.grid(column=0, row=2 + labels.index(label), sticky='w')


def create_password_strength_frame(frame) -> None:
    """
    Called upon starting the program,
    this function creates the 'password strength' frame with a label for instructions,
    an entry box for password input, and four warning labels to display the strength of the password.
    It also creates a menu for pasting text, which is triggered by a right-click on the input box.

    Parameters
    ----------
    frame: ttk.Frame
        The 'password strength' frame
    """
    title_font = Font(family='Roboto', size=24)
    warning_font = Font(family='Roboto', size=16)

    global paste
    paste = tk.Menu(frame, tearoff=False)
    paste.add_command(label='Paste', command=paste_text)

    instruction_label = tk.Label(frame, text='Type your password to check its strength', font=title_font)
    instruction_label.grid(column=0, row=0)

    global input_box
    input_box = tk.Entry(frame, width=32, borderwidth=2)
    input_box.grid(column=0, row=1)
    input_box.bind('<KeyRelease>', display_warnings)
    input_box.bind('<Button-3>', display_paste_button)

    first_label = tk.Label(frame, font=warning_font, text=input_password_msg)

    second_label = tk.Label(frame, font=warning_font, text='')

    third_label = tk.Label(frame, font=warning_font, text='')

    fourth_label = tk.Label(frame, font=warning_font, text='')

    global labels
    labels = [first_label, second_label, third_label, fourth_label]

    for label in labels:
        label.grid(column=0, row=2 + labels.index(label), sticky='n')
