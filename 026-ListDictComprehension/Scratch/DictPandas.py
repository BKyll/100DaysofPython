# Iterate of Pandas DataFrame
import pandas

student_dict = {
    "student": ["Bryan", "James", "Lily"],
    "scores" : [56, 76, 98]
}

# Looping through a dictionary
# for (key, value) in student_dict.items():
#     print(value)

# Looping through a dataframe
student_df = pandas.DataFrame(student_dict)
# print(student_df)

# for (key, value) in student_df.items():
#     print(value)

for (index, row) in student_df.iterrows():
    if row.student == 'Bryan':
        print(row.scores)
