from pathlib import Path
import pandas
# import csv

CWD = f"{Path.cwd()}\\025-CSVFiles"

# with open(f"{CWD}\\Scratch_Weather\\weather_data.csv") as weather_data:
#     # data = weather_data.readlines()
#     # print(data)
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if not row[1] == "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

data = pandas.read_csv(f"{CWD}\\Scratch_Weather\\weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(data["temp"].mean())
print(data["temp"].max())

# Get data in column
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Using data from row
monday = data[data.day == "Monday"]
print((1.8 * monday.temp) + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv(f"{CWD}\\Scratch_Weather\\new_dataframe.csv")
