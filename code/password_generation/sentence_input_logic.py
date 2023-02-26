
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
    split_sentence = sentence.split(' ')
    password = ''

    for word in split_sentence:
        password += word[0]

    return password


