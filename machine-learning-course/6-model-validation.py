import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


# # # # # PREVIOUS # # # # #

melbourne_file_path = 'input/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data = melbourne_data.dropna(axis=0)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = melbourne_data[melbourne_features]


# # # # # SLIP DATA # # # # #

train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=0)
melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(train_x, train_y)


# # # # # MEAN ABSOLUTE ERROR # # # # #

predictions = melbourne_model.predict(val_x)
mae = mean_absolute_error(val_y, predictions)
print('The mean absolute error is', mae)
