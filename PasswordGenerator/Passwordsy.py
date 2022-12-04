import secrets
import string
import tkinter as tk

root = tk.Tk()

characters = string.hexdigits + string.punctuation
error = "An error occured, try again with a whole number greater than 0."

root.minsize(854, 240)
root.maxsize(854, 240)
root.grid_columnconfigure(0, weight = 1)
root.resizable(0,0)
root.iconphoto(False, tk.PhotoImage(file="logo.png"))
root.title("Passwordsy")

welcome = tk.Label(root, text = "Passwordsy", font = 'Helvetica 24')
welcome.grid(row = 1)
welcome.grid_rowconfigure(1, weight = 1)
welcome.grid_columnconfigure(1, weight = 1)

question = tk.Label(root, text = "(up to 100) Number of characters:", font = 'Helvetica 12')
question.grid(row = 3)
question.grid_rowconfigure(1, weight = 1)
question.grid_columnconfigure(1, weight = 1)

input = tk.Entry(root, width = 10, borderwidth = 2)
input.grid(row = 4)
input.grid_rowconfigure(1, weight = 1)
input.grid_columnconfigure(1, weight = 1)

tip = tk.Label(root, text = "CTRL + C to copy \nCTRL + V to paste", font = 'Helvetica 12')
tip.grid(row = 2)
tip.grid_rowconfigure(1, weight = 1)
tip.grid_columnconfigure(1, weight = 1)

def Click() -> str:
    '''After clicking on the done button,
        it generates a password,
        and shows it on the screen.
    '''
    length_str = input.get()

    try:
        length_int = int(length_str) # Gets the length the user requested.
        if length_int > 100:
            length_int = 100 # Maxes it out at 100.
        if length_int <= 0:
            raise ValueError("Integer is less than 0")

        password = ''.join(secrets.choice(characters) for i in range(length_int))

        password_label = tk.Text(root, width=100, height = 1, borderwidth = 0, font = 'Consolas 11')
        password_label.insert(1.0, password)
        password_label.grid(row = 6, pady = 10) # Shows the password.
        password_label.configure(state = "disabled") # Makes it uneditable.
        password_label.grid_rowconfigure(1, weight = 1)
        password_label.grid_columnconfigure(1, weight = 1)

        password = ""
    except ValueError:
        password_label = tk.Text(root, width=100, height = 1, borderwidth = 0, font = 'Consolas 11')
        password_label.insert(1.0, error)
        password_label.grid(row = 6, pady = 10) # Shows the password.
        password_label.configure(state = "disabled") # Makes it uneditable.
        password_label.grid_rowconfigure(1, weight = 1)
        password_label.grid_columnconfigure(1, weight = 1)
        
done_btn_image = tk.PhotoImage(file="doneButton.png")

done_btn = tk.Button(root, image = done_btn_image, command=Click, borderwidth = 0)
done_btn.grid(row = 5, column = 0, pady = 10, sticky="nsew")
done_btn.grid_rowconfigure(0, weight = 1)
done_btn.grid_columnconfigure(0, weight = 1)

root.mainloop()
