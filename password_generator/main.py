import tkinter as tk
from tkinter import ttk as ttk
import generate_password
from PIL import ImageTk, Image

def main() -> None:
    '''
    Called upon starting the program,
    it generates the window, notebook and frames for the app.
    '''
    window = tk.Tk()
    notebook = ttk.Notebook(window)
    notebook.grid(column = 0, row = 0)

    window_width = 854
    window_height = 350
    horizontal_resizable_ability = False
    vertical_resizable_ability = False
    app_name = 'Passwordsy'

    window.minsize(window_width, window_height)
    window.maxsize(window_width, window_height)

    window.grid_columnconfigure(0, weight = 1)
    window.resizable(horizontal_resizable_ability, vertical_resizable_ability)
    window.iconphoto(False, tk.PhotoImage(file = 'logo.png'))
    window.title(app_name)

    class GeneratePasswordFrame:
        '''
        A class that contains the creation of the "generate password" frame.

        ...

        Attributes
        ----------
        generate_password_frame: ttk.frame
            The generate password frame
        done_btn_image: ImageTk.PhotoImage
            The photo that will be used for the done button.
        '''
        generate_password_frame = ttk.Frame(notebook, width = 854, height = 350)
        generate_password_frame.grid(column = 0, row = 1)
        notebook.add(generate_password_frame, text = 'Generate password')
        done_btn_image = ImageTk.PhotoImage(Image.open('done_button.png'))

        generate_password.show_generate_password_frame(generate_password_frame, done_btn_image)

    password_strength_frame = ttk.Frame(notebook, width = 854, height = 350)
    password_strength_frame.grid(column = 0, row = 0)
    notebook.add(password_strength_frame, text = 'Check a password\'s strength')

    window.mainloop()

if __name__ == '__main__':
    exit(main())
