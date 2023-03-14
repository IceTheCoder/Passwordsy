"""
Called upon app startup,
this module prepares the GUI for password generation
"""
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from PIL import ImageTk, Image
import customtkinter

from password_generation import generate_password_logic as logic
from password_generation import other_methods_gui as other

invalid_input_error = 'An error occurred. Try again with a whole number between 4 and 100.'
no_character_set_error = 'An error occurred. Try again with at least 1 character set.'
double_error = 'An error occurred. Try again with at least 1 character set and a whole number between 4 and 100.'

global input_box
global copy_menu
global passwords
global show_hide_all_button

class PasswordGenerationFrame(customtkinter.CTkFrame):
    """
    Called upon starting the program,
    this class uses the Custom Tkinter module to create a GUI frame,
    used to generate passwords with various options for customisation
    (length and character sets),
    and serves as a hub for all other password generation functions.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        title_font = customtkinter.CTkFont(family='Roboto', size=36)
        section_title_font = customtkinter.CTkFont(family='Roboto', size=24)
        description_font = customtkinter.CTkFont(family='Roboto', size=18)

        global passwords
        passwords = []

        small_button_font = customtkinter.CTkFont(family='Roboto', size=16)
        medium_button_font = customtkinter.CTkFont(family='Roboto', size=24)
        large_button_font = customtkinter.CTkFont(family='Roboto', size=36)
        password_font = customtkinter.CTkFont(family='Consolas', size=14)

        password_width = 750
        password_height = 30
        password_border_width = 0

        self.password_label_1 = customtkinter.CTkTextbox(self, width=password_width, height=password_height,
                                                         border_width=password_border_width, font=password_font)
        self.password_label_2 = customtkinter.CTkTextbox(self, width=password_width, height=password_height,
                                                         border_width=password_border_width, font=password_font)
        self.password_label_3 = customtkinter.CTkTextbox(self, width=password_width, height=password_height,
                                                         border_width=password_border_width, font=password_font)
        self.password_label_4 = customtkinter.CTkTextbox(self, width=password_width, height=password_height,
                                                         border_width=password_border_width, font=password_font)
        self.password_labels = [self.password_label_1, self.password_label_2,
                                self.password_label_3, self.password_label_4]

        for password_label in self.password_labels:
            password_label.grid(column=0, row=4 + self.password_labels.index(password_label), pady=10, padx=10)

        for password_label in self.password_labels:
            password_label.grid_remove()

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
            show_text(self.password_labels[index], passwords[index])

            # Check if there is any content in all labels by checking the length (the length of an empty label is 1)
            if len(self.password_labels[0].get('1.0', 'end')) != 1 \
                    and len(self.password_labels[1].get('1.0', 'end')) != 1 \
                    and len(self.password_labels[2].get('1.0', 'end')) != 1 \
                    and len(self.password_labels[3].get('1.0', 'end')) != 1:
                self.show_hide_all_slider.set(1)

            button.configure(text='HIDE', command=lambda: hide_password(index, button))

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
            clear_text_label(self.password_labels[index])

            # Check if there is no content in no label by checking the length (the length of an empty label is 1)
            if len(self.password_labels[0].get('1.0', 'end')) == 1 \
                    and len(self.password_labels[1].get('1.0', 'end')) == 1 \
                    and len(self.password_labels[2].get('1.0', 'end')) == 1 \
                    and len(self.password_labels[3].get('1.0', 'end')) == 1:
                self.show_hide_all_slider.set(0)

            button.configure(text='SHOW', command=lambda: show_password(index, button))

        def run_function_based_on_slider_value(value) -> None:
            """
            Called when the user moves the slider,
            this function checks what function to run based on the slider's value:
            if it is 0, it runs hide_all_passwords(), if it is 1, it runs show_all_passwords.

            Parameters
            ----------
            value: float
                The slider's value
            """
            if value == 0:
                hide_all_passwords()
            elif value == 1:
                show_all_passwords()

        def show_all_passwords() -> None:
            """
            Called when the user clicks the 'show all' button,
            this function goes through each password_label,
            inserts the specific password inside of it through the show_text function,
            and changes the button into a hide all button.
            """
            for index, button in enumerate(self.show_hide_buttons):
                show_password(index, button)

        def hide_all_passwords() -> None:
            """
            Called when the user clicks the 'hide all' button,
            this function goes through each password_label,
            and clears it.
            """
            for index, button in enumerate(self.show_hide_buttons):
                hide_password(index, button)

        self.show_hide_button_1 = customtkinter.CTkButton(self, text='SHOW', border_width=2, fg_color='blue',
                                                          hover_color='gray', border_color='black',
                                                          font=small_button_font, width=75,
                                                          command=lambda: show_password(0, show_hide_button_1))
        self.show_hide_button_2 = customtkinter.CTkButton(self, text='SHOW', border_width=2, fg_color='blue',
                                                          hover_color='gray', border_color='black',
                                                          font=small_button_font, width=75,
                                                          command=lambda: show_password(0, show_hide_button_2))
        self.show_hide_button_3 = customtkinter.CTkButton(self, text='SHOW', border_width=2, fg_color='blue',
                                                          hover_color='gray', border_color='black',
                                                          font=small_button_font, width=75,
                                                          command=lambda: show_password(0, show_hide_button_3))
        self.show_hide_button_4 = customtkinter.CTkButton(self, text='SHOW', border_width=2, fg_color='blue',
                                                          hover_color='gray', border_color='black',
                                                          font=small_button_font, width=75,
                                                          command=lambda: show_password(0, show_hide_button_3))
        self.show_hide_buttons = [self.show_hide_button_1, self.show_hide_button_2,
                                  self.show_hide_button_3, self.show_hide_button_4]
        self.show_hide_all_slider = customtkinter.CTkSlider(master=self, from_=0, to=1,
                                                            command=run_function_based_on_slider_value,
                                                            width=50, height=25, number_of_steps=1, fg_color='#D3D3D3',
                                                            progress_color='#D3D3D3', button_color='blue')

        self.hide_label = customtkinter.CTkLabel(master=self, text='Hide',
                                                 font=customtkinter.CTkFont(family='Roboto', size=18))
        self.show_label = customtkinter.CTkLabel(master=self, text='Show', font=description_font)

        self.copy_button_1 = customtkinter.CTkButton(self, text='COPY', border_width=2, font=small_button_font,
                                                     width=75,
                                                     fg_color='blue', border_color='black', hover_color='gray',
                                                     command=lambda: logic.copy_password(0, passwords))
        self.copy_button_2 = customtkinter.CTkButton(self, text='COPY', border_width=2, font=small_button_font,
                                                     width=75,
                                                     fg_color='blue', border_color='black', hover_color='gray',
                                                     command=lambda: logic.copy_password(1, passwords))
        self.copy_button_3 = customtkinter.CTkButton(self, text='COPY', border_width=2, font=small_button_font,
                                                     width=75,
                                                     fg_color='blue', border_color='black', hover_color='gray',
                                                     command=lambda: logic.copy_password(2, passwords))
        self.copy_button_4 = customtkinter.CTkButton(self, text='COPY', border_width=2, font=small_button_font,
                                                     width=75,
                                                     fg_color='blue', border_color='black', hover_color='gray',
                                                     command=lambda: logic.copy_password(3, passwords))
        self.copy_buttons = [self.copy_button_1, self.copy_button_2,
                             self.copy_button_3, self.copy_button_4]

        self.frame_title = customtkinter.CTkLabel(master=self, text='Generate password', font=title_font)
        self.frame_title.grid(column=0, row=0, columnspan=4)

        self.question = customtkinter.CTkLabel(master=self, text='Number of characters (4 to 100):',
                                               font=description_font)
        self.question.grid(column=0, row=1, columnspan=4)

        self.character_sets_label = customtkinter.CTkLabel(master=self, text='Character sets', font=section_title_font)
        self.character_sets_label.grid(column=5, row=3, columnspan=2, sticky='s')

        self.lowercase_letters_var = tk.IntVar()
        self.lowercase_letters_checkbox = customtkinter.CTkCheckBox(master=self, variable=self.lowercase_letters_var,
                                                                    text='Lowercase letters', checkbox_width=20,
                                                                    checkbox_height=20, fg_color='gray',
                                                                    hover_color='white')

        self.uppercase_letters_var = tk.IntVar()
        self.uppercase_letters_checkbox = customtkinter.CTkCheckBox(master=self, variable=self.uppercase_letters_var,
                                                                    text='Uppercase letters', checkbox_width=20,
                                                                    checkbox_height=20, fg_color='gray',
                                                                    hover_color='white')

        self.digits_var = tk.IntVar()
        self.digits_checkbox = customtkinter.CTkCheckBox(master=self, variable=self.digits_var, text='Digits',
                                                         checkbox_width=20, checkbox_height=20, fg_color='gray',
                                                         hover_color='white')

        self.punctuation_var = tk.IntVar()
        self.punctuation_checkbox = customtkinter.CTkCheckBox(master=self, variable=self.punctuation_var,
                                                              text='Punctuation', checkbox_width=20, checkbox_height=20,
                                                              fg_color='gray', hover_color='white')

        self.checkboxes = [self.lowercase_letters_checkbox, self.uppercase_letters_checkbox,
                           self.digits_checkbox, self.punctuation_checkbox]

        self.other_methods_window = None

        self.try_other_methods_btn = customtkinter.CTkButton(self, text='Try other methods...',
                                                             border_width=2, border_color='black', fg_color='blue',
                                                             hover_color='gray', font=medium_button_font,
                                                             command=self.open_other_methods)
        self.try_other_methods_btn.grid(row=0, column=2, rowspan=3, columnspan=6)

        for checkbox in self.checkboxes:
            checkbox.grid(column=5, row=4 + self.checkboxes.index(checkbox), pady=8, sticky='w')
            checkbox.select()

        def show_copy_menu(event, password_labels=self.password_labels) -> None:
            """
            Called when the user releases a mouse button on a password label,
            this function uses the Tkinter module to display a contextual menu containing a 'copy' button
            for copying the password to the clipboard on the x and y coordinates of the user's cursor,
            where the y coordinates are adjusted by 30 pixels.

            Parameters
            ----------
            event: tkinter.event
                Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
            password_labels: list
                List of password labels
            """
            global copy_menu
            print('Hello, world!')
            copy_menu.tk_popup(event.x_root, event.y_root - 30)

            for label in password_labels:
                label.tag_bind('copy_tag', '<Button-3>', show_copy_menu)

            # Unbind the tag for all password labels except for the one that was clicked
            event.widget.tag_unbind('copy_tag', '<Button-3>')
            for label in password_labels:
                if label != event.widget:
                    label.tag_unbind('copy_tag', '<Button-3>')

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

            for label in self.password_labels:
                label.unbind('<Button-3>')
                label.bind('<Button-3>', show_copy_menu)

            message = logic.determine_error(
                logic.validate_character_sets(self.lowercase_letters_var, self.uppercase_letters_var,
                                              self.digits_var, self.punctuation_var),
                input_box.get(), no_character_set_error, double_error, invalid_input_error)

            # Check if an error was not returned
            if message == '':
                passwords = []
                for label in self.password_labels:
                    label.grid(column=0, row=4 + self.password_labels.index(label), pady=10, padx=10)
                    adapted_input = logic.adapt_input(input_box.get())
                    input_box.delete(0, 'end')
                    input_box.insert(1, str(adapted_input))

                    message = logic.generate_password(adapted_input, self.lowercase_letters_var,
                                                      self.uppercase_letters_var, self.digits_var, self.punctuation_var)
                    passwords.append(message)

                    show_text(label, '')
                    label.grid(column=0, row=4 + self.password_labels.index(label), pady=10, padx=10)
                for index, button in enumerate(self.show_hide_buttons):
                    button.grid(row=4 + index, column=1, columnspan=2, padx=15)
                for index, copy_button in enumerate(self.copy_buttons):
                    copy_button.grid(row=4 + index, column=3, columnspan=2, padx=15)
                self.show_hide_all_slider.grid(row=3, column=2, columnspan=2)
                self.hide_label.grid(row=3, column=1, sticky='e')
                self.show_label.grid(row=3, column=4, sticky='w')

            else:
                messagebox.showerror('Error', message)
                if message == invalid_input_error or message == double_error:
                    input_box.delete(0, 'end')

            hide_all_passwords()
            for button in self.show_hide_buttons:
                hide_password(self.show_hide_buttons.index(button), button)

        global input_box
        input_box = customtkinter.CTkEntry(self, width=50, corner_radius=8.5)
        input_box.bind('<Return>', lambda e: create_password_labels())
        input_box.grid(column=0, row=2, columnspan=4)

        self.done_btn = customtkinter.CTkButton(self, text='DONE', font=large_button_font, border_width=2,
                                                command=lambda: create_password_labels(),
                                                border_color='black', fg_color='blue', hover_color='gray')
        self.done_btn.grid(column=0, row=3, columnspan=4)

        global copy_menu
        copy_menu = tk.Menu(self, tearoff=False)
        copy_menu.add_command(label='Copy', command=lambda: logic.copy_selected_text(input_box, self.password_labels))

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
            label.configure(state='normal')
            label.delete('1.0', 'end')
            label.insert('1.0', message)
            label.configure(state='disabled')  # , bg='#ffffff')

    def open_other_methods(self):
        """
        Called when the user clicks on the 'try other methods' button,
        this function creates a Toplevel window containing other methods of password generation.
        """
        if self.other_methods_window is None or not self.other_methods_window.winfo_exists():
            self.other_methods_window = other.OtherMethodsWindow(self)
            self.after(100, self.other_methods_window.focus_set)
