import pandas as pd

# save file path to variable for easier access
melbourne_file_path = 'input/melb_data.csv'

# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)

# print a summary of the data in Melbourne data
description = melbourne_data.describe(include='all')

print(description)
