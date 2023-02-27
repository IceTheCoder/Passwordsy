wordlist = open('wordlist_en_eff.txt', 'r')
wordlist_read = wordlist.readlines()
modified_wordlist = []

for line in wordlist_read:
    modified_wordlist.append(line.strip())  # Place each of the 100,000 most commonly used passwords into a list

length = 0

for word in modified_wordlist:
    if len(word) > length:
        length = len(word)

print(length)
