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
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=1)


# # # # # OPTIMIZE TREE DEPTH # # # # #

def get_mae(max_leaf_nodes, tx, vx, ty, vy):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
    model.fit(tx, ty)
    predictions = model.predict(vx)
    mae = mean_absolute_error(vy, predictions)
    return mae


# compare MAE with differing values of max_leaf_nodes
for n_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(n_leaf_nodes, train_x, val_x, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" % (n_leaf_nodes, my_mae))
