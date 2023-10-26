# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
import csv

import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv("026-ListDictComprehension/NATO-alphabet-start/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_input = input("Enter a word: ").upper()
nato_word = [nato_dict[letter] for letter in word_input]
nato_word_fixed = ''
for w in nato_word:
    nato_word_fixed += f"{w} "
print(nato_word_fixed)
