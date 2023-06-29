import matplotlib.pyplot as plt

def plot_regression_results(x_test, y_test, variable_y_pred, x_col_name, y_col_name):
    plt.figure(num='Linear Regression')
    plt.scatter(x_test, y_test, marker='o', s=1, color="black")
    plt.plot(x_test, variable_y_pred, color="blue", linewidth=1)

    plt.title(f"{x_col_name} vs. {y_col_name}")
    plt.xlabel(x_col_name)
    plt.ylabel(y_col_name)

    scale_x = [i for i in range(int(max(x_test.flatten())) + 1)]
    scale_y = [i for i in range(int(max(y_test.flatten())) + 10)]
    plt.xticks(scale_x[0::1])
    plt.yticks(scale_y[0::10])
    plt.show()
