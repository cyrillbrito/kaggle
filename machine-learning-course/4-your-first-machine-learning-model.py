import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# # # # # PREPARE DATA # # # # #

melbourne_file_path = 'input/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

# Get prediction target using the dot-notation
y = melbourne_data.Price

# List of features
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

# Data
x = melbourne_data[melbourne_features]


# # # # # DEFINE MODEL # # # # #

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(x, y)

print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(melbourne_model.predict(x.head()))
print(y.head())
