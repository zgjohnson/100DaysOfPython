import pandas

nato_dict = {row.letter: row.code for (index, row) in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows()}
# print(nato_dict)

word = input("Enter a word? \n").upper()
nato_list = [nato_dict[letter] for letter in word]
print(nato_list)
