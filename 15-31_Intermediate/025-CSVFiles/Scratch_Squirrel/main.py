from pathlib import Path
import pandas

CWD = f"{Path.cwd()}\\025-CSVFiles"

# Use squirrel data to create a csv called squirrel_count.csv
# csv contains chart of squirrel colors and the total number of those colors.

data = pandas.read_csv(f"{CWD}\\Scratch_Squirrel\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data["Primary Fur Color"].value_counts().to_csv(f"{CWD}\\Scratch_Squirrel\\squirrel_color_data.csv")