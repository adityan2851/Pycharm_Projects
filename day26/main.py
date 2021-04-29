import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter your name").upper()
output = [_dict[letter] for letter in word]
print(output)
