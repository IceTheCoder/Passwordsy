import tkinter as tk
import string as string

title_font = 'Helvetica 24'
tips_font = 'Helvetica 12'

common_passwords_file = open('passwords.txt', 'r')
common_passwords_read = common_passwords_file.readlines()
modified_common_passwords = []

for line in common_passwords_read:
    modified_common_passwords.append(line.strip())

def show_password_strength_frame(frame, done_btn_image):
    '''
    Called upon starting the program,
    this function creates the "password strength" frame.

    Parameters
    ----------
    frame: ttk.Frame
        The "password strength" frame
    done_btn_image: tk.PhotoImage
        Image of the done button
    '''
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

    global fourth_label
    fourth_label = tk.Label(global_frame, font = tips_font, text = '')



def check_password_strength():
    '''
    Called upon pressing the done button,
    this functions hosts all functions neccesary to check:
    if a password is common, a password's length, a password's complexity, if a password contains repeated patterns.
    '''
    first_label.place_forget()
    second_label.place_forget()
    third_label.place_forget()
    fourth_label.place_forget()

    def check_if_password_is_common():
        '''
        Called upon pressing the done button,
        this function checks if there's any input,
        searches if the password is in the 100,000 most used ones if there is,
        asks the user to input a password if there's not.
        '''
        if len(input_box.get()) == 0:
            first_label.configure(text = 'Please input a password.')
            first_label.place(relx = 0.5, rely = 0.38, anchor = 'n')

        elif modified_common_passwords.count(input_box.get()) > 0:
            first_label.configure(text = 'Common: Your passord is common.')
            first_label.place(relx = 0.01, rely = 0.4, anchor = 'w')

        elif modified_common_passwords.count(input_box.get()) == 0:
            first_label.configure(text = 'Not common: Your passord isn\'t common.')
            first_label.place(relx = 0.01, rely = 0.4, anchor = 'w')

    def check_password_length():
        '''
        Called upon pressing the done button,
        this function checks if there's any input,
        categorises the inputted password as very weak, weak, good, or strong depending on its length if there is,
        asks the user to input a password if there's not.
        '''
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
        '''
        Called upon pressing the done button,
        this function checks if there's any input,
        checks how many of the following the inputted password is missing: 
        lowercase letters, uppercase letters, digits, and punctuation,
        and warns the user about them if there is input,
        asks the user to input a password if there's not.
        '''

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
    
    def check_for_patterns_in_password():
        '''
        Called upon pressing the done button,
        this function checks if there's any input,
        checks if there are any repeating characters in the input if there is,
        asks the user to input a password if there's not.
        '''

        input = []
        input[:0] = input_box.get()

        def show_repeated_pattern_warning():
            '''
            Called upon pressing the done button,
            this function checks if there's any input,
            warns the user if there is a repeating pattern if there is input,
            asks the user to input a password if there's not.
            '''

            fourth_label.configure(text = 'Repeated character: Your password contains at least one repeated character.')
            fourth_label.place(relx = 0.01, rely = 0.7, anchor = 'w')

        for character in input:
            count = 0
            for other_character in input:
                if character == other_character:
                    count += 1
            if count > 1:
                show_repeated_pattern_warning()

    check_if_password_is_common()
    check_password_length()
    check_password_complexity()
    check_for_patterns_in_password()
