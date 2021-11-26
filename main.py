# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
df = pd.DataFrame(data)
df_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(df_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type a word: ").upper()

# This code outputs in different orders as expected
# p_code_words = [code for (letter, code) in df_dict.items() if letter in user_input]
p_code_words = [df_dict[letter] for letter in user_input if letter in df_dict]

print(p_code_words)
