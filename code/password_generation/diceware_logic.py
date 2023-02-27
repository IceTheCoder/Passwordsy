import secrets

numbers = [1, 2, 3, 4, 5, 6]

# The wordlist is from https://github.com/ulif/diceware
diceware_wordlist = open('password_generation\wordlist_en_eff.txt', 'r')
diceware_wordlist_read = diceware_wordlist.readlines()
wordlist = {}

# Make a 'wordlist' dictionary, where the key is the dice roll numbers, and the value is the specific word.
for line in diceware_wordlist_read:
    # Split the line into a list of dice roll numbers and the corresponding word
    line_parts = line.strip().split('\t')
    dice_rolls = line_parts[0]
    word = line_parts[1]

    # Add the dice roll numbers and word to the dictionary
    wordlist[dice_rolls] = word


def roll_dice() -> None:
    """
    Called when the user clicks the 'done button' of the diceware frame,
    this function returns a random pair of the number formed by 5 dice rolls
    and the associated word with that number, according to the diceware wordlist.
    """
    final_pairs = {}
    dice_roll = ''

    i = 0
    while i < 5:
        dice_roll += str(secrets.choice(numbers))
        i += 1

    final_pairs[dice_roll] = wordlist[dice_roll]
    return final_pairs
