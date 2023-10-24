# # File not found
# with open("a_file.txt") as file:
#     file.read()

# # Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existant_key"]

# # Index Error
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]

# # Type Error
# text = "abc"
# print(text + 5)

# # Error Catching
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")

# BMI
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height can not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
