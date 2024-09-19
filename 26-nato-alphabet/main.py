
import pandas as pd

file = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {}


for (index, row) in file.iterrows():
    phonetic_dict[row.letter] = row.code


while True:
    word = input("Enter a word: ")
    word = word.upper()

    if word == "EXIT":
        break

    res = [phonetic_dict[ele] for ele in word]
    print(res)

