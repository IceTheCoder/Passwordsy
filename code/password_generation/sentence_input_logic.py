"""
This module deals with the logic part of generating a secure password based on a user's sentence.
"""
from __future__ import annotations

import string
import clipboard
from tkinter import TclError


def check_password_strength(inputted_password) -> list | str:
    """
    Called upon pressing the done button,
    this function defines several functions that check
    the prevalence, length, complexity and repetitiveness of an inputted password,
    and returns appropriate messages.
    It then calls these functions and returns a list of messages indicating the results of each check.

    Parameters
    ----------
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
            return f'Your password has only {str(len(inputted_password))} character. ' \
                   f'You should write a longer sentence.'

        elif 0 < len(inputted_password) <= 7:
            return f'Very weak length: Your password has only {str(len(inputted_password))} characters. ' \
                   f'You should write a longer sentence.'

        elif 8 <= len(inputted_password) <= 10:
            return f'Weak length: Your password has only {str(len(inputted_password))} characters. ' \
                   f' should write a longer sentence.'

        elif 11 <= len(inputted_password) <= 13:
            return f'Good length: Your password has {str(len(inputted_password))} characters. ' \
                   f'You could write a longer sentence.'

        elif 14 <= len(inputted_password):
            return f'Strong length: Your password has {str(len(inputted_password))} characters'

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

            return f'Simple password: You should add {output} to your sentence.'

        else:
            return 'Complex password: Your sentence contains upper and lowercase letters, digits, and punctuation.'

    if inputted_password is None:
        return ['', '']
    else:
        return [check_password_length(), check_password_complexity()]


def produce_password(char_dict) -> list:
    """
    This function gets the characters that are needed to be highlighted:
    starting letters of every word and any digits or punctuation
    """
    letters_to_be_coloured = {}
    password = ''

    first_letter_taken = False
    for key, value in char_dict.items():
        if value in string.punctuation or value in string.digits:
            letters_to_be_coloured[f'1.{key}'] = f'1.{key + 1}'
            password += value
        elif value == 'space':
            first_letter_taken = False
        elif not first_letter_taken:
            letters_to_be_coloured[f'1.{key}'] = f'1.{key + 1}'
            password += value
            first_letter_taken = True

    return [letters_to_be_coloured, password]


def copy_selected_text(labels) -> None:
    """
    Called upon pressing the copy button,
    this function copies the selected text,
    and focuses the keyboard on the input_box to deselect the text.
    """
    try:
        for label in labels:
            selected_text = str(label.selection_get())
            clipboard.copy(selected_text)
    except (ValueError, TclError):
        # There is no need to warn the user when they try to copy nothing as it does not have any effect on the app
        pass
