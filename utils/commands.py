# Standard
import secrets

from tkinter import messagebox, Text

# Pip
# None

# Custom
# None


def generate_password(user_input, characters, root) -> None:
    """

    After clicking on the done button,
    it generates a password, and shows it on the screen.

    :args:
        user_input(Entry): Entry widget for entering string lenght
        characters (str): String collection from which a password is generated.
        root(Tkinter): The tkinter window from which this command is evoked.

    :return:
        None
    """

    length_str = user_input.get()
    try:
        length_int = int(length_str)  # Gets the length the user requested.
        if length_int > 100:
            length_int = 100  # Maxes it out at 100.
        password = "".join(secrets.choice(characters) for i in range(length_int))

        password_label = Text(
            root, width=100, height=1, borderwidth=0, font="Consolas 11"
        )
        password_label.insert(1.0, password)
        password_label.grid(row=6, pady=10)  # Shows the password.
        password_label.configure(state="disabled")  # Makes it uneditable.
        password_label.grid_rowconfigure(1, weight=1)
        password_label.grid_columnconfigure(1, weight=1)

        password = ""
    except ValueError:
        messagebox.showerror(
            title="Incorrect Value",
            message="Only numbers are allowed!"
        )


if __name__ == "__main__":
    pass
