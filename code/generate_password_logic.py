import string
import secrets
from pynput.keyboard import Key, Controller
import clipboard

keyboard = Controller()

def adapt_input(requested_password_length):
    if requested_password_length == '':
        raise ValueError
    else:
        try:
            return max(min(abs(int(round(float(requested_password_length), 0))), 100), 4)
        except:
            raise ValueError

def validate_input(lowercase_letters_var, uppercase_letters_var, digits_var, punctuation_var, no_character_set_error, input_box, double_error, invalid_input_error) -> str:
    '''
    Called by the create_password_labels function,
    this function checks if a password can be generated.
    It first checks if the user has chosen any characters sets,
    then it checks if the user's chosen length is valid,
    and displays an adequate error.

    Parameters
    ----------
    requested_password_length: int
        The length requested by the user.
    lowercase_letters_var: tkinter.IntVar()
        The variable used to check if the lowercase letters checkbox has been selected or not.
    uppercase_letters_var: tkinter.IntVar()
        The variable used to check if the upprcase letters checkbox has been selected or not.
    digits_var: tkinter.IntVar()
        The variable used to check if the digits checkbox has been selected or not.
    punctuation_var: tkinter.IntVar()
        The variable used to check if the punctuation checkbox has been selected or not.
    no_character_set_error: str
        The error used when no character set has been picked.
    input_box: tkinter.Entry()
        The input box used for the length of the password.
    double_error: str
        The error used when no character set has been picked and when the input is invalid.
    invalid_input_error: str
        The error used when the input is invalid.
    '''
    try:
        if lowercase_letters_var.get() == 0 and uppercase_letters_var.get() == 0 and digits_var.get() == 0 and punctuation_var.get() == 0:
            return no_character_set_error
        else:
            return invalid_input_error
    except:
        if lowercase_letters_var.get() == 0 and uppercase_letters_var.get() == 0 and digits_var.get() == 0 and punctuation_var.get() == 0:
            return double_error
        else:
            return invalid_input_error
    
def generate_password(requested_password_length, lowercase_letters_var, uppercase_letters_var, digits_var, punctuation_var) -> str:
    '''
    Called by the validate_input function,
    this function returns a password based on the user's requested length and on the selected character sets.

    Parameters
    ----------
    requested_password_length: int
        The length requested by the user.
    lowercase_letters_var: tkinter.IntVar()
        The variable used to check if the lowercase letters checkbox has been selected or not.
    uppercase_letters_var: tkinter.IntVar()
        The variable used to check if the upprcase letters checkbox has been selected or not.
    digits_var: tkinter.IntVar()
        The variable used to check if the digits checkbox has been selected or not.
    punctuation_var: tkinter.IntVar()
        The variable used to check if the punctuation checkbox has been selected or not.
    '''
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
    '''
    Called when the user releases a mouse button on a password label,
    this function uses the Tkinter module to display a contextual menu containing a 'copy' button for copying the password to the clipboard on the x and y coordinates of the user's cursor,
    where the y coordinates are adjusted by 30 pixels.

    Parameters
    ----------
    event:
        Gets the coordinates of the mouse cursor when the user releases a mouse button on a password_label.
    copy:
        The copy button itself.
    '''
    copy.tk_popup(event.x_root, event.y_root - 30)

def copy_text(input_box, labels) -> None:
    '''
    Called upon pressing the copy button,
    this function copies the selected text,
    and focuses the keyboard on the input_box to deselect the text.
    '''
    for label in labels:
        selected_text = label.selection_get()
        clipboard.copy(selected_text)

    input_box.focus_set()
