import secrets
import string
import tkinter as tk
from pynput.keyboard import Key, Controller

title_font = 'Helvetica 24'
section_title_font = 'Helvetica 16'
description_font = 'Helvetica 12'

keyboard = Controller()

password_width = 100
password_height = 1
password_border_width = 0
password_font = 'Consolas 11'

invalid_input_error = 'An error occurred. Try again with a whole number between 4 and 100.'
no_character_set_error = 'An error occurred. Try again with at least 1 character set.'
double_error = 'An error occurred. Try again with at least 1 character set and a whole number between 4 and 100.'

def show_copy_button(event) -> None:
    '''
    Called when the user releases a mouse button on a password label,
    this function displays a 'copy' menu on the x and y coordinates of the user's cursor,
    with the y coordinates adjusted by 30 pixels.

    Parameters
    ----------
    event:
        Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
    '''
    copy.tk_popup(event.x_root, event.y_root - 30)

def copy_text() -> None:
    '''
    Called upon pressing the copy button,
    this function simulates pressing CTRL and C to copy the selected text.
    '''
    keyboard.press(Key.ctrl_l)
    keyboard.press('c')
    keyboard.release(Key.ctrl_l)
    keyboard.release('c')

def show_generate_password_frame(frame, done_btn_image) -> None:
    '''
    Called upon starting the program,
    this function creates the password generation frame and its contents,
    and serves as a hub for all other password-generation functions.

    Parameters
    ----------
    frame: ttk.frame
        The "generate password" frame upon which the objects of this function will be placed.
    done_btn_image: ImageTk.PhotoImage
        The image used for the done button.
    '''

    global copy
    copy = tk.Menu(frame, tearoff = False)
    copy.add_command(label = 'Copy', command = copy_text)
    
    frame_title_text = 'Generate password'

    frame_title = tk.Label(frame, text = frame_title_text, font = title_font)
    frame_title.grid(column = 0, row = 1, columnspan = 2)

    question = tk.Label(frame, text = 'Number of characters (4 to 100):', font = description_font)
    question.grid(column = 0, row = 2, columnspan = 2)

    password_label_1 = tk.Text(frame, width = password_width, height = password_height,
                               borderwidth = password_border_width, font = password_font)
    password_label_2 = tk.Text(frame, width = password_width, height = password_height,
                               borderwidth = password_border_width, font = password_font)
    password_label_3 = tk.Text(frame, width = password_width, height = password_height,
                               borderwidth = password_border_width, font = password_font)
    password_label_4 = tk.Text(frame, width = password_width, height = password_height,
                               borderwidth = password_border_width, font = password_font)

    character_sets_label = tk.Label(frame, text = 'Character sets', font = section_title_font)
    character_sets_label.grid(column = 1, row = 4, columnspan = 2)

    lowercase_letters_var = tk.IntVar()
    lowercase_letters_checkbox = tk.Checkbutton(frame, variable = lowercase_letters_var, offvalue = 0, onvalue = 1)
    lowercase_letters_text = tk.Label(frame, text = 'Lowercase letters', font = description_font)

    uppercase_letters_var = tk.IntVar()
    uppercase_letters_checkbox = tk.Checkbutton(frame, variable = uppercase_letters_var, offvalue = 0, onvalue = 1)
    uppercase_letters_text = tk.Label(frame, text = 'Uppercase letters', font = description_font)

    digits_var = tk.IntVar()
    digits_checkbox = tk.Checkbutton(frame, variable = digits_var, offvalue = 0, onvalue = 1)
    digits_text = tk.Label(frame, text = 'Digits', font = description_font)

    punctuation_var = tk.IntVar()
    punctuation_checkbox = tk.Checkbutton(frame, variable = punctuation_var, offvalue = 0, onvalue = 1)
    punctuation_text = tk.Label(frame, text = 'Punctuation', font = description_font)

    password_labels = [password_label_1, password_label_2, password_label_3, password_label_4]
    checkboxes = [lowercase_letters_checkbox, uppercase_letters_checkbox, digits_checkbox, punctuation_checkbox]
    checkboxes_text = [lowercase_letters_text, uppercase_letters_text, digits_text, punctuation_text]

    for checkbox in checkboxes:
        checkbox.grid(column = 1, row = 5 + checkboxes.index(checkbox), pady = 8)
        checkbox.select()
    
    for text in checkboxes_text:
        text.grid(column = 2, row = 5 + checkboxes_text.index(text))

    def create_password_labels(event) -> None:
        '''
        Called upon clicking the done button or pressing the ENTER key,
        this function binds each password_label to the show_copy_button function when releasing a mouse button,
        calls the generate_password function to get the 4 passwords
        (or an error),
        and displays them:
        the 4 passwords on each password_label,
        or the error on the first password_label
        Parameters
        ----------
        event:
            Necessary for initiating the function when pressing the ENTER key.
        '''

        for password_label in password_labels:
            password_label.bind('<ButtonRelease>', show_copy_button)
            password = generate_password(input_box.get())
            if password != invalid_input_error and password != no_character_set_error and password != double_error:
                show_password(password_label, password, password_labels.index(password_label))
                password_label.grid(column = 0, row = 5 + password_labels.index(password_label), pady = 10, padx = 10)
        
        password_label_1.grid(column = 0, row = 5, padx = 10, pady = 10)
        show_password(password_label_1, password, 0)

    global input_box
    input_box = tk.Entry(frame, width = 10, borderwidth = 2)
    input_box.bind('<Return>', create_password_labels)
    input_box.grid(column = 0, row = 3, columnspan = 2)

    done_btn = tk.Button(frame, image = done_btn_image, borderwidth = 0, command = lambda: create_password_labels(None))
    done_btn.grid(column = 0, row = 4, columnspan = 2)

    def show_password(label, text, index) -> None:
        '''
        Called by the create_password_labels function,
        after password generation or attempted password generation,
        this function displays the passwords or an error.

        Parameters
        ----------
        label: tkinter.Text
            Each individual password label one by one if passwords are generated,
            or the first password label if an error is generated.
        text: str
            Each password or the error.
        index:
            The index of the password label being shown is necessary for placing it correctly on the screen.
        '''
        label.config(state = 'normal')
        label.delete('1.0', 'end')
        label.insert('1.0', text)
        label.grid(column = 0, row = 5 + index, pady = 10)
        label.config(state = 'disabled', bg = '#ffffff')

    def generate_password(requested_length) -> None:
        '''
        Called by the create_password_labels function
        (upon clicking the done button or pressing the ENTER key),
        this function checks if no character set has been chosen and if the input is valid,
        and returns a password or an error.

        Parameters
        ----------
        requested_length: int
            The length requested by the user.
        '''

        if lowercase_letters_var.get() == 0 and uppercase_letters_var.get() == 0 and digits_var.get() == 0 and punctuation_var.get() == 0:
            try:
                if 4 <= int(requested_length) <= 100:
                    return no_character_set_error
                else:
                    input_box.delete(0, 'end')
                    return double_error
            except:
                input_box.delete(0, 'end')
                return double_error

        try:
            if not 4 <= int(requested_length) <= 100:
                return invalid_input_error
        except:
            return invalid_input_error

        # Define all character sets that will be used in the password
        character_sets = []
        if lowercase_letters_var.get() == 1:
            character_sets.append(string.ascii_lowercase)
        if uppercase_letters_var.get() == 1:
            character_sets.append(string.ascii_uppercase)
        if digits_var.get() == 1:
            character_sets.append(string.digits)
        if punctuation_var.get() == 1:
            character_sets.append(string.punctuation)

        # Keep generating a new password until it includes at least one character from each chosen character set
        while True:
            password = ''.join(secrets.choice(''.join(character_sets)) for _ in range(int(requested_length)))
            if all(any(char in s for char in password) for s in character_sets):
                return password
