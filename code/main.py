"""
This is the main module of Passwordsy.
"""
import tkinter as tk
from abc import ABC
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter

from password_generation import generate_password_gui
from password_strength import password_strength_gui


class TabView(customtkinter.CTkTabview, ABC):
    """
    A CustomTkinter tab view with two tabs: 'Generate password' and 'Password strength'.

    Inherits from customtkinter.CTkTabview to provide functionality for creating and managing tabs.

    Attributes:
        tab_names: list
            A list of strings containing the names of the two tabs.

    Methods:
        __init__(self, master, **kwargs): Constructor for the TabView class.
            Initializes the two tabs, sets their sizes, and adds the widgets to them.

    Usage:
        Instantiate the TabView class passing the master widget as an argument to create a CustomTkinter
        tab view with two tabs: "Generate password" and "Password strength".
    """
    tab_names = ["Generate password", "Password strength"]

    def __init__(self, master: customtkinter.CTkTabview, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=1200, height=485)

        # Create the tabs using the configured names
        for tab_name in self.tab_names:
            self.add(tab_name)

        self.generate_password_frame = generate_password_gui.PasswordGenerationFrame(
            master=self.tab(self.tab_names[0]))
        self.generate_password_frame.pack(fill='both', expand=1)
        self.generate_password_frame.configure(fg_color=('#DBDBDB', '#2B2B2B'))

        # Expand some widgets' rows and columns to take up the entire window
        self.generate_password_frame.grid_columnconfigure(0, weight=1)
        i = 0
        self.generate_password_frame.grid_rowconfigure(0, weight=1)
        self.generate_password_frame.grid_rowconfigure(1, weight=1)
        self.generate_password_frame.grid_rowconfigure(2, weight=1)
        self.generate_password_frame.grid_rowconfigure(3, weight=1)
        self.generate_password_frame.grid_rowconfigure(4, weight=1)
        self.generate_password_frame.grid_rowconfigure(5, weight=1)
        self.generate_password_frame.grid_rowconfigure(6, weight=1)
        self.generate_password_frame.grid_rowconfigure(7, weight=1)
        self.generate_password_frame.grid_rowconfigure(8, weight=1)
        # To prevent lag
        self.generate_password_frame.grid_propagate(False)

        # Create the password strength frame
        self.password_strength_frame = password_strength_gui.PasswordStrengthFrame(master=self.tab(self.tab_names[1]))
        self.password_strength_frame.pack(fill='both', expand=1)
        self.password_strength_frame.configure(fg_color=('#DBDBDB', '#2B2B2B'))

        # Expand widgets to take up the entire window
        self.password_strength_frame.grid_columnconfigure(0, weight=1)
        i = 0
        while i <= 6:
            self.password_strength_frame.grid_rowconfigure(i, weight=1)
            i += 1


def resize(root_window: tk.Tk, event: tk.Event = None) -> None:
    """
    This function aims to reduce resizing lag.

    Parameters
    ----------
    root_window: tk.Tk()
        The main window of the app.
    event:
        Necessary for executing the function when the user resizes.

    Returns
    -------
    None
    """
    root_window.update_idletasks()


class App(customtkinter.CTk):
    """
    This class creates the app itself.
    """
    def __init__(self):
        super().__init__()

        # Center the notebook
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.iconbitmap('textures/logo.ico')
        self.geometry('1200x485')

        app_name = 'Passwordsy'
        self.title(app_name)

        self.tab_view = TabView(master=self)
        self.tab_view.grid(column=0, row=0)

        self.bind('<Configure>', lambda a: resize(self))


def main() -> None:
    """
    Called upon starting the program,
    this function uses the Tkinter module to create a window, notebook,
    two frames the user can switch between,
    and a basic configuration.

    Returns
    -------
    None
    """
    root = App()
    root.mainloop()


if __name__ == '__main__':
    exit(main())
