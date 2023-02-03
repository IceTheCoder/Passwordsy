import secrets as secrets
import string as string
import tkinter as tk

title_font = 'Helvetica 24'
description_font = 'Helvetica 12'

characters = string.ascii_letters + string.punctuation + string.digits

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
    frame_title_text = 'Generate password'

    frame_title = tk.Label(frame, text = frame_title_text, font = title_font)
    frame_title.place(relx = 0.5, rely = 0.0, anchor = 'n')

    tip = tk.Label(frame, text = 'CTRL + C to copy', font = description_font)
    tip.place(relx = 0.5, rely = 0.1, anchor = 'n')

    question = tk.Label(frame, text = 'Number of characters (up to 100):', font = description_font)
    question.place(relx = 0.5, rely = 0.16, anchor = 'n')

    def show_copy_menu(event):
        global copy
        copy = tk.Label(frame, text = 'Copy', font = description_font)
        copy.place(relx = 0.5, rely = 0.85)

    def hide_copy_menu(event):
        try:
            copy.place_forget()
        except:
            pass


    def create_password_labels(event) -> None:
        '''
        Called upon clicking the done button or pressing the ENTER key,
        this function creates the password(s) or error label(s),
        and calls the show_password() function to show the passwords or the error.

        Parameters
        ----------
        event:
            Necessary for initiating the function when pressing the ENTER key

        Raises
        ------
        ValueError
            If an invalid value is placed in the input box.
        '''

        try:
            copy.place_forget()
        except:
            pass

        password_width = 100
        password_height = 1
        password_border_width = 0
        password_font = 'Consolas 11'

        error = 'An error occured. Try again with a whole number greater than 0.'

        password_label_1 = tk.Text(frame, width = password_width, height = password_height,
                                   borderwidth = password_border_width, font = password_font)
        password_label_2 = tk.Text(frame, width = password_width, height = password_height,
                                   borderwidth = password_border_width, font = password_font)
        password_label_3 = tk.Text(frame, width = password_width, height = password_height,
                                   borderwidth = password_border_width, font = password_font)
        password_label_4 = tk.Text(frame, width = password_width, height = password_height,
                                   borderwidth = password_border_width, font = password_font)

        password_labels = [password_label_1, password_label_2, password_label_3, password_label_4]

        try:
            for password_label in password_labels:
                password_label.bind('<ButtonRelease>', show_copy_menu)
                password_label.bind('<Button>', hide_copy_menu)
                requested_length = int(input_box.get())
                password = generate_password(requested_length)
                show_password(password_label, password, password_labels.index(password_label))
        except ValueError:
            input_box.delete(0, 'end')
            show_password(password_label_1, error, 0)

    global input_box
    input_box = tk.Entry(frame, width = 10, borderwidth = 2)
    input_box.bind('<Return>', create_password_labels)
    input_box.place(relx = 0.5, rely = 0.2325, anchor = 'n')

    done_btn = tk.Button(frame, image = done_btn_image, borderwidth = 0, command = lambda: create_password_labels(None))
    done_btn.place(relx = 0.5, rely = 0.31, anchor = 'n')

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

        label.insert(1.0, text)
        label.place(relx = 0.5, rely = 0.485 + (index / 10), anchor = 'n')
        label.configure(state = 'disabled')  # Makes the text uneditable.

    def generate_password(requested_length) -> str:
        '''
        Called by the create_password_labels function,
        (upon clicking the done button or the ENTER key),
        this function checks if the requested_length is valid,
        returns a password if it is,
        raises a value error if it's not.

        Parameters
        ----------
        requested_length: int
            The length requested by the user.
        
        Raises
        ------
        ValueError
            If the requested length is not an integer greater than 0.
        '''

        if requested_length > 0:
            return ''.join(secrets.choice(characters) for _ in range(min(int(requested_length), 100))) # This is where the password itself is generated
        else:
            raise ValueError
