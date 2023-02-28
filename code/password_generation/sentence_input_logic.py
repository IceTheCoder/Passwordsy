
import string


def produce_password(sentence):
    """
    Called as the user types a sentence to be turned into a password,
    this function takes the sentence the user is typing,
    splits it into words,
    and returns the first letter of each word,
    as well as any punctuation and numbers.

    Parameters
    ----------
    sentence: str
        The sentence the user is typing.
    """
    password = ''

    split_full_sentence = sentence.split(' ')
    letters_only_sentence = ''

    for word in sentence:
        for letter in word:
            if letter not in string.digits and letter not in string.punctuation:
                letters_only_sentence += letter

    split_letters_only_sentence = letters_only_sentence.split(' ')

    for word in split_full_sentence:
        letter_taken = False
        for character in word:
            if character in string.digits or character in string.punctuation:
                password += character
            elif not letter_taken:
                password += character
                letter_taken = True

    return password


def check_password_strength(event, inputted_password) -> list | str:
    """
    Called upon pressing the done button,
    this function defines several functions that check
    the prevalence, length, complexity and repetitiveness of an inputted password,
    and returns appropriate messages.
    It then calls these functions and returns a list of messages indicating the results of each check.

    Parameters
    ----------
    event:
        Necessary for initiating the function as the user types.
    inputted_password: str
        The input of the user
    """
    user_input = []
    user_input[:0] = inputted_password  # Adds each character of the input to a list.

    def check_password_length() -> str:
        """
        Called by the check_password_strength function
        (as the user types),
        this function categorises the inputted password as very weak, weak, good, or strong depending on its length,
        and returns a suitable message.
        """
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

    def check_password_complexity() -> str:
        """
        Called by the check_password_strength function
        (as the user types),
        this function checks how many of the following the inputted password is missing:
        lowercase letters, uppercase letters, digits, and punctuation,
        and returns an adequate warning about them.
        """
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

        for character in user_input:
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

        if missing_security_features_list:
            output = ''

            for missing_feature in missing_security_features_list:
                if len(missing_security_features_list) == 1:
                    output = str(missing_feature)
                elif len(missing_security_features_list) == 2:
                    if missing_feature != missing_security_features_list[-1]:
                        output = output + str(missing_feature) + ' and '
                    else:
                        output += str(missing_feature)
                else:
                    if missing_feature == missing_security_features_list[-2]:
                        output = output + str(missing_feature) + ', and '
                    elif missing_feature == missing_security_features_list[-1]:
                        output += str(missing_feature)
                    else:
                        output = output + str(missing_feature) + ', '

            return f'Not complex: Your password is missing {output}.'

        else:
            return 'Complex: Your password contains lowercase letters, uppercase letters, digits, and punctuation.'

    return [check_password_length(), check_password_complexity()]
