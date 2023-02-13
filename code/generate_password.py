import secrets
import string
import tkinter as tk
from pynput.keyboard import Key, Controller

title_font = 'Helvetica 24'
section_font = 'Helvetica 16'
description_font = 'Helvetica 12'

keyboard = Controller()

characters = string.ascii_letters + string.punctuation + string.digits

password_width = 100
password_height = 1
password_border_width = 0
password_font = 'Consolas 11'

error = 'An error occurred. Try again with a whole number between 6 and 100.'

def show_copy_button(event) -> None:
    '''
    Called when the user releases a mouse button on a password label,
    this function displays a 'copy' button slightly above the mouse cursor,
    and places it on top of all other widgets.

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

    question = tk.Label(frame, text = 'Number of characters (6 to 100):', font = description_font)
    question.grid(column = 0, row = 2, columnspan = 2)

    password_label_1 = tk.Text(frame, width = password_width, height = password_height,
                               borderwidth = password_border_width, font = password_font)
    password_label_2 = tk.Text(frame, width = password_width, height = password_height,
                               borderwidth = password_border_width, font = password_font)
    password_label_3 = tk.Text(frame, width = password_width, height = password_height,
                               borderwidth = password_border_width, font = password_font)
    password_label_4 = tk.Text(frame, width = password_width, height = password_height,
                               borderwidth = password_border_width, font = password_font)

    character_sets_label = tk.Label(frame, text = 'Character sets', font = section_font)
    character_sets_label.grid(column = 1, row = 4, columnspan = 2)

    lowercase_letters_checkbox = tk.Checkbutton(frame)
    lowercase_letters_checkbox.grid(column = 1, row = 5)
    lowercase_letters_text = tk.Label(frame, text = 'Lowercase letters', font = description_font)
    lowercase_letters_text.grid(column = 2, row = 5, sticky = 'w')

    uppercase_letters_checkbox = tk.Checkbutton(frame)
    uppercase_letters_checkbox.grid(column = 1, row = 6)
    uppercase_letters_text = tk.Label(frame, text = 'Uppercase letters', font = description_font)
    uppercase_letters_text.grid(column = 2, row = 6, sticky = 'w')

    digits_checkbox = tk.Checkbutton(frame)
    digits_checkbox.grid(column = 1, row = 7)
    digits_text = tk.Label(frame, text = 'Digits', font = description_font)
    digits_text.grid(column = 2, row = 7, sticky = 'w')

    punctuation_checkbox = tk.Checkbutton(frame)
    punctuation_checkbox.grid(column = 1, row = 8)
    punctuation_text = tk.Label(frame, text = 'Punctuation', font = description_font)
    punctuation_text.grid(column = 2, row = 8, sticky = 'w')

    password_labels = [password_label_1, password_label_2, password_label_3, password_label_4]

    checkboxes = [lowercase_letters_checkbox, uppercase_letters_checkbox, digits_checkbox, punctuation_checkbox]

    for password_label in password_labels:
        password_label.grid(column = 0, row = 5 + password_labels.index(password_label), pady = 10, padx = 10)
        password_label.config(state = 'disabled')

    for checkbox in checkboxes:
        checkbox.select()

    def create_password_labels(event) -> None:
        '''
        Called upon clicking the done button or pressing the ENTER key,
        this function places the password_labels in a list,
        binds them to the show_copy_button function when releasing a mouse mutton,
        calls the generate_password function to get the passwords and calls the show_password function to display them,
        or clears the input_box and calls the show_password function to show an error if the input is invalid.
        Parameters
        ----------
        event:
            Necessary for initiating the function when pressing the ENTER key.

        Raises
        ------
        ValueError
            If an invalid value is placed in the input box.
        '''

        try:
            for password_label in password_labels:
                password_label.bind('<ButtonRelease>', show_copy_button)

                generate_password(int(input_box.get()))

                global password
                password_to_be_shown = password

                show_password(password_label, password_to_be_shown, password_labels.index(password_label))

        except ValueError:
            input_box.delete(0, 'end')
            show_password(password_label_1, error, 0)

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
            The password or the error.
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
        this function checks if the requested_length is valid,
        creates a global variable with a secure password if it is,
        raises a value error if it's not.

        Parameters
        ----------
        requested_length: int
            The length requested by the user.
        
        Raises
        ------
        ValueError
            If the requested length is not an integer between 6 and 100.
        '''
        try:
            if 6 <= requested_length <= 100:
                generated_password = ''.join(secrets.choice(characters) for _ in range(max(min(int(requested_length), 100), max(int(requested_length), 6))))

                lowercase_letters = []
                lowercase_letters[:0] = string.ascii_lowercase

                uppercase_letters = []
                uppercase_letters[:0] = string.ascii_uppercase

                digits = []
                digits[:0] = string.digits

                punctuation = []
                punctuation[:0] = string.punctuation

                generate_password_characters = []
                generate_password_characters[:0] = generated_password

                number_of_lowercase_letters = 0
                number_of_uppercase_letters = 0
                number_of_digits = 0
                number_of_punctuation = 0

                for character in generate_password_characters:
                    if character in lowercase_letters:
                        number_of_lowercase_letters += 1

                    if character in uppercase_letters:
                        number_of_uppercase_letters += 1

                    if character in digits:
                        number_of_digits += 1

                    if character in punctuation:
                        number_of_punctuation += 1

                if number_of_lowercase_letters == 0 or number_of_uppercase_letters == 0 or number_of_digits == 0 or number_of_punctuation == 0:
                    generate_password(requested_length)
                else:
                    global password
                    password = generated_password
            else:
                raise ValueError
        except:
            raise ValueError
