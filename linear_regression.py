import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def perform_linear_regression(record):
    x_col_name, y_col_name, variable_x, variable_y = record

    x_train, x_test, y_train, y_test = train_test_split(variable_x, variable_y, test_size=0.2, random_state=0)
    x_train, x_test = x_train.reshape(-1, 1), x_test.reshape(-1, 1)
    y_train, y_test = y_train.reshape(-1, 1), y_test.reshape(-1, 1)

    regr = LinearRegression()
    regr.fit(x_train, y_train)
    variable_y_pred = regr.predict(x_test)

    return x_col_name, y_col_name, x_test, y_test, variable_y_pred
