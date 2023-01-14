import tkinter as tk
import logic

def main():
    window = tk.Tk()

    WINDOW_WIDTH = 854
    WINDOW_HEIGHT = 350
    RESIZABLE_ABILITY = 0
    APP_NAME = 'Passwordsy'
    DESCRIPTION_FONT = 'Helvetica 12'

    window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.grid_columnconfigure(0, weight = 1)
    window.resizable(RESIZABLE_ABILITY, RESIZABLE_ABILITY)
    window.iconphoto(False, tk.PhotoImage(file='logo.png'))
    window.title(APP_NAME)

    title = tk.Label(window, text = APP_NAME, font = 'Helvetica 24')
    title.grid(row = 1)

    question = tk.Label(window, text = 'Number of characters (up to 100):', font = DESCRIPTION_FONT)
    question.grid(row = 3)

    tip = tk.Label(window, text = 'CTRL + C to copy \nCTRL + V to paste', font = DESCRIPTION_FONT)
    tip.grid(row = 2)

    def createPasswordLabels(event) -> None:
            '''
            Called upon clicking the done button or pressing the ENTER key,
            this function creates the password or error label,
            and calls the ShowPassword function to show the passwords or error.

            :param event: Used for calling the function when pressing the ENTER key.
            '''

            PASSWORD_WIDTH = 100
            PASSWORD_HEIGHT = 1
            PASSWORD_BORDER_WIDTH = 0
            PASSWORD_FONT = 'Consolas 11'
            
            error = 'An error occured. Try again with a whole number greater than 0.'

            password_label_1 = tk.Text(window, width = PASSWORD_WIDTH, height = PASSWORD_HEIGHT, borderwidth = PASSWORD_BORDER_WIDTH, font = PASSWORD_FONT)
            password_label_2 = tk.Text(window, width = PASSWORD_WIDTH, height = PASSWORD_HEIGHT, borderwidth = PASSWORD_BORDER_WIDTH, font = PASSWORD_FONT)
            password_label_3 = tk.Text(window, width = PASSWORD_WIDTH, height = PASSWORD_HEIGHT, borderwidth = PASSWORD_BORDER_WIDTH, font = PASSWORD_FONT)
            password_label_4 = tk.Text(window, width = PASSWORD_WIDTH, height = PASSWORD_HEIGHT, borderwidth = PASSWORD_BORDER_WIDTH, font = PASSWORD_FONT)
            password_labels = [password_label_1, password_label_2, password_label_3, password_label_4]

            try:
                for password_label in password_labels:
                    password = logic.generatePassword(input_box.get())
                    showPassword(password_label, password, password_labels.index(password_label))

            except ValueError:
                showPassword(password_label_1, error, 0)

    input_box = tk.Entry(window, width = 10, borderwidth = 2)
    input_box.bind("<Return>", createPasswordLabels)
    input_box.grid(row = 4)

    def showPassword(label, text, index) -> None:
        '''
        Called by the CreatePasswordLabels function,
        this function displays the passwords or an error.

        :param tk.Text label: Each individual password or error label.
        :param str text: The generated password or the error.
        :param int index: Which label is being displayed.
        '''
        label.insert(1.0, text)
        label.grid(row = 6 + index, pady = 5)
        label.configure(state = 'disabled') # Makes the text uneditable.


    done_btn_image = tk.PhotoImage(file = 'doneButton.png')

    DONE_BUTTON_BORDER_WIDTH = 0

    done_btn = tk.Button(window, image = done_btn_image, borderwidth = DONE_BUTTON_BORDER_WIDTH, command = lambda: createPasswordLabels(None))
    done_btn.grid(row = 5, column = 0, pady = 10)

    window.mainloop()

if __name__ == "__main__":
    exit(main())


