import tkinter as tk
from tkinter import ttk as ttk
from PIL import ImageTk, Image
import generate_password
import password_strength

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

    done_btn_image = ImageTk.PhotoImage(Image.open('done_btn.png'))

    def motion(event):
        generate_password.update_mouse_coordinates(event.x_root - window.winfo_rootx(), event.y_root - window.winfo_rooty())
        password_strength.update_mouse_coordinates(event.x_root - window.winfo_rootx(), event.y_root - window.winfo_rooty())

    class GeneratePasswordFrame:
        '''
        A class that contains the creation of the "generate password" frame.

        ...

        Attributes
        ----------
        generate_password_frame: ttk.frame
            The generate password frame
        '''

        generate_password_frame = ttk.Frame(notebook, width = 854, height = 350)
        generate_password_frame.grid(column = 0, row = 1)
        notebook.add(generate_password_frame, text = 'Generate password')

        generate_password.show_generate_password_frame(generate_password_frame, done_btn_image)

    class PasswordStrengthFrame:
        '''
        A class that contains the creation of the "password strength" frame.

        ...

        Attributes
        ----------
        password_strength_frame: ttk.frame
            The password strength frame
        '''
        password_strength_frame = ttk.Frame(notebook, width = 854, height = 350)
        password_strength_frame.grid(column = 0, row = 0)
        notebook.add(password_strength_frame, text = 'Check a password\'s strength')

        password_strength.show_password_strength_frame(password_strength_frame)

    window.bind('<Motion>', motion)

    window.mainloop()

if __name__ == '__main__':
    exit(main())
