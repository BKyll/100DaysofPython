# Dictionary Comprehension
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(30, 100) for student in names}
# Mine
passed_students = {student: student_scores[student] for student in student_scores if student_scores[student] > 70}
# Example
# passed_students = {new_key: new_value for (key, value) in dictionary.items()}
passed_students = {student: score for (student, score) in student_scores.items() if score > 70}

# DAY 26 - DICTIONARY COMPREHENSION 1
# Input: "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇
result = {word: len(word) for word in sentence.split()}

print(result)


# DAY 26 - DICTIONARY COMPREHENSION 2
# Input: {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_c = eval(input())
# 🚨 Don't change code above 👆
# Write your code 👇 below:
weather_f = {c: weather_c[c] * (9/5) + 32 for c in weather_c}
# Actual
# weather_f = {day: temp * (9/5) + 32 for (day, temp) in weather_c.items()}

print(weather_f)
