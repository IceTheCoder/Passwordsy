import tkinter as tk
import logic
from tkinter import ttk as ttk

def main():
    window = tk.Tk()
    notebook = ttk.Notebook(window)
    notebook.grid(column = 0, row = 0)

    window_width = 854
    window_height = 350
    resizable_ability = False
    app_name = 'Passwordsy'
    title_font = 'Helvetica 24'
    description_font = 'Helvetica 12'

    generate_password_frame = ttk.Frame(notebook, width = 854, height = 350)
    password_strength_frame = ttk.Frame(notebook, width = 854, height = 350)

    generate_password_frame.grid(column = 0, row = 1)
    password_strength_frame.grid(column = 0, row = 0)

    notebook.add(generate_password_frame, text = 'Generate a password')
    notebook.add(password_strength_frame, text = 'Check a password\'s strength')

    title = tk.Label(generate_password_frame, text=app_name, font = title_font)
    title.place(relx = 0.5, rely = 0.0, anchor = 'n')

    tip = tk.Label(generate_password_frame, text='CTRL + C to copy', font=description_font)
    tip.place(relx = 0.5, rely = 0.1, anchor = 'n')

    question = tk.Label(generate_password_frame, text='Number of characters (up to 100):', font=description_font)
    question.place(relx = 0.5, rely = 0.15, anchor = 'n')


    window.minsize(window_width, window_height)
    window.maxsize(window_width, window_height)
    window.grid_columnconfigure(0, weight=1)
    window.resizable(resizable_ability, resizable_ability)
    window.iconphoto(False, tk.PhotoImage(file='logo.png'))
    window.title(app_name)

    def create_password_labels(_) -> None:
        """
        Called upon clicking the done button or pressing the ENTER key,
        this function creates the password or error label,
        and calls the ShowPassword function to show the passwords or error.

        :param _: Used for calling the function when pressing the ENTER key.
        """

        password_width = 100
        password_height = 1
        password_border_width = 0
        password_font = 'Consolas 11'

        error = 'An error occured. Try again with a whole number greater than 0.'

        password_label_1 = tk.Text(generate_password_frame, width=password_width, height=password_height,
                                   borderwidth=password_border_width, font=password_font)
        password_label_2 = tk.Text(generate_password_frame, width=password_width, height=password_height,
                                   borderwidth=password_border_width, font=password_font)
        password_label_3 = tk.Text(generate_password_frame, width=password_width, height=password_height,
                                   borderwidth=password_border_width, font=password_font)
        password_label_4 = tk.Text(generate_password_frame, width=password_width, height=password_height,
                                   borderwidth=password_border_width, font=password_font)
        password_labels = [password_label_1, password_label_2, password_label_3, password_label_4]

        try:
            for password_label in password_labels:
                password = logic.generate_password(int(input_box.get()))
                show_password(password_label, password, password_labels.index(password_label))

        except ValueError:
            input_box.delete(0, 'end')
            show_password(password_label_1, error, 0)

    input_box = tk.Entry(generate_password_frame, width=10, borderwidth=2)
    input_box.bind("<Return>", create_password_labels)
    input_box.place(relx = 0.5, rely = 0.2225, anchor = 'n')

    def show_password(label, text, index) -> None:
        """
        Called by the CreatePasswordLabels function,
        this function displays the passwords or an error.

        :param tk.Text label: Each individual password or error label.
        :param str text: The generated password or the error.
        :param int index: Which label is being displayed.
        """
        label.insert(1.0, text)
        label.place(relx = 0.5, rely = 0.485 + (index / 10), anchor = 'n')
        label.configure(state='disabled')  # Makes the text uneditable.

    done_button_image = tk.PhotoImage(file='doneButton.png')

    done_button_border_width = 0

    done_btn = tk.Button(generate_password_frame, image=done_button_image, borderwidth=done_button_border_width,
                         command = lambda: create_password_labels(None))
    done_btn.place(relx = 0.5, rely = 0.31, anchor = 'n')

    window.mainloop()

if __name__ == "__main__":
    exit(main())
