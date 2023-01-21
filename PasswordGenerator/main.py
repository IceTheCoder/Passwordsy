import tkinter as tk
import logic


def main():
    window = tk.Tk()

    window_width = 854
    window_height = 350
    resizable_ability = False
    app_name = 'Passwordsy'
    description_font = 'Helvetica 12'

    window.minsize(window_width, window_height)
    window.maxsize(window_width, window_height)
    window.grid_columnconfigure(0, weight=1)
    window.resizable(resizable_ability, resizable_ability)
    window.iconphoto(False, tk.PhotoImage(file='logo.png'))
    window.title(app_name)

    title = tk.Label(window, text=app_name, font='Helvetica 24')
    title.grid(row=1)

    question = tk.Label(window, text='Number of characters (up to 100):', font=description_font)
    question.grid(row=3)

    tip = tk.Label(window, text='CTRL + C to copy \nCTRL + V to paste', font=description_font)
    tip.grid(row=2)

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

        password_label_1 = tk.Text(window, width=password_width, height=password_height,
                                   borderwidth=password_border_width, font=password_font)
        password_label_2 = tk.Text(window, width=password_width, height=password_height,
                                   borderwidth=password_border_width, font=password_font)
        password_label_3 = tk.Text(window, width=password_width, height=password_height,
                                   borderwidth=password_border_width, font=password_font)
        password_label_4 = tk.Text(window, width=password_width, height=password_height,
                                   borderwidth=password_border_width, font=password_font)
        password_labels = [password_label_1, password_label_2, password_label_3, password_label_4]

        try:
            for password_label in password_labels:
                password = logic.generate_password(int(input_box.get()))
                show_password(password_label, password, password_labels.index(password_label))

        except ValueError:
            input_box.delete(0, 'end')
            show_password(password_label_1, error, 0)

    input_box = tk.Entry(window, width=10, borderwidth=2)
    input_box.bind("<Return>", create_password_labels)
    input_box.grid(row=4)

    def show_password(label, text, index) -> None:
        """
        Called by the CreatePasswordLabels function,
        this function displays the passwords or an error.

        :param tk.Text label: Each individual password or error label.
        :param str text: The generated password or the error.
        :param int index: Which label is being displayed.
        """
        label.insert(1.0, text)
        label.grid(row=6 + index, pady=5)
        label.configure(state='disabled')  # Makes the text uneditable.

    done_button_image = tk.PhotoImage(file='doneButton.png')

    done_button_border_width = 0

    done_btn = tk.Button(window, image=done_button_image, borderwidth=done_button_border_width,
                         command=lambda: create_password_labels(None))
    done_btn.grid(row=5, column=0, pady=10)

    window.mainloop()


if __name__ == "__main__":
    exit(main())
