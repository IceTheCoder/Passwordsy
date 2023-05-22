"""
Called upon app startup,
this module prepares the GUI for password generation
"""
import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from PIL import ImageTk, Image
import customtkinter
from tkinter import TclError

from password_generation import generate_password_logic as logic
from password_generation import other_methods_gui as other
import diacritics_fix as fix

invalid_input_error = 'An error occurred. Try again with a whole number between 4 and 100.'
no_character_set_error = 'An error occurred. Try again with at least 1 character set.'
double_error = 'An error occurred. Try again with at least 1 character set and a whole number between 4 and 100.'


class PasswordGenerationFrame(customtkinter.CTkFrame):
    """
    Called upon starting the program,
    this class uses the Custom Tkinter module to create a GUI frame,
    used to generate passwords with various options for customisation
    (length and character sets),
    and serves as a hub for all other password generation functions.
    """
    def __init__(self, master: customtkinter.CTkFrame, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.gui_font_name = 'Roboto'
        self.password_font_name = 'Consolas'
        self.show_button_text = 'SHOW'
        self.button_border_width = 2
        self.button_fg_color = 'blue'
        self.button_hover_color = 'gray'
        self.button_border_color = 'black'
        self.small_button_width = 60
        self.copy_button_text = 'COPY'
        self.title_columnspan = 5
        self.checkbox_size = 20
        self.checkbox_fg_color = 'grey'
        self.checkbox_hover_color = ('grey', 'white')
        self.password_width = 816
        self.password_height = 30
        self.password_border_width = 0

        self.title_font = customtkinter.CTkFont(family=self.gui_font_name, size=36)
        self.section_title_font = customtkinter.CTkFont(family=self.gui_font_name, size=24)
        self.description_font = customtkinter.CTkFont(family=self.gui_font_name, size=18)

        self.small_button_font = customtkinter.CTkFont(family=self.gui_font_name, size=16)
        self.medium_button_font = customtkinter.CTkFont(family=self.gui_font_name, size=24)
        self.large_button_font = customtkinter.CTkFont(family=self.gui_font_name, size=36)
        self.password_font = customtkinter.CTkFont(family=self.password_font_name, size=14)

        self.password_labels = []

        self.passwords = []

        def clear_text_label(textbox: customtkinter.CTkTextbox) -> None:
            """
            Called when the user clicks one of the hide buttons,
            this function deletes all content of the specific label.

            Returns: None

            Parameters
            ----------
            textbox: customtkinter.CTkTextbox
                The text label to be cleared.
            """
            textbox.configure(state='normal')
            textbox.delete('1.0', 'end')
            textbox.configure(state='disabled')

        def show_password(indicator: int, btn: customtkinter.CTkButton) -> None:
            """
            Called when the user clicks one of the 4 show buttons,
            this function displays the specific password through the show_text function,
            and changes the specific button to a hide button.

            Returns: None

            Parameters
            ----------
            indicator: int
                The number of the button that was clicked.
            btn: customtkinter.CTkButton
                The button that was clicked.
            """
            # https://stackoverflow.com/questions/68327/change-command-method-for-tkinter-button-in-python
            btn.configure(text='HIDE', command=lambda: hide_password(indicator, btn))

            if len(self.passwords) == 4:
                self.password_labels[indicator].unbind('<Button-3>')
                show_text(self.password_labels[indicator], self.passwords[indicator])

                # Check if there is any content in all labels by checking the length (the length of an empty label is 1)
                # If there is, change the slider accordingly
                if len(self.password_labels[0].get('1.0', 'end')) != 1 \
                        and len(self.password_labels[1].get('1.0', 'end')) != 1 \
                        and len(self.password_labels[2].get('1.0', 'end')) != 1 \
                        and len(self.password_labels[3].get('1.0', 'end')) != 1:
                    self.show_hide_all_slider.set(1)

                self.password_labels[indicator].bind('<Button-3>', show_copy_menu)

        def hide_password(indicator: int, btn: customtkinter.CTkButton) -> None:
            """
            Called when the user clicks one of the 4 hide buttons,
            this function clears the specific password_label through the clear_text_label function,
            and changes the specific button to a show_button.

            Returns: None

            Parameters
            ----------
            indicator: int
                The number of the button that was clicked.
            btn: CTKButton
                The button that was clicked.
            """
            btn.configure(text='SHOW', command=lambda: show_password(indicator, btn))

            if len(self.passwords) == 4:
                clear_text_label(self.password_labels[indicator])

                # Check if there is no content in no label by checking the length (the length of an empty label is 1)
                if len(self.password_labels[0].get('1.0', 'end')) == 1 \
                        and len(self.password_labels[1].get('1.0', 'end')) == 1 \
                        and len(self.password_labels[2].get('1.0', 'end')) == 1 \
                        and len(self.password_labels[3].get('1.0', 'end')) == 1:
                    self.show_hide_all_slider.set(0)

                self.password_labels[indicator].unbind('<Button-3>')

        def run_function_based_on_slider_value(value: float) -> None:
            """
            Called when the user moves the slider,
            this function checks what function to run based on the slider's value:
            if it is 0, it runs hide_all_passwords(), if it is 1, it runs show_all_passwords.

            Returns: None

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

            Returns: None
            """
            for indicator, btn in enumerate(self.show_hide_buttons):
                show_password(indicator, btn)

        def hide_all_passwords() -> None:
            """
            Called when the user clicks the 'hide all' button,
            this function goes through each password_label,
            and clears it.

            Returns: None
            """
            for indicator, btn in enumerate(self.show_hide_buttons):
                hide_password(indicator, btn)

        self.show_hide_button_1 = customtkinter.CTkButton(self,
                                                          text=self.show_button_text,
                                                          border_width=self.button_border_width,
                                                          fg_color=self.button_fg_color,
                                                          border_color=self.button_border_color,
                                                          hover_color=self.button_hover_color,
                                                          font=self.small_button_font,
                                                          width=self.small_button_width,
                                                          command=lambda: show_password(0, self.show_hide_button_1))

        self.show_hide_button_2 = customtkinter.CTkButton(self,
                                                          text=self.show_button_text,
                                                          border_width=self.button_border_width,
                                                          fg_color=self.button_fg_color,
                                                          border_color=self.button_border_color,
                                                          hover_color=self.button_hover_color,
                                                          font=self.small_button_font,
                                                          width=self.small_button_width,
                                                          command=lambda: show_password(0, self.show_hide_button_2))

        self.show_hide_button_3 = customtkinter.CTkButton(self,
                                                          text=self.show_button_text,
                                                          border_width=self.button_border_width,
                                                          fg_color=self.button_fg_color,
                                                          border_color=self.button_border_color,
                                                          hover_color=self.button_hover_color,
                                                          font=self.small_button_font,
                                                          width=self.small_button_width,
                                                          command=lambda: show_password(0, self.show_hide_button_3))

        self.show_hide_button_4 = customtkinter.CTkButton(self,
                                                          text=self.show_button_text,
                                                          border_width=self.button_border_width,
                                                          fg_color=self.button_fg_color,
                                                          border_color=self.button_border_color,
                                                          hover_color=self.button_hover_color,
                                                          font=self.small_button_font,
                                                          width=self.small_button_width,
                                                          command=lambda: show_password(0, self.show_hide_button_3))

        self.show_hide_buttons = [self.show_hide_button_1, self.show_hide_button_2,
                                  self.show_hide_button_3, self.show_hide_button_4]

        self.show_hide_all_slider = customtkinter.CTkSlider(master=self, command=run_function_based_on_slider_value,
                                                            width=63, height=25, number_of_steps=1, fg_color='#D3D3D3',
                                                            progress_color='#D3D3D3', button_color='blue')
        self.show_hide_all_slider.set(0)

        self.hide_label = customtkinter.CTkLabel(master=self, text='Hide', font=self.description_font)
        self.show_label = customtkinter.CTkLabel(master=self, text='Show', font=self.description_font)

        self.copy_button_1 = customtkinter.CTkButton(self,
                                                     text=self.copy_button_text,
                                                     border_width=self.button_border_width,
                                                     font=self.small_button_font,
                                                     width=self.small_button_width,
                                                     fg_color=self.button_fg_color,
                                                     border_color=self.button_border_color,
                                                     hover_color=self.button_hover_color,
                                                     command=lambda: logic.copy_password(0, self.passwords))

        self.copy_button_2 = customtkinter.CTkButton(self,
                                                     text=self.copy_button_text,
                                                     border_width=self.button_border_width,
                                                     font=self.small_button_font,
                                                     width=self.small_button_width,
                                                     fg_color=self.button_fg_color,
                                                     border_color=self.button_border_color,
                                                     hover_color=self.button_hover_color,
                                                     command=lambda: logic.copy_password(1, self.passwords))

        self.copy_button_3 = customtkinter.CTkButton(self,
                                                     text=self.copy_button_text,
                                                     border_width=self.button_border_width,
                                                     font=self.small_button_font,
                                                     width=self.small_button_width,
                                                     fg_color=self.button_fg_color,
                                                     border_color=self.button_border_color,
                                                     hover_color=self.button_hover_color,
                                                     command=lambda: logic.copy_password(2, self.passwords))

        self.copy_button_4 = customtkinter.CTkButton(self,
                                                     text=self.copy_button_text,
                                                     border_width=self.button_border_width,
                                                     font=self.small_button_font,
                                                     width=self.small_button_width,
                                                     fg_color=self.button_fg_color,
                                                     border_color=self.button_border_color,
                                                     hover_color=self.button_hover_color,
                                                     command=lambda: logic.copy_password(3, self.passwords))

        self.copy_buttons = [self.copy_button_1, self.copy_button_2,
                             self.copy_button_3, self.copy_button_4]

        self.frame_title = customtkinter.CTkLabel(master=self, text='Generate password', font=self.title_font)
        self.frame_title.grid(column=0, row=0, columnspan=self.title_columnspan)

        self.question = customtkinter.CTkLabel(master=self, text='Number of characters (4 to 100):',
                                               font=self.description_font)
        self.question.grid(column=0, row=1, columnspan=self.title_columnspan)

        self.character_sets_label = customtkinter.CTkLabel(master=self, text='Character sets',
                                                           font=self.section_title_font)
        self.character_sets_label.grid(column=5, row=3, columnspan=2, sticky='s')

        self.lowercase_letters_var = tk.IntVar()
        self.lowercase_letters_checkbox = customtkinter.CTkCheckBox(master=self,
                                                                    variable=self.lowercase_letters_var,
                                                                    text='Lowercase letters',
                                                                    checkbox_width=self.checkbox_size,
                                                                    checkbox_height=self.checkbox_size,
                                                                    fg_color=self.checkbox_fg_color,
                                                                    hover_color=self.checkbox_hover_color)

        self.uppercase_letters_var = tk.IntVar()
        self.uppercase_letters_checkbox = customtkinter.CTkCheckBox(master=self,
                                                                    variable=self.uppercase_letters_var,
                                                                    text='Uppercase letters',
                                                                    checkbox_width=self.checkbox_size,
                                                                    checkbox_height=self.checkbox_size,
                                                                    fg_color=self.checkbox_fg_color,
                                                                    hover_color=self.checkbox_hover_color)

        self.digits_var = tk.IntVar()
        self.digits_checkbox = customtkinter.CTkCheckBox(master=self,
                                                         variable=self.digits_var,
                                                         text='Digits',
                                                         checkbox_width=self.checkbox_size,
                                                         checkbox_height=self.checkbox_size,
                                                         fg_color=self.checkbox_fg_color,
                                                         hover_color=self.checkbox_hover_color)

        self.punctuation_var = tk.IntVar()
        self.punctuation_checkbox = customtkinter.CTkCheckBox(master=self,
                                                              variable=self.punctuation_var,
                                                              text='Punctuation',
                                                              checkbox_width=self.checkbox_size,
                                                              checkbox_height=self.checkbox_size,
                                                              fg_color=self.checkbox_fg_color,
                                                              hover_color=self.checkbox_hover_color)

        self.checkboxes = [self.lowercase_letters_checkbox, self.uppercase_letters_checkbox,
                           self.digits_checkbox, self.punctuation_checkbox]

        self.other_methods_window = None

        self.try_other_methods_btn = customtkinter.CTkButton(self, text='Try other methods...',
                                                             border_width=2, border_color='black', fg_color='blue',
                                                             hover_color='gray', font=self.medium_button_font,
                                                             command=self.open_other_methods)
        self.try_other_methods_btn.grid(row=0, column=2, rowspan=3, columnspan=6)

        self.password_label_1 = customtkinter.CTkTextbox(self,
                                                         width=self.password_width,
                                                         height=self.password_height,
                                                         border_width=self.password_border_width,
                                                         font=self.password_font)
        self.password_label_2 = customtkinter.CTkTextbox(self,
                                                         width=self.password_width,
                                                         height=self.password_height,
                                                         border_width=self.password_border_width,
                                                         font=self.password_font)
        self.password_label_3 = customtkinter.CTkTextbox(self,
                                                         width=self.password_width,
                                                         height=self.password_height,
                                                         border_width=self.password_border_width,
                                                         font=self.password_font)
        self.password_label_4 = customtkinter.CTkTextbox(self,
                                                         width=self.password_width,
                                                         height=self.password_height,
                                                         border_width=self.password_border_width,
                                                         font=self.password_font)

        self.password_labels = [self.password_label_1, self.password_label_2,
                                self.password_label_3, self.password_label_4]

        self.show_hide_all_slider.grid(row=3, column=2, columnspan=2)
        self.hide_label.grid(row=3, column=1, padx=5)
        self.show_label.grid(row=3, column=4, padx=5)

        for label in self.password_labels:
            label.grid(column=0, row=4 + self.password_labels.index(label), pady=10, padx=10)

        for index, button in enumerate(self.show_hide_buttons):
            button.grid(row=4 + index, column=1, columnspan=2, padx=15)
        for index, copy_button in enumerate(self.copy_buttons):
            copy_button.grid(row=4 + index, column=3, columnspan=2, padx=15)

        for checkbox in self.checkboxes:
            checkbox.grid(column=5, row=4 + self.checkboxes.index(checkbox), pady=0, sticky='w')
            checkbox.select()

        def show_copy_menu(event: tkinter.Event) -> None:
            """
            Called when the user releases a mouse button on a password label,
            this function uses the Tkinter module to display a contextual menu containing a 'copy' button
            for copying the password to the clipboard on the x and y coordinates of the user's cursor,
            where the y coordinates are adjusted by 30 pixels.

            Returns: None

            Parameters
            ----------
            event: tkinter.Event
                Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
            """
            # https://stackoverflow.com/questions/69425865/tkinter-event-x-y-mouse-position-wrong-value-only-when-mouse-movement-up
            self.copy_menu.tk_popup(event.x_root, event.y_root - 30)  # https://youtu.be/Z4zePg2M5H8

            for pass_label in self.password_labels:
                pass_label.tag_bind('copy_tag', '<Button-3>', show_copy_menu)

            # Unbind the tag for all password labels except for the one that was clicked to prevent multiple instances
            # of the copy menu.
            event.widget.tag_unbind('copy_tag', '<Button-3>')
            for pass_label in self.password_labels:
                if pass_label != event.widget:
                    pass_label.tag_unbind('copy_tag', '<Button-3>')

        def create_password_labels(event) -> None:
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

            Returns: None

            Parameters
            ----------
            event: tk.Event
                Necessary for running the function when the user presses the RETURN key.
            """
            message = logic.determine_error(
                logic.validate_character_sets(self.lowercase_letters_var, self.uppercase_letters_var,
                                              self.digits_var, self.punctuation_var),
                self.input_box.get(), no_character_set_error, double_error, invalid_input_error)

            for p_label in self.password_labels:
                p_label.grid(column=0, row=4 + self.password_labels.index(p_label), pady=10, padx=10)

            # Check if an error was not returned
            if message == '':
                self.password_label_1 = customtkinter.CTkTextbox(self,
                                                                 width=self.password_width,
                                                                 height=self.password_height,
                                                                 border_width=self.password_border_width,
                                                                 font=self.password_font)
                self.password_label_2 = customtkinter.CTkTextbox(self,
                                                                 width=self.password_width,
                                                                 height=self.password_height,
                                                                 border_width=self.password_border_width,
                                                                 font=self.password_font)
                self.password_label_3 = customtkinter.CTkTextbox(self,
                                                                 width=self.password_width,
                                                                 height=self.password_height,
                                                                 border_width=self.password_border_width,
                                                                 font=self.password_font)
                self.password_label_4 = customtkinter.CTkTextbox(self,
                                                                 width=self.password_width,
                                                                 height=self.password_height,
                                                                 border_width=self.password_border_width,
                                                                 font=self.password_font)
                for p_label in self.password_labels:
                    p_label.destroy()

                self.password_labels = [self.password_label_1, self.password_label_2,
                                        self.password_label_3, self.password_label_4]

                self.passwords = []
                for p_label in self.password_labels:
                    adapted_input = logic.adapt_input(self.input_box.get())
                    self.input_box.delete(0, 'end')
                    self.input_box.insert(1, str(adapted_input))

                    message = logic.generate_password(adapted_input, self.lowercase_letters_var,
                                                      self.uppercase_letters_var, self.digits_var, self.punctuation_var)
                    self.passwords.append(message)

                    show_text(p_label, '')
                    p_label.grid(column=0, row=4 + self.password_labels.index(p_label), pady=10, padx=10)
                for i, show_hide_button in enumerate(self.show_hide_buttons):
                    show_hide_button.grid(row=4 + i, column=1, columnspan=2, padx=15)
                for i, btn in enumerate(self.copy_buttons):
                    btn.grid(row=4 + i, column=3, columnspan=2, padx=15)
                hide_all_passwords()
            else:
                error_title = ''
                if message == invalid_input_error:
                    error_title = 'Invalid input'
                elif message == no_character_set_error:
                    error_title = 'No character set'
                elif message == double_error:
                    error_title = 'Invalid input and no character set'
                # https://youtu.be/S3AaSwpb5GE
                messagebox.showerror(error_title, message)
                if message == invalid_input_error or message == double_error:
                    # https://stackoverflow.com/questions/2260235/how-to-clear-the-entry-widget-after-a-button-is-pressed-in-tkinter
                    self.input_box.delete(0, 'end')

        self.input_box = customtkinter.CTkEntry(self, width=50, corner_radius=8)
        self.input_box.bind('<Return>', create_password_labels)  # https://www.youtube.com/watch?v=GLnNPjL1U2g
        self.input_box.bind('<KeyPress>', fix.on_key_press)
        # https://stackoverflow.com/questions/75846986/certain-characters-like-%c8%9b-and-%c8%99-become-question-marks-as-i-type-them-in-a-tkin/76015278#76015278

        self.input_box.grid(column=0, row=2, columnspan=self.title_columnspan)

        self.done_btn = customtkinter.CTkButton(self,
                                                text='DONE',
                                                font=self.large_button_font,
                                                border_width=self.button_border_width,
                                                command=lambda: create_password_labels(None),
                                                border_color=self.button_border_color,
                                                fg_color=self.button_fg_color,
                                                hover_color=self.button_hover_color)
        self.done_btn.grid(column=0, row=3, columnspan=self.title_columnspan)

        # https://youtu.be/KRuUtNxOb_k
        self.copy_menu = tk.Menu(self, tearoff=False)
        self.copy_menu.add_command(label='Copy', command=lambda: logic.copy_selected_text(self.input_box,
                                                                                          self.password_labels))

        def show_text(textbox: customtkinter.CTkTextbox, message: str) -> None:
            """
            Called by the create_password_labels function,
            this function updates the contents of the password_labels,
            by enabling the label, deleting its current contents,
            inserting the new text, and then disabling the label again.

            Returns: None

            Parameters
            ----------
            textbox: customtkinter.CTkTextbox
                Each password label one by one if passwords are generated,
                or the first password label if an error is generated.
            message: str
                Each password or the error.
            """
            textbox.configure(state='normal')
            textbox.delete('1.0', 'end')
            textbox.insert('1.0', message)
            # https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only
            textbox.configure(state='disabled')

    def open_other_methods(self) -> None:
        """
        Called when the user clicks on the 'try other methods' button,
        this function creates a Toplevel window containing other methods of password generation.

        Returns: None
        """
        if self.other_methods_window is None or not self.other_methods_window.winfo_exists():
            self.other_methods_window = other.OtherMethodsWindow(self)
        else:
            self.other_methods_window.focus()
