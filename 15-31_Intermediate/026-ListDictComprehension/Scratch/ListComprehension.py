# Old way
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension
numbers = [1, 2, 3]
new_numbers = [(n+1) for n in numbers]

# String as List
my_name = "Bryan"
letters = [letter for letter in my_name]

# Int as List
x = 12345
num = [int(number) for number in str(x)]

# Range as List
range = [y * 2 for y in range(1, 5)]

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]

