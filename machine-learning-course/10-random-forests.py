import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# # # # # PREVIOUS # # # # #

melbourne_file_path = 'input/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data = melbourne_data.dropna(axis=0)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = melbourne_data[melbourne_features]
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=1)


# # # # # RANDOM FOREST # # # # #

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_x, train_y)
melb_preds = forest_model.predict(val_x)
print(mean_absolute_error(val_y, melb_preds))
