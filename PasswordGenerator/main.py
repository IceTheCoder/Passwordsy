import tkinter as tk
import logic

def main():
    window = tk.Tk()

    window.minsize(854, 480)
    window.maxsize(854, 480)
    window.grid_columnconfigure(0, weight = 1)
    window.resizable(0,0)
    window.iconphoto(False, tk.PhotoImage(file='logo.png'))
    window.title('Passwordsy')

    title = tk.Label(window, text = 'Passwordsy', font = 'Helvetica 24')
    title.grid(row = 1)
    title.grid_rowconfigure(1, weight = 1)
    title.grid_columnconfigure(1, weight = 1)

    question = tk.Label(window, text = 'Number of characters (up to 100):', font = 'Helvetica 12')
    question.grid(row = 3)
    question.grid_rowconfigure(1, weight = 1)
    question.grid_columnconfigure(1, weight = 1)

    input_box = tk.Entry(window, width = 10, borderwidth = 2)
    input_box.grid(row = 4)
    input_box.grid_rowconfigure(1, weight = 1)
    input_box.grid_columnconfigure(1, weight = 1)

    tip = tk.Label(window, text = 'CTRL + C to copy \nCTRL + V to paste', font = 'Helvetica 12')
    tip.grid(row = 2)
    tip.grid_rowconfigure(1, weight = 1)
    tip.grid_columnconfigure(1, weight = 1)


    def createPasswordLabels() -> None:
            '''
            Called upon done button click,
            this function creates the password/error label(s),
            and calls the ShowPassword function to show the passwords or error.
            '''

            password_label_1 = tk.Text(window, width=100, height = 1, borderwidth = 0, font = 'Consolas 11')
            password_label_2 = tk.Text(window, width=100, height = 1, borderwidth = 0, font = 'Consolas 11')
            password_label_3 = tk.Text(window, width=100, height = 1, borderwidth = 0, font = 'Consolas 11')
            password_label_4 = tk.Text(window, width=100, height = 1, borderwidth = 0, font = 'Consolas 11')
            password_labels = [password_label_1, password_label_2, password_label_3, password_label_4]

            try:
                for password_label in password_labels:
                    password = logic.generatePassword(input_box.get())
                    showPassword(password_label, password, password_labels.index(password_label))

            except:
                showPassword(password_label_1, 'An error occured. Try again with a whole number greater than 0.', 0)


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
        label.grid_rowconfigure(1 , weight = 1)
        label.grid_columnconfigure(1, weight = 1)


    done_btn_image = tk.PhotoImage(file = 'doneButton.png')

    done_btn = tk.Button(window, image = done_btn_image, borderwidth = 0, command = createPasswordLabels)
    done_btn.grid(row = 5, column = 0, pady = 10)
    done_btn.grid_rowconfigure(0, weight = 1)
    done_btn.grid_columnconfigure(0, weight = 1)

    window.mainloop()
        
if __name__ == "__main__":
    exit(main())
