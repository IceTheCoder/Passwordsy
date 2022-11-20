# Standard
import secrets
import string

from tkinter import Tk, PhotoImage, Label, Entry, Text, Button

# Pip
# None

# Custom
from utils.commands import generate_password


def main_passwordsy() -> None:
    """
    The main program to invoke passwordsy


    :args:
        None

    :return:
        None

    """
    root = Tk()

    characters = string.hexdigits + string.punctuation

    root.minsize(854, 240)
    root.maxsize(854, 240)
    root.grid_rowconfigure(7, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.resizable(0, 0)
    root.iconphoto(
        False, PhotoImage(file="passwordsy_assets/img_assets/passwordsy_logo.png")
    )
    root.title("Passwordsy")

    welcome = Label(root, text="Passwordsy", font="Helvetica 24")
    welcome.grid(row=1)
    welcome.grid_rowconfigure(1, weight=1)
    welcome.grid_columnconfigure(1, weight=1)

    question = Label(
        root, text="(up to 100) Number of characters:", font="Helvetica 12"
    )
    question.grid(row=3)
    question.grid_rowconfigure(1, weight=1)
    question.grid_columnconfigure(1, weight=1)

    user_input = Entry(root, width=10, borderwidth=2)
    user_input.grid(row=4)
    user_input.grid_rowconfigure(1, weight=1)
    user_input.grid_columnconfigure(1, weight=1)

    tip = Label(root, text="CTRL + C to copy \nCTRL + V to paste", font="Helvetica 12")
    tip.grid(row=2)
    tip.grid_rowconfigure(1, weight=1)
    tip.grid_columnconfigure(1, weight=1)

    done_img = PhotoImage(file="passwordsy_assets/img_assets/done_button.png")

    done_button = Button(
        root,
        image=done_img,
        command=lambda: generate_password(user_input, characters, root),
        borderwidth=0,
    )
    done_button.grid(row=5, column=0, pady=10, sticky="nsew")
    done_button.grid_rowconfigure(0, weight=1)
    done_button.grid_columnconfigure(0, weight=1)

    root.mainloop()


if __name__ == "__main__":
    pass
