"""
This module deals with the logical part of discovering vulnerabilities in a given password.
"""
from __future__ import annotations
import string
from pynput.keyboard import Key, Controller
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

keyboard = Controller()

# passwords.txt is from the https://github.com/danielmiessler/SecLists repository.
# https://www.youtube.com/watch?v=DCaKj3eIrro
passwords_file = Path('password_strength/passwords.txt')
with passwords_file.open() as f:
    common_passwords_read = f.read().strip().splitlines()


# https://www.reddit.com/user/ekchew/
def as_text_list(iterable_input: Iterable) -> str:
    """
    Given ["foo", "bar", "baz"], returns "foo, bar, and baz".
    """
    lst = list(iterable_input)
    if len(lst) <= 2:
        text = " and ".join(lst)  # e.g. "", "foo", or "foo and bar"
    else:
        lst[-1] = f"and {lst[-1]}"  # ["foo", "bar", "and baz"]
        text = ", ".join(lst)  # "foo, bar, and baz"
    return text


def check_if_password_is_common(inputted_password) -> str:
    """
    Called by the check_password_strength function
    (as the user types),
    this function checks if the inputted password is in the 100,000 most used passwords (common_passwords_read),
    and returns an appropriate message.
    It does this by counting the number of times an inputted_password is found in the SecLists list.
    """
    # https://www.reddit.com/user/Diapolo10/
    if common_passwords_read.count(inputted_password) > 0:
        return 'Common: Your password is common.'
    return 'Not common: Your password isn\'t common.'


def check_password_length(inputted_password) -> str:
    """
    Called by the check_password_strength function
    (as the user types),
    this function categorises the inputted password as very weak, weak, good, or strong depending on its length,
    and returns a suitable message.
    """
    if 0 < len(inputted_password) <= 7:
        return f"Very weak length: Your password has only {len(inputted_password)} character" \
               f"{'s' if len(inputted_password) != 1 else ''}."  # https://www.reddit.com/user/Diapolo10/
    elif 8 <= len(inputted_password) <= 10:
        return f'Weak length: Your password has only {str(len(inputted_password))} characters.'
    elif 11 <= len(inputted_password) <= 13:
        return f'Good length: Your password has {str(len(inputted_password))} characters.'
    elif 14 <= len(inputted_password):
        return f'Strong length: Your password has {str(len(inputted_password))} characters.'


def check_password_complexity(user_input) -> str:
    """
    Called by the check_password_strength function
    (as the user types),
    this function checks how many of the following the inputted password is missing:
    lowercase letters, uppercase letters, digits, and punctuation,
    and returns an adequate warning about them.
    """
    missing_security_features_list = []
    # https://www.reddit.com/user/Diapolo10/
    has_lowercase_letters = False
    has_uppercase_letters = False
    has_digits = False
    has_punctuation = False
    # User input is a list of each character of the inputted password
    for character in user_input:
        if character in string.ascii_lowercase:
            has_lowercase_letters = True
        elif character in string.ascii_uppercase:
            has_uppercase_letters = True
        elif character in string.digits:
            has_digits = True
        elif character in string.punctuation:
            has_punctuation = True
    if not has_lowercase_letters:
        missing_security_features_list.append('lowercase letters')
    if not has_uppercase_letters:
        missing_security_features_list.append('uppercase letters')
    if not has_digits:
        missing_security_features_list.append('digits')
    if not has_punctuation:
        missing_security_features_list.append('punctuation')
    output = as_text_list(missing_security_features_list)
    if output:
        return f'Not complex: Your password is missing {output}.'
    else:
        return 'Complex: Your password contains lowercase letters, uppercase letters, digits, and punctuation.'


def check_for_patterns_in_password(inputted_password) -> str:
    """
    Called by the check_password_strength function
    (as the user types),
    this function checks if there are any repeating characters in the inputted password,
    and returns an adequate message.
    """
    for character in inputted_password:
        if inputted_password.count(character) > 1:
            return 'Repeated character(s): Your password contains at least one repeated character.'
    return 'No repeated characters: Your password contains no repeated characters.'


def check_password_strength(inputted_password: str, input_password_msg: str) -> list | str:
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
    input_password_msg: str
        'Please input a password.'
    """
    user_input = []
    user_input[:0] = inputted_password  # Adds each character of the input to a list.

    if len(inputted_password) == 0:
        return input_password_msg
    else:
        prevalence_warning = check_if_password_is_common(inputted_password)
        length_warning = check_password_length(inputted_password)
        complexity_warning = check_password_complexity(user_input)
        pattern_warning = check_for_patterns_in_password(inputted_password)

        return [prevalence_warning, length_warning, complexity_warning, pattern_warning]


def paste_text() -> None:
    """
    Called upon pressing the paste button,
    this function uses the keyboard module to simulate pressing CTRL and V to paste text into the input_box.
    """
    # https://youtu.be/DTnz8wA6wpw
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)
    keyboard.release('v')
