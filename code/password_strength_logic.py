import string

common_passwords_file = open('passwords.txt', 'r') # passwords.txt is from the https://github.com/danielmiessler/SecLists repository.
common_passwords_read = common_passwords_file.readlines()
modified_common_passwords = []

for line in common_passwords_read:
    modified_common_passwords.append(line.strip()) # Place each of the 100,000 most commonly used passwords into a list


def check_password_strength(event, inputted_password, input_password_msg) -> list:
    '''
    Called upon pressing the done button,
    this function defines several functions that check the prevalance, length, complexity and repetitiveness of an inputted password, 
    and returns appropriate messages. 
    It then calls these functions and returns a list of messages indicating the results of each check.

    Parameters
    ----------
    event:
        Necessary for initiating the function as the user types.
    inputted_password: str
        The input of the user
    input_password_msg: str
        'Please input a password.'
    '''
    input = []
    input[:0] = inputted_password # Adds each character of the input to a list.

    def check_if_password_is_common() -> None:
        '''
        Called by the check_password_strength function
        (as the user types),
        this function checks if the inputted password is in the 100,000 most used passwords (modified_common_password),
        and returns an appropiate message.
        It does this by counting the number of times an inputted_password is found in the SecLists list.
        '''
        if modified_common_passwords.count(inputted_password) > 0:
            return 'Common: Your password is common.'

        elif modified_common_passwords.count(inputted_password) == 0:
            return 'Not common: Your password isn\'t common.'

    def check_password_length() -> None:
        '''
        Called by the check_password_strength function
        (as the user types),
        this function categorises the inputted password as very weak, weak, good, or strong depending on its length,
        and returns a suitable message.
        '''
        if len(inputted_password) == 1:
            return f'Very weak length: Your password has only {str(len(inputted_password))} character.'

        elif 0 < len(inputted_password) <= 7:
            return f'Very weak length: Your password has only {str(len(inputted_password))} characters.'
        
        elif 8 <= len(inputted_password) <= 10:
            return f'Weak length: Your password has only {str(len(inputted_password))} characters.'

        elif 11 <= len(inputted_password) <= 13:
            return f'Good length: Your password has {str(len(inputted_password))} characters.'

        elif 14 <= len(inputted_password):
            return f'Strong length: Your password has {str(len(inputted_password))} characters.'

    def check_password_complexity() -> None:
        '''
        Called by the check_password_strength function
        (as the user types),
        this function checks how many of the following the inputted password is missing: 
        lowercase letters, uppercase letters, digits, and punctuation,
        and returns an adequate warning about them.
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
            
            return f'Not complex: Your password is missing {output}.'

        else:
            return 'Complex: Your password contains lowercase letters, uppercase letters, digits, and punctation.'

    def check_for_patterns_in_password() -> None:
        '''
        Called by the check_password_strength function
        (as the user types),
        this function checks if there are any repeating characters in the inputted password,
        and returns an adequate message.
        '''
        for character in inputted_password:
            if inputted_password.count(character) > 1:
                return 'Repeated character(s): Your password contains at least one repeated character.'
        
        return 'No repeated characters: Your password contains no repeated characters.'

    if len(inputted_password) == 0:
        return input_password_msg
    else:
        prevalance_warning = check_if_password_is_common()   
        length_warning = check_password_length()    
        complexity_warning = check_password_complexity() 
        pattern_warning = check_for_patterns_in_password()

        return [prevalance_warning, length_warning, complexity_warning, pattern_warning]
