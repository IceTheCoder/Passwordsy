import tkinter as tk
import string
from pynput.keyboard import Key, Controller

keyboard = Controller()

title_font = 'Helvetica 24'
warning_font = 'Helvetica 16'

common_passwords_file = open('passwords.txt', 'r') # passwords.txt is from the https://github.com/danielmiessler/SecLists repository.
common_passwords_read = common_passwords_file.readlines()
modified_common_passwords = []

for line in common_passwords_read:
    modified_common_passwords.append(line.strip()) # Places each of the 100,000 most commonly used passwords into a list

def show_paste_button(event) -> None:
    '''
    Called when the user right-clicks on the input box,
    this function displays a 'paste' button slightly above the mouse cursor,
    and places it on top of all other widgets.

    Parameters
    ----------
    event:
        Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
    '''
    paste.tk_popup(event.x_root, event.y_root - 30)

def paste_text() -> None:
    '''
    Called upon pressing the paste button,
    this function simulates pressing CTRL and V to paste the copied text.
    '''
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)
    keyboard.release('v')

def show_password_strength_frame(frame) -> None:
    '''
    Called upon starting the program,
    this function creates the contents of the "password strength" frame.

    Parameters
    ----------
    frame: ttk.Frame
        The "password strength" frame
    '''

    global paste
    paste = tk.Menu(frame, tearoff = False)
    paste.add_command(label = 'Paste', command = paste_text)

    instruction_label = tk.Label(frame, text = 'Type your password to check its strength', font = title_font)
    instruction_label.grid(column = 0, row = 1, sticky = 'n')

    global input_box
    input_box = tk.Entry(frame, width = 32, borderwidth = 2)
    input_box.grid(column = 0, row = 2, sticky = 'n')
    input_box.bind('<KeyRelease>', check_password_strength)
    input_box.bind('<Button-3>', show_paste_button)

    global first_label
    first_label = tk.Label(frame, font = warning_font, text = '')
    
    global second_label
    second_label = tk.Label(frame, font = warning_font, text = '')

    global third_label
    third_label = tk.Label(frame, font = warning_font, text = '')

    global fourth_label
    fourth_label = tk.Label(frame, font = warning_font, text = '')

    global warnings
    warnings = [first_label, second_label, third_label, fourth_label]

    for label in warnings:
        label.grid(column = 0, row = 3 + warnings.index(label))

def check_password_strength(event):
    '''
    Called upon pressing the done button,
    this function hosts all functions necesary to check:
    if a password is common, a password's length, complexity, and if a password contains repeated patterns.

    Parameters
    ----------
    event:
         Necessary for initiating the function as the user types.
    '''
    global warnings
    for label in warnings:
        label.grid(column = 0, row = 3 + warnings.index(label))
        label.configure(text = '')

    def check_if_password_is_common():
        '''
        Called by the check_password_strength function
        (upon pressing the done button),
        this function checks if there's any input,
        checks if the input is in the 100,000 most used passwords if there is input,
        asks the user to input a password if there's no input.
        '''
        if modified_common_passwords.count(input_box.get()) > 0:
            first_label.configure(text = 'Common: Your password is common.')
            first_label.grid(column = 0, row = 3, sticky = 'w')

        elif modified_common_passwords.count(input_box.get()) == 0:
            first_label.configure(text = 'Not common: Your password isn\'t common.')
            first_label.grid(column = 0, row = 3, sticky = 'w')

    def check_password_length():
        '''
        Called by the check_password_strength function
        (upon pressing the done button),
        this function checks if there's any input,
        categorises the inputted password as very weak, weak, good, or strong depending on its length if there is input,
        asks the user to input a password if there's no input.
        '''
        if len(input_box.get()) == 1:
            second_label.configure(text = 'Very weak length: Your password has only ' + str(len(input_box.get())) + ' character.')
            second_label.grid(column = 0, row = 4, sticky = 'w')

        elif 0 < len(input_box.get()) <= 7:
            second_label.configure(text = 'Very weak length: Your password has only ' + str(len(input_box.get())) + ' characters.')
            second_label.grid(column = 0, row = 4, sticky = 'w')
        
        elif 8 <= len(input_box.get()) <= 10:
            second_label.configure(text = 'Weak length: Your password has only ' + str(len(input_box.get())) + ' characters.')
            second_label.grid(column = 0, row = 4, sticky = 'w')

        elif 11 <= len(input_box.get()) <= 13:
            second_label.configure(text = 'Good length: Your password has ' + str(len(input_box.get())) + ' characters.')
            second_label.grid(column = 0, row = 4, sticky = 'w')

        elif 14 <= len(input_box.get()):
            second_label.configure(text = 'Strong length: Your password has ' + str(len(input_box.get())) + ' characters.')
            second_label.grid(column = 0, row = 4, sticky = 'w')

    def check_password_complexity():
        '''
        Called by the check_password_strength function
        (upon pressing the done button),
        this function checks if there's any input,
        checks how many of the following the inputted password is missing: 
        lowercase letters, uppercase letters, digits, and punctuation,
        and warns the user about them if there is input,
        asks the user to input a password if there's no input.
        '''
        missing_security_features_list = []

        # Places each character into a list based on its type.
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
                if len(missing_security_features_list) == 1:
                    output = str(missing_feature)
                elif missing_feature != missing_security_features_list[-1]:
                    output = output + str(missing_feature) + ', '
                else:
                    output = output + 'and ' + str(missing_feature)
            
            third_label.configure(text = 'Not complex: Your password is missing ' + output + '.')
            third_label.grid(column = 0, row = 5, sticky = 'w')

        else:
            third_label.configure(text = 'Complex: Your password contains lowercase letters, uppercase letters, digits, and punctation.')
            third_label.grid(column = 0, row = 5, sticky = 'w')

    def check_for_patterns_in_password():
        '''
        Called by the check_password_strength function
        (upon pressing the done button),
        this function checks if there's any input,
        checks if there are any repeating characters in the input if there is,
        asks the user to input a password if there's not.
        '''

        global are_there_repeated_characters
        are_there_repeated_characters = False

        input = []
        input[:0] = input_box.get() # Adds each character of the input to a list.

        def show_repeated_pattern_warning():
            '''
            Called by the check_for_patterns_in_password_function
            (upon pressing the done button),
            this function warns the user if there are repeated characters in their password.
            '''

            fourth_label.configure(text = 'Repeated character(s): Your password contains at least one repeated character.')
            fourth_label.grid(column = 0, row = 6, sticky = 'w')

        for character in input: # For every character in the input, it checks if there is another character that matches, and shows the repeated pattern warning if there is.
            count = 0
            for other_character in input:
                if character == other_character:
                    count += 1

            if count > 1:
                are_there_repeated_characters = True
                show_repeated_pattern_warning()

        if are_there_repeated_characters == False:
            fourth_label.configure(text = 'No repeated characters: Your password contains no repeated characters.')
            fourth_label.grid(column = 0, row = 6, sticky = 'w')

    if len(input_box.get()) == 0:
        first_label.configure(text = 'Please input a password.')
        first_label.grid(column = 0, row = 3, sticky = 'n')
    else:
        check_if_password_is_common()   
        check_password_length()    
        check_password_complexity() 
        check_for_patterns_in_password()
