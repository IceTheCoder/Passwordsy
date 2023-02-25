import string
import secrets
import clipboard
from pynput.keyboard import Controller

keyboard = Controller()


def adapt_input(requested_password_length) -> int:
    """
    Called by the create_password_labels function
    (upon pressing the done button),
    this function first checks if any input has been given.
    It raises a ValueError if no input has been given,
    and if input has been given,
    it attempts to adapt the input to an integer between 4 and 100.
    If it succeeds, it returns the adapted input,
    if it fails, it raises a ValueError.

    Parameters
    ----------
    requested_password_length: str
        The input of the user.
    """
    if requested_password_length == '':
        raise ValueError
    else:
        try:
            generated_password = max(min(abs(int(round(float(requested_password_length), 0))), 100), 4)
            return generated_password
        except ValueError:
            raise ValueError


def determine_error(valid_character_set_bool, requested_password_length, no_character_set_error, double_error,
                    invalid_input_error) -> str:
    """
    Called by create_password_labels,
    (upon pressing the done button)
    this function returns what error should be shown to the user:
    an invalid_input_error if a character set has been chosen, but the input is unadaptable.
    a no_character_set_error if no character set has been chosen, but the input is adaptable,
    or a double_error if no character set has been chosen, and the input is unadaptable.

    Parameters
    ----------
    valid_character_set_bool: boolean
        Whether at least one character set has been chosen, as determined by validate_character_sets.
    requested_password_length: str
        The input_box content.
    no_character_set_error: str
        'An error occurred. Try again with at least 1 character set.'
    double_error: str
        'An error occurred. Try again with at least 1 character set and a whole number between 4 and 100.'
    invalid_input_error: str
        'An error occurred. Try again with a whole number between 4 and 100.'
    """
    if valid_character_set_bool:
        try:
            adapt_input(requested_password_length)
            return ''
        except ValueError:
            return invalid_input_error
    else:
        try:
            adapt_input(requested_password_length)
            return no_character_set_error
        except ValueError:
            return double_error


def validate_character_sets(lowercase_letters_var, uppercase_letters_var, digits_var, punctuation_var) -> bool:
    """
    Called by the create_password_labels function
    (upon pressing the done button),
    this function checks if at least one character set has been chosen by the user,
    and returns a boolean.

    Parameters
    ----------
    lowercase_letters_var: tkinter.IntVar()
        The variable of the lowercase letters checkbox.
    uppercase_letters_var: tkinter.IntVar()
        The variable of the uppercase letters checkbox.
    digits_var: tkinter.IntVar()
        The variable of the digits checkbox.
    punctuation_var: tkinter.IntVar()
        The variable of the punctuation checkbox.
    """
    if lowercase_letters_var.get() == 0 and uppercase_letters_var.get() == 0 and digits_var.get() == 0 \
            and punctuation_var.get() == 0:
        return False
    else:
        return True


def generate_password(requested_password_length, lowercase_letters_var, uppercase_letters_var, digits_var,
                      punctuation_var) -> str:
    """
    Called by the validate_input function,
    this function returns a password based on the user's requested length and on the selected character sets.

    Parameters
    ----------
    requested_password_length: int
        The length requested by the user.
    lowercase_letters_var: tkinter.IntVar()
        The variable used to check if the lowercase letters checkbox has been selected or not.
    uppercase_letters_var: tkinter.IntVar()
        The variable used to check if the uppercase letters checkbox has been selected or not.
    digits_var: tkinter.IntVar()
        The variable used to check if the digits checkbox has been selected or not.
    punctuation_var: tkinter.IntVar()
        The variable used to check if the punctuation checkbox has been selected or not.
    """
    # Define all character sets that will be used in the password
    character_sets = []
    if lowercase_letters_var.get() == 1:
        character_sets.append(string.ascii_lowercase)
    if uppercase_letters_var.get() == 1:
        character_sets.append(string.ascii_uppercase)
    if digits_var.get() == 1:
        character_sets.append(string.digits)
    if punctuation_var.get() == 1:
        character_sets.append(string.punctuation)

    # Keep generating a new password until it includes at least one character from each chosen character set
    while True:
        password = ''.join(secrets.choice(''.join(character_sets)) for _ in range(int(requested_password_length)))
        if all(any(char in s for char in password) for s in character_sets):
            return password


def show_copy_button(event, copy) -> None:
    """
    Called when the user releases a mouse button on a password label,
    this function uses the Tkinter module to display a contextual menu containing a 'copy' button
    for copying the password to the clipboard on the x and y coordinates of the user's cursor,
    where the y coordinates are adjusted by 30 pixels.

    Parameters
    ----------
    event: tkinter.event
        Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
    copy: tkinter.Menu()
        The copy button itself.
    """
    copy.tk_popup(event.x_root, event.y_root - 30)


def copy_text(input_box, labels) -> None:
    """
    Called upon pressing the copy button,
    this function copies the selected text,
    and focuses the keyboard on the input_box to deselect the text.
    """
    for label in labels:
        selected_text = label.selection_get()
        clipboard.copy(selected_text)

    input_box.focus_set()
