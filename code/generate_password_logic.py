import string
import secrets

def validate_input(requested_password_length, lowercase_letters_var, uppercase_letters_var, digits_var, punctuation_var, no_character_set_error, input_box, double_error, invalid_input_error):
    '''Called by the create_password_labels function
    (upon clicking the done button or pressing the ENTER key),
    this function first checks if the input is valid and if at least 1 character set has been chosen
    (displays an error if not),
    and calls the generate_password function to return a password'''
    
    if lowercase_letters_var.get() == 0 and uppercase_letters_var.get() == 0 and digits_var.get() == 0 and punctuation_var.get() == 0:
        try:
            if 4 <= int(requested_password_length) <= 100:
                return no_character_set_error
            else:
                input_box.delete(0, 'end')
                return double_error
        except:
            input_box.delete(0, 'end')
            return double_error

    try:
        if not 4 <= int(requested_password_length) <= 100:
            input_box.delete(0, 'end')
            return invalid_input_error
    except:
        input_box.delete(0, 'end')
        return invalid_input_error
    
def generate_password(requested_password_length, lowercase_letters_var, uppercase_letters_var, digits_var, punctuation_var) -> None:
    '''
    Called by the validate_input function,
    this function generates a password based on the user's requested length and on the selected character sets.
    Parameters
    ----------
    requested_length: int
        The length requested by the user.
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
