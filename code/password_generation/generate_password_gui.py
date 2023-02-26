import tkinter as tk

from password_generation import generate_password_logic as logic
from password_generation import other_methods_gui as other
from tkinter import messagebox

title_font = 'Helvetica 24'
section_title_font = 'Helvetica 16'
description_font = 'Helvetica 12'

password_width = 100
password_height = 1
password_border_width = 0
password_font = 'Consolas 11'

invalid_input_error = 'An error occurred. Try again with a whole number between 4 and 100.'
no_character_set_error = 'An error occurred. Try again with at least 1 character set.'
double_error = 'An error occurred. Try again with at least 1 character set and a whole number between 4 and 100.'

global input_box
global copy_menu
global passwords
global show_hide_all_button
passwords = []


def create_generate_password_frame(frame, done_btn_image) -> None:
    """
    Called upon starting the program,
    this function uses the Tkinter module to create a GUI frame
    to generate passwords with various options for customisation
    (length and character sets),
    and serves as a hub for all other password generation functions.

    Parameters
    ----------
    frame: ttk.frame
        The "generate password" frame upon which the objects of this function will be placed.
    done_btn_image: ImageTk.PhotoImage
        The image used for the done button.
    """
    password_label_1 = tk.Text(frame, width=password_width, height=password_height,
                               borderwidth=password_border_width, font=password_font)
    password_label_2 = tk.Text(frame, width=password_width, height=password_height,
                               borderwidth=password_border_width, font=password_font)
    password_label_3 = tk.Text(frame, width=password_width, height=password_height,
                               borderwidth=password_border_width, font=password_font)
    password_label_4 = tk.Text(frame, width=password_width, height=password_height,
                               borderwidth=password_border_width, font=password_font)
    password_labels = [password_label_1, password_label_2, password_label_3, password_label_4]

    def clear_text_label(label):
        """
        Called when the user clicks one of the hide buttons,
        this function deletes all content of the specific label.

        Parameters
        ----------
        label: tk.Text
            The text label to be cleared.
        """
        label.configure(state='normal')
        label.delete('1.0', 'end')
        label.configure(state='disabled')

    def show_password(index, button) -> None:
        """
        Called when the user clicks one of the 4 show buttons,
        this function displays the specific password through the show_text function,
        and changes the specific button to a hide button.

        Parameters
        ----------
        index: int
            The number of the button that was clicked.
        button: tk.Button
            The button that was clicked.
        """
        global passwords
        show_text(password_labels[index], passwords[index])

        button.configure(text='Hide', command=lambda: hide_password(index, button))

    def hide_password(index, button) -> None:
        """
        Called when the user clicks one of the 4 hide buttons,
        this function clears the specific password_label through the clear_text_label function,
        and changes the specific button to a show_button.

        Parameters
        ----------
        index: int
            The number of the button that was clicked.
        button: tk.Button
            The button that was clicked.
        """
        clear_text_label(password_labels[index])
        button.configure(text='Show', command=lambda: show_password(index, button))

    def show_all_passwords():
        """
        Called when the user clicks the 'show all' button,
        this function goes through each password_label,
        inserts the specific password inside of it through the show_text function,
        and changes the button into a hide all button.
        """
        global show_hide_all_button
        for index, label in enumerate(password_labels):
            show_text(label, passwords[index])
        show_hide_all_button.configure(text='Hide all', command=hide_all_passwords)

    def hide_all_passwords():
        """
        Called when the user clicks the 'hide all' button,
        this function goes through each password_label,
        and clears it.
        """
        global show_hide_all_button
        for label in password_labels:
            clear_text_label(label)
        show_hide_all_button.configure(text='Show all', command=show_all_passwords)

    global show_hide_all_button
    show_hide_button_1 = tk.Button(frame, text='Show', command=lambda: show_password(0, show_hide_button_1))
    show_hide_button_2 = tk.Button(frame, text='Show', command=lambda: show_password(1, show_hide_button_2))
    show_hide_button_3 = tk.Button(frame, text='Show', command=lambda: show_password(2, show_hide_button_3))
    show_hide_button_4 = tk.Button(frame, text='Show', command=lambda: show_password(3, show_hide_button_4))
    show_hide_buttons = [show_hide_button_1, show_hide_button_2, show_hide_button_3, show_hide_button_4]
    show_hide_all_button = tk.Button(frame, text='Show all', command=show_all_passwords)

    copy_button_1 = tk.Button(frame, text='Copy', command=lambda: logic.copy_password(0, passwords))
    copy_button_2 = tk.Button(frame, text='Copy', command=lambda: logic.copy_password(1, passwords))
    copy_button_3 = tk.Button(frame, text='Copy', command=lambda: logic.copy_password(2, passwords))
    copy_button_4 = tk.Button(frame, text='Copy', command=lambda: logic.copy_password(3, passwords))
    copy_buttons = [copy_button_1, copy_button_2, copy_button_3, copy_button_4]

    frame_title = tk.Label(frame, text='Generate password', font=title_font)
    frame_title.grid(column=0, row=0, columnspan=3)

    question = tk.Label(frame, text='Number of characters (4 to 100):', font=description_font)
    question.grid(column=0, row=1, columnspan=3)

    character_sets_label = tk.Label(frame, text='Character sets', font=section_title_font)
    character_sets_label.grid(column=3, row=3, columnspan=2, sticky='s')

    lowercase_letters_var = tk.IntVar()
    lowercase_letters_checkbox = tk.Checkbutton(frame, variable=lowercase_letters_var, offvalue=0, onvalue=1)
    lowercase_letters_text = tk.Label(frame, text='Lowercase letters', font=description_font)

    uppercase_letters_var = tk.IntVar()
    uppercase_letters_checkbox = tk.Checkbutton(frame, variable=uppercase_letters_var, offvalue=0, onvalue=1)
    uppercase_letters_text = tk.Label(frame, text='Uppercase letters', font=description_font)

    digits_var = tk.IntVar()
    digits_checkbox = tk.Checkbutton(frame, variable=digits_var, offvalue=0, onvalue=1)
    digits_text = tk.Label(frame, text='Digits', font=description_font)

    punctuation_var = tk.IntVar()
    punctuation_checkbox = tk.Checkbutton(frame, variable=punctuation_var, offvalue=0, onvalue=1)
    punctuation_text = tk.Label(frame, text='Punctuation', font=description_font)

    checkboxes = [lowercase_letters_checkbox, uppercase_letters_checkbox, digits_checkbox, punctuation_checkbox]
    checkboxes_text_labels = [lowercase_letters_text, uppercase_letters_text, digits_text, punctuation_text]

    try_other_methods_button = tk.Button(frame, text='Try other methods...', command=other.create_other_methods_window)
    try_other_methods_button.grid(row=0, column=3, rowspan=3, columnspan=4)

    for checkbox in checkboxes:
        checkbox.grid(column=3, row=4 + checkboxes.index(checkbox), pady=8)
        checkbox.select()

    for text_label in checkboxes_text_labels:
        text_label.grid(column=4, row=4 + checkboxes_text_labels.index(text_label), sticky='w')

    def create_password_labels() -> None:
        """
        Called upon clicking the done button or pressing the ENTER key,
        this function calls determine_error and validate_character_sets of generate_password_logic,
        and then settles whether an error has occurred or not.
        If an error has occurred, the function displays said error
        (obtained through determine_error),
        and displays it on the screen through show_text.
        If an error has not occurred,
        the function calls generate_password of generate_password_logic.py to get 4 passwords,
        and calls the show_text function to display them to the user.
        """
        global passwords

        for password_label in password_labels:
            password_label.bind('<Button-3>', lambda e: logic.show_copy_button(e, copy_menu))

        message = logic.determine_error(
            logic.validate_character_sets(lowercase_letters_var, uppercase_letters_var, digits_var, punctuation_var),
            input_box.get(), no_character_set_error, double_error, invalid_input_error)

        # Check if an error was not returned
        if message == '':
            passwords = []
            for password_label in password_labels:
                password_label.grid(column=0, row=4 + password_labels.index(password_label), pady=10, padx=10)
                adapted_input = logic.adapt_input(input_box.get())
                input_box.delete(0, 'end')
                input_box.insert(1, str(adapted_input))

                message = logic.generate_password(adapted_input, lowercase_letters_var, uppercase_letters_var,
                                                  digits_var, punctuation_var)
                passwords.append(message)

                show_text(password_label, '')
                password_label.grid(column=0, row=4 + password_labels.index(password_label), pady=10, padx=10)
            for index, show_button in enumerate(show_hide_buttons):
                show_button.grid(row=4 + index, column=1, padx=15)
            for index, copy_button in enumerate(copy_buttons):
                copy_button.grid(row=4 + index, column=2, padx=15)
            show_hide_all_button.grid(row=3, column=1, sticky='s', columnspan=2)
        else:
            tk.messagebox.showerror('Error', message)
            if message == invalid_input_error or message == double_error:
                input_box.delete(0, 'end')

        hide_all_passwords()
        for button in show_hide_buttons:
            hide_password(show_hide_buttons.index(button), button)

    global input_box
    input_box = tk.Entry(frame, width=10, borderwidth=2)
    input_box.bind('<Return>', lambda e: create_password_labels())
    input_box.grid(column=0, row=2, columnspan=3)

    done_btn = tk.Button(frame, image=done_btn_image, borderwidth=0, command=lambda: create_password_labels())
    done_btn.grid(column=0, row=3, columnspan=3)

    global copy_menu
    copy_menu = tk.Menu(frame, tearoff=False)
    copy_menu.add_command(label='Copy', command=lambda: logic.copy_selected_text(input_box, password_labels))

    def show_text(label, message) -> None:
        """
        Called by the create_password_labels function,
        this function updates the contents of the password_labels,
        by enabling the label, deleting its current contents,
        inserting the new text, and then disabling the label again.

        Parameters
        ----------
        label: tkinter.Text
            Each password label one by one if passwords are generated,
            or the first password label if an error is generated.
        message: str
            Each password or the error.
        """
        label.config(state='normal')
        label.delete('1.0', 'end')
        label.insert('1.0', message)
        label.config(state='disabled', bg='#ffffff')


def select_input_box() -> None:
    """
    Called whenever the tab is changed,
    this function focuses the keyboard to the input box,
    which allows the user to start typing immediately without having to click on the input box first.
    """
    input_box.focus()
