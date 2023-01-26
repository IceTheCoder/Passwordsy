import tkinter as tk

title_font = 'Helvetica 24'

file = open('passwords.txt', 'r')
read = file.readlines()
modified = []

for line in read:
    modified.append(line.strip())


def show_password_strength_frame(frame):
    global global_frame
    global_frame = frame
    my_label = tk.Label(frame, text = 'Type your password to check its strength', font = title_font)
    my_label.place(relx = 0.5, rely = 0, anchor = 'n')

    global input_box
    input_box = tk.Entry(frame, width = 16, borderwidth = 2)
    input_box.place(relx = 0.5, rely = 0.125, anchor = 'n')

    done_btn = tk.Button(frame, text = 'DONE', command = check_password_strength)
    done_btn.place(relx = 0.5, rely = 0.2, anchor = 'n')

    global result_label
    result_label = tk.Label(global_frame, font = title_font)
    

def check_password_strength():

    if len(input_box.get()) == 0:
        result_label.configure(text = 'Please input a password.')
        result_label.place(relx = 0.5, rely = 0.3, anchor = 'n')
    elif modified.count(input_box.get()) > 0:
        result_label.configure(text = 'Your passord is common')
        result_label.place(relx = 0.5, rely = 0.3, anchor = 'n')
    elif modified.count(input_box.get()) == 0:
        result_label.configure(text = 'Your passord isn\'t common')
        result_label.place(relx = 0.5, rely = 0.3, anchor = 'n')

    # Find a way to check if the input is in the top 100,000 most commonly used passwords according to SecLists.