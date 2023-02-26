
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
