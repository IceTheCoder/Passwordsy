import tkinter as tk

title_font = 'Helvetica 24'
tips_font = 'Helvetica 12'

file = open('passwords.txt', 'r')
read = file.readlines()
modified = []

for line in read:
    modified.append(line.strip())


def show_password_strength_frame(frame):
    global global_frame
    global_frame = frame
    instruction_label = tk.Label(frame, text = 'Type your password to check its strength', font = title_font)
    instruction_label.place(relx = 0.5, rely = 0, anchor = 'n')

    global input_box
    input_box = tk.Entry(frame, width = 16, borderwidth = 2)
    input_box.place(relx = 0.5, rely = 0.125, anchor = 'n')

    done_btn = tk.Button(frame, text = 'DONE', command = check_password_strength)
    done_btn.place(relx = 0.5, rely = 0.2, anchor = 'n')

    global first_label
    first_label = tk.Label(global_frame, font = tips_font, text = '')
    
    global second_label
    second_label = tk.Label(global_frame, font = tips_font, text = '')


def check_password_strength():
    first_label.place_forget()
    second_label.place_forget()


    def check_if_password_is_common():
        if len(input_box.get()) == 0:
            first_label.configure(text = 'Please input a password.')
            first_label.place(relx = 0.5, rely = 0.28, anchor = 'n')

        elif modified.count(input_box.get()) > 0:
            first_label.configure(text = 'Common: Your passord is common')
            first_label.place(relx = 0.01, rely = 0.3, anchor = 'w')

        elif modified.count(input_box.get()) == 0:
            first_label.configure(text = 'Not common: Your passord isn\'t common')
            first_label.place(relx = 0.01, rely = 0.3, anchor = 'w')

    def check_password_length():

        if len(input_box.get()) == 0:
            first_label.configure(text = 'Please input a password.')
            first_label.place(relx = 0.5, rely = 0.28, anchor = 'n')

        elif 0 < len(input_box.get()) <= 7:
            second_label.configure(text = 'Very weak: Your password has only ' + str(len(input_box.get())) + ' characters')
            second_label.place(relx = 0.01, rely = 0.4, anchor = 'w')
        
        elif 8 <= len(input_box.get()) <= 10:
            second_label.configure(text = 'Weak: Your password has only ' + str(len(input_box.get())) + ' characters')
            second_label.place(relx = 0.01, rely = 0.4, anchor = 'w')

        elif 11 <= len(input_box.get()) <= 13:
            second_label.configure(text = 'Good: Your password has ' + str(len(input_box.get())) + ' characters')
            second_label.place(relx = 0.01, rely = 0.4, anchor = 'w')

        elif 14 <= len(input_box.get()):
            second_label.configure(text = 'Strong: Your password has ' + str(len(input_box.get())) + ' characters')
            second_label.place(relx = 0.01, rely = 0.4, anchor = 'w')


    check_if_password_is_common()
    check_password_length()
