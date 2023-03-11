"""
This is the main module of Passwordsy.
"""
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter

from password_generation import generate_password_gui
from password_strength import password_strength_gui


class TabView(customtkinter.CTkTabview):
    """
    This class creates the tabview of the app.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create the password generation frame
        self.generate_password_frame = generate_password_gui.PasswordGenerationFrame(master=self)
        self.generate_password_frame.grid(column=0, row=0)

        # Expand some widgets' rows and columns to take up the entire window
        self.generate_password_frame.grid_columnconfigure(0, weight=1)
        self.generate_password_frame.grid_rowconfigure(0, weight=1)
        self.generate_password_frame.grid_rowconfigure(1, weight=1)
        self.generate_password_frame.grid_rowconfigure(2, weight=1)
        self.generate_password_frame.grid_rowconfigure(3, weight=1)
        self.generate_password_frame.grid_rowconfigure(4, weight=1)
        self.generate_password_frame.grid_rowconfigure(5, weight=1)

        # Create the password strength frame
        self.password_strength_frame = password_strength_gui.PasswordStrengthFrame(master=self)
        self.password_strength_frame.grid(column=0, row=0)

        # Expand widgets to take up the entire window
        self.password_strength_frame.grid_columnconfigure(0, weight=1)
        self.password_strength_frame.grid_rowconfigure(0, weight=1)
        self.password_strength_frame.grid_rowconfigure(1, weight=1)
        self.password_strength_frame.grid_rowconfigure(2, weight=1)
        self.password_strength_frame.grid_rowconfigure(3, weight=1)
        self.password_strength_frame.grid_rowconfigure(4, weight=1)
        self.password_strength_frame.grid_rowconfigure(5, weight=1)
        self.password_strength_frame.grid_rowconfigure(6, weight=1)

        generate_password_frame = self.add('Generate password')
        password_strength_frame = self.add('Password strength')

        # Add those frames to the tabview
        #self.add(self.generate_password_frame, text='Generate password')
        #self.add(self.password_strength_frame, text='Password strength')


class App(customtkinter.CTk):
    """
    This class creates the app itself.
    """
    def __init__(self):
        super().__init__()

        # Center the notebook
        #self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(0, weight=1)
        self.iconbitmap('textures/logo.ico')

        app_name = 'Passwordsy'
        self.title(app_name)

        self.tab_view = TabView(master=self)
        self.tab_view.grid(column=0, row=0)
        #self.tab_view.bind('<<NotebookTabChanged>>', lambda e: generate_password_gui.select_input_box())


def main():
    """
    Called upon starting the program,
    this function uses the Tkinter module to create a window, notebook,
    two frames the user can switch between,
    and a basic configuration.
    """
    root = App()
    root.mainloop()


if __name__ == '__main__':
    exit(main())
