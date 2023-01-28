import tkinter as tk
import string as string

title_font = 'Helvetica 24'
tips_font = 'Helvetica 12'

file = open('passwords.txt', 'r')
read = file.readlines()
modified = []

for line in read:
    modified.append(line.strip())


def show_password_strength_frame(frame, done_btn_image):
    global global_frame
    global_frame = frame
    instruction_label = tk.Label(frame, text = 'Type your password to check its strength', font = title_font)
    instruction_label.place(relx = 0.5, rely = 0, anchor = 'n')

    global input_box
    input_box = tk.Entry(frame, width = 16, borderwidth = 2)
    input_box.place(relx = 0.5, rely = 0.125, anchor = 'n')

    done_btn = tk.Button(frame, image = done_btn_image, text = 'DONE', borderwidth = 0, command = check_password_strength)
    done_btn.place(relx = 0.5, rely = 0.2, anchor = 'n')

    global first_label
    first_label = tk.Label(global_frame, font = tips_font, text = '')
    
    global second_label
    second_label = tk.Label(global_frame, font = tips_font, text = '')

    global third_label
    third_label = tk.Label(global_frame, font = tips_font, text = '')


def check_password_strength():
    first_label.place_forget()
    second_label.place_forget()
    third_label.place_forget()

    def check_if_password_is_common():
        if len(input_box.get()) == 0:
            first_label.configure(text = 'Please input a password.')
            first_label.place(relx = 0.5, rely = 0.38, anchor = 'n')

        elif modified.count(input_box.get()) > 0:
            first_label.configure(text = 'Common: Your passord is common.')
            first_label.place(relx = 0.01, rely = 0.4, anchor = 'w')

        elif modified.count(input_box.get()) == 0:
            first_label.configure(text = 'Not common: Your passord isn\'t common.')
            first_label.place(relx = 0.01, rely = 0.4, anchor = 'w')

    def check_password_length():
        if len(input_box.get()) == 0:
            first_label.configure(text = 'Please input a password.')
            first_label.place(relx = 0.5, rely = 0.38, anchor = 'n')

        elif 0 < len(input_box.get()) <= 7:
            second_label.configure(text = 'Very weak length: Your password has only ' + str(len(input_box.get())) + ' characters.')
            second_label.place(relx = 0.01, rely = 0.5, anchor = 'w')
        
        elif 8 <= len(input_box.get()) <= 10:
            second_label.configure(text = 'Weak length: Your password has only ' + str(len(input_box.get())) + ' characters.')
            second_label.place(relx = 0.01, rely = 0.5, anchor = 'w')

        elif 11 <= len(input_box.get()) <= 13:
            second_label.configure(text = 'Good length: Your password has ' + str(len(input_box.get())) + ' characters.')
            second_label.place(relx = 0.01, rely = 0.5, anchor = 'w')

        elif 14 <= len(input_box.get()):
            second_label.configure(text = 'Strong length: Your password has ' + str(len(input_box.get())) + ' characters.')
            second_label.place(relx = 0.01, rely = 0.5, anchor = 'w')

    def check_password_complexity():
        if len(input_box.get()) == 0:
            first_label.configure(text = 'Please input a password.')
            first_label.place(relx = 0.5, rely = 0.38, anchor = 'n')
        else:

            missing_security_features_list = []
    
            lowercase_letters = []
            lowercase_letters[:0] = string.ascii_lowercase
    
            uppercase_letters = []
            uppercase_letters[:0] = string.ascii_uppercase
    
            digits = []
            digits[:0] = string.digits
    
            punctuation = []
            punctuation[:0] = string.punctuation
    
            input = []
            input[:0] = input_box.get()
    
            number_of_lowercase_letters = 0
            number_of_uppercase_letters = 0
            number_of_digits = 0
            number_of_punctuation = 0
    
            for character in input:
                if character in lowercase_letters:
                    number_of_lowercase_letters += 1
                if character in uppercase_letters:
                    number_of_uppercase_letters += 1
                if character in digits:
                    number_of_digits += 1
                if character in punctuation:
                    number_of_punctuation += 1
    
            if number_of_lowercase_letters == 0:
                missing_security_features_list.append('lowercase letters')
            if number_of_uppercase_letters == 0:
                missing_security_features_list.append('uppercase letters')
            if number_of_digits == 0:
                missing_security_features_list.append('digits')
            if number_of_punctuation == 0:
                missing_security_features_list.append('punctuation')
    
            if missing_security_features_list != []:
                output = ''
    
                for missing_feature in missing_security_features_list:
                    if missing_feature != missing_security_features_list[-1]:
                        output = output + str(missing_feature) + ', '
                    else:
                        output = output + 'and ' + str(missing_feature)
                
                third_label.configure(text = 'Not complex: Your password is missing ' + output + '.')
                third_label.place(relx = 0.01, rely = 0.6, anchor = 'w')
    
            else:
                third_label.configure(text = 'Complex: Your password contains lowercase letters, uppercase letters, digits, and punctation.')
                third_label.place(relx = 0.01, rely = 0.6, anchor = 'w')
    

    check_if_password_is_common()
    check_password_length()
    check_password_complexity()
