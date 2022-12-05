import tkinter as tk
import logic

def main():
    window = tk.Tk()

    window.minsize(854, 240)
    window.maxsize(854, 240)
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


    def ShowPassword(string) -> None:
            '''
            Displays the password or the error.
            '''
            password_label = tk.Text(window, width=100, height = 1, borderwidth = 0, font = 'Consolas 11')
            password_label.insert(1.0, string)
            password_label.grid(row = 6, pady = 10)
            password_label.configure(state = 'disabled') # Makes the text uneditable.
            password_label.grid_rowconfigure(1, weight = 1)
            password_label.grid_columnconfigure(1, weight = 1)


    def StartPasswordGeneration() -> None:
        '''
        After clicking the done button,
        the function runs password generation
        and displays the password or an error.
        '''
        try:
            password = logic.GeneratePassword(int(input_box.get()))
            ShowPassword(password)

        except ValueError:
            ShowPassword('An error occured. Try again with a whole number greater than 0.')


    done_btn_image = tk.PhotoImage(file = 'doneButton.png')

    done_btn = tk.Button(window, image = done_btn_image, borderwidth = 0, command = StartPasswordGeneration)
    done_btn.grid(row = 5, column = 0, pady = 10)
    done_btn.grid_rowconfigure(0, weight = 1)
    done_btn.grid_columnconfigure(0, weight = 1)

    window.mainloop()
        
if __name__ == "__main__":
    exit(main())
