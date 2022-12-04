import tkinter as tk
import logic

root = tk.Tk()

root.minsize(854, 240)
root.maxsize(854, 240)
root.grid_columnconfigure(0, weight = 1)
root.resizable(0,0)
root.iconphoto(False, tk.PhotoImage(file='logo.png'))
root.title('Passwordsy')

welcome = tk.Label(root, text = 'Passwordsy', font = 'Helvetica 24')
welcome.grid(row = 1)
welcome.grid_rowconfigure(1, weight = 1)
welcome.grid_columnconfigure(1, weight = 1)

question = tk.Label(root, text = '(up to 100) Number of characters:', font = 'Helvetica 12')
question.grid(row = 3)
question.grid_rowconfigure(1, weight = 1)
question.grid_columnconfigure(1, weight = 1)

input = tk.Entry(root, width = 10, borderwidth = 2)
input.grid(row = 4)
input.grid_rowconfigure(1, weight = 1)
input.grid_columnconfigure(1, weight = 1)

tip = tk.Label(root, text = 'CTRL + C to copy \nCTRL + V to paste', font = 'Helvetica 12')
tip.grid(row = 2)
tip.grid_rowconfigure(1, weight = 1)
tip.grid_columnconfigure(1, weight = 1)

def ShowPassword(string) -> None:
        '''
        Displays the password or the error.
        '''
        password_label = tk.Text(root, width=100, height = 1, borderwidth = 0, font = 'Consolas 11')
        password_label.insert(1.0, string)
        password_label.grid(row = 6, pady = 10)
        password_label.configure(state = 'disabled') # Makes the text uneditable.
        password_label.grid_rowconfigure(1, weight = 1)
        password_label.grid_columnconfigure(1, weight = 1)


def StartPasswordGeneration() -> None:
    '''
    After clicking the done button,
    the function runs password generation
    and display the password or an error.
    '''
    try:
        password = logic.GeneratePassword(int(input.get()))
    
        ShowPassword(password)

    except ValueError:
        ShowPassword('An error occured. Try again with a whole number greater than 0.')


done_btn_image = tk.PhotoImage(file = 'doneButton.png')

done_btn = tk.Button(root, image = done_btn_image, borderwidth = 0, command = StartPasswordGeneration)
done_btn.grid(row = 5, column = 0, pady = 10, sticky = 'nsew')
done_btn.grid_rowconfigure(0, weight = 1)
done_btn.grid_columnconfigure(0, weight = 1)

root.mainloop()
