from sklearn.tree import DecisionTreeRegressor
import numpy as np
X_temp = np.array([[200], [250], [300], [350]])
y_time = np.array([20, 15, 10, 7])
pizza_tree = DecisionTreeRegressor().fit(X_temp, y_time)
print(int(pizza_tree.predict([[275]])[0]))