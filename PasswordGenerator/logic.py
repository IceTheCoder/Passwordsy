import secrets
import string

characters = string.ascii_letters + string.punctuation + string.digits

def GeneratePassword(requested_length) -> str:
    '''
    Called by the CreatePasswordLabels function,
    this function checks if the requested_length is valid,
    returns a password if it is,
    raises a value error if it's not.

    :param int requested_length: The length inputed by the user in the input box.
    :raises ValueError: if the requested_length is not an integer.
    '''
    
    try:
        legnth_int = min(int(requested_length), 100)
        return ''.join(secrets.choice(characters) for i in range(legnth_int)) # This is where the password itself is generated
    except:
        raise ValueError
