import tkinter as tk
from pynput.keyboard import Key, Controller
import password_strength_logic

keyboard = Controller()

title_font = 'Helvetica 24'
warning_font = 'Helvetica 16'

def display_paste_button(event) -> None:
    '''
    Called when the user right-clicks on the input_box,
    this function uses the Tkinter module to display a contextual menu containing a 'paste' button on the x and y coordinates of the user's cursor,
    where the y coordinates are adjusted by 30 pixels.

    Parameters
    ----------
    event:
        Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
    '''
    paste.tk_popup(event.x_root, event.y_root - 30)

def paste_text() -> None:
    '''
    Called upon pressing the paste button,
    this function uses the keyboard module to simulate pressing CTRL and V to copy the selected text.
    '''
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)
    keyboard.release('v')

def create_password_strength_frame(frame) -> None:
    '''
    Called upon starting the program,
    this function creates the "password strength" frame with a label for instructions, 
    an entry box for password input, and four warning labels to display the strength of the password. 
    It also creates a menu for pasting text, which is triggered by a right-click on the input box.

    Parameters
    ----------
    frame: ttk.Frame
        The "password strength" frame
    '''

    global paste
    paste = tk.Menu(frame, tearoff = False)
    paste.add_command(label = 'Paste', command = paste_text)

    instruction_label = tk.Label(frame, text = 'Type your password to check its strength', font = title_font)
    instruction_label.grid(column = 0, row = 1)

    global input_box
    input_box = tk.Entry(frame, width = 32, borderwidth = 2)
    input_box.grid(column = 0, row = 2)
    input_box.bind('<KeyRelease>', lambda abcdefgh: password_strength_logic.check_password_strength(None, warnings, first_label, input_box.get(), second_label, third_label, fourth_label))
    input_box.bind('<Button-3>', display_paste_button)

    global first_label
    first_label = tk.Label(frame, font = warning_font, text = '')
    
    global second_label
    second_label = tk.Label(frame, font = warning_font, text = '')

    global third_label
    third_label = tk.Label(frame, font = warning_font, text = '')

    global fourth_label
    fourth_label = tk.Label(frame, font = warning_font, text = '')

    global warnings
    warnings = [first_label, second_label, third_label, fourth_label]

    for label in warnings:
        label.grid(column = 0, row = 3 + warnings.index(label))
