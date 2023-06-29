import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np

def load_data_from_sheet(sheet_name):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    data = sheet.get_all_values()
    header = data[0]
    records = data[1:]

    x_col_name, y_col_name = header[0], header[1]
    variable_x = np.array([float(record[0]) for record in records])
    variable_y = np.array([float(record[1]) for record in records])

    return x_col_name, y_col_name, variable_x, variable_y
