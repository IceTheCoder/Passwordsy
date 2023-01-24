import tkinter as tk

title_font = 'Helvetica 24'

def show_password_strength_frame(frame):
    my_label = tk.Label(frame, text = 'Type your password to check its strength', font = title_font)
    my_label.place(relx = 0.5, rely = 0, anchor = 'n')

    input_box = tk.Entry(frame, width = 16, borderwidth = 2)
    input_box.place(relx = 0.5, rely = 0.125, anchor = 'n')

    while True:
        pass
