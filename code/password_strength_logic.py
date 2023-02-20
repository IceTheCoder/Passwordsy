import string

common_passwords_file = open('passwords.txt', 'r') # passwords.txt is from the https://github.com/danielmiessler/SecLists repository.
common_passwords_read = common_passwords_file.readlines()
modified_common_passwords = []

for line in common_passwords_read:
    modified_common_passwords.append(line.strip()) # Places each of the 100,000 most commonly used passwords into a list

def check_password_strength(event, warnings, first_label, inputted_password, second_label, third_label, fourth_label) -> None:
    '''
    Called upon pressing the done button,
    this function hosts all functions necessary to check:
    if a password is common, a password's length, complexity, and if a password contains repeated patterns.

    Parameters
    ----------
    event:
        Necessary for initiating the function as the user types.
    warnings: list
        A list containing the warning labels.
    first_label: tkinter.Label()
        The first warning label.
    inputted_password: str
        The password inputted by the user.
    sceond_label: tkinter.Label()
        The second warning label.
    trhird_label: tkinter.Label()
        The third warning label.
    fourth_label: tkinter.Label()
        The fourth warning label.    
    '''
    for label in warnings:
        label.configure(text = '')

    input = []
    input[:0] = inputted_password # Adds each character of the input to a list.

    def check_if_password_is_common() -> None:
        '''
        Called by the check_password_strength function
        (upon pressing the done button),
        checks if the inputted password is in the 100,000 most used passwords (modified_common_password).
        '''
        if modified_common_passwords.count(inputted_password) > 0:
            first_label.configure(text = 'Common: Your password is common.')
            first_label.grid(column = 0, row = 3, sticky = 'w')

        elif modified_common_passwords.count(inputted_password) == 0:
            first_label.configure(text = 'Not common: Your password isn\'t common.')
            first_label.grid(column = 0, row = 3, sticky = 'w')

    def check_password_length() -> None:
        '''
        Called by the check_password_strength function
        (upon pressing the done button),
        this function categorises the inputted password as very weak, weak, good, or strong depending on its length.
        '''
        if len(inputted_password) == 1:
            second_label.configure(text = f'Very weak length: Your password has only {str(len(inputted_password))} character.')
            second_label.grid(column = 0, row = 4, sticky = 'w')

        elif 0 < len(inputted_password) <= 7:
            second_label.configure(text = f'Very weak length: Your password has only {str(len(inputted_password))} characters.')
            second_label.grid(column = 0, row = 4, sticky = 'w')
        
        elif 8 <= len(inputted_password) <= 10:
            second_label.configure(text = f'Weak length: Your password has only {str(len(inputted_password))} characters.')
            second_label.grid(column = 0, row = 4, sticky = 'w')

        elif 11 <= len(inputted_password) <= 13:
            second_label.configure(text = f'Good length: Your password has {str(len(inputted_password))} characters.')
            second_label.grid(column = 0, row = 4, sticky = 'w')

        elif 14 <= len(inputted_password):
            second_label.configure(text = f'Strong length: Your password has {str(len(inputted_password))} characters.')
            second_label.grid(column = 0, row = 4, sticky = 'w')

    def check_password_complexity() -> None:
        '''
        Called by the check_password_strength function
        (upon pressing the done button),
        checks how many of the following the inputted password is missing: 
        lowercase letters, uppercase letters, digits, and punctuation,
        and warns the user about them.
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

        number_of_lowercase_letters = 0
        number_of_uppercase_letters = 0
        number_of_digits = 0
        number_of_punctuation = 0

        for character in input:
            if character in lowercase_letters:
                number_of_lowercase_letters += 1
            elif character in uppercase_letters:
                number_of_uppercase_letters += 1
            elif character in digits:
                number_of_digits += 1
            elif character in punctuation:
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
            
            third_label.configure(text = f'Not complex: Your password is missing {output}.')
            third_label.grid(column = 0, row = 5, sticky = 'w')

        else:
            third_label.configure(text = 'Complex: Your password contains lowercase letters, uppercase letters, digits, and punctation.')
            third_label.grid(column = 0, row = 5, sticky = 'w')

    def check_for_patterns_in_password() -> None:
        '''
        Called by the check_password_strength function
        (upon pressing the done button),
        this function checks if there are any repeating characters in the inputted password.
        '''

        global are_there_repeated_characters
        are_there_repeated_characters = False

        def show_repeated_pattern_warning() -> None:
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

    if len(inputted_password) == 0:
        first_label.configure(text = 'Please input a password.')
        first_label.grid(column = 0, row = 3, sticky = 'n')
    else:
        prevalance_warning = check_if_password_is_common()   
        length_warning = check_password_length()    
        complexity_warning = check_password_complexity() 
        pattern_warning = check_for_patterns_in_password()

        return [prevalance_warning, length_warning, complexity_warning, pattern_warning]
