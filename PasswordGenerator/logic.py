import secrets
import string

characters = string.ascii_letters + string.punctuation

def GeneratePassword(length) -> str:
    '''
    Checks if the requested length is valid,
    returns a password if it is,
    raises a value error if it's not.
    '''
    if 1 <= length:
        if length > 100:
            length = 100

        return ''.join(secrets.choice(characters) for i in range(length)) # This is where the password itself is generated.

    else:
        raise ValueError
