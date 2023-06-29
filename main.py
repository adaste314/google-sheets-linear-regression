from data_loader import load_data_from_sheet
from linear_regression import perform_linear_regression
from plotter import plot_regression_results

def main():
    # Load data from Google Sheets
    record = load_data_from_sheet('adam_stepansky_data')

    # Perform linear regression
    x_name, y_name, x_test, y_test, variable_y_pred = perform_linear_regression(record)

    # Plot regression results
    plot_regression_results(x_test, y_test, variable_y_pred, x_name, y_name)

if __name__ == '__main__':
    main()
