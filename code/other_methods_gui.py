import tkinter as tk
from PIL import ImageTk, Image


def create_other_methods_window():
    other_methods_window = tk.Toplevel()

    window_title = 'Try other methods...'

    other_methods_window.iconphoto(False, tk.PhotoImage(file='logo.png'))
    other_methods_window.title(window_title)
