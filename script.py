# Python Selenium - imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Python GoogleSheetsAPI-imports
from googleapiclient.discovery import build
from google.oauth2 import service_account

from pages.automations_page import AutomationsPage
from apis.google_api import GoogleApi



# SERVICE_ACCOUNT_FILE = 'keys.json'
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# my_credentials = None
# my_credentials = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# # The ID spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1JaWqBcd6jGMV_2eOBq_rAcbXLFKhKHBkcOAuzNjIxbc'

# service = build('sheets', 'v4', credentials=my_credentials)


# # Call the Sheets API
# sheet = service.spreadsheets()


# target_columns = ['D', 'E', 'F', 'G', 'H', 'I']
# target_lines = [*range(2, 1301, 1)]

# for line_idx, line_elmnt in enumerate(target_lines):
#     for col_idx, col_elmnt in enumerate(target_columns):
#         target_cell = target_columns[col_idx] + str(target_lines[line_idx])

#         result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="WorkSheet!" + target_cell).execute()
        
#         values = result.get('values', [])
#         print(values)
#     print("---")


    # [
    #     [
    #         ["D1"],["E1"],["F1"],["G1"],["H1"],["I1"]
    #     ]
    #     [
    #         ["D2"],["E2"],["F2"],["G2"],["H2"],["I2"]
    #     ]
    #     ...
    #     [
    #         ["D1300"],["E1300"],["F1300"],["G1300"],["H1300"],["I1300"]
    #     ]
    # ]


href_cells_list = []
target_columns = ['D', 'E', 'F', 'G', 'H', 'I']
target_lines = [*range(2, 1301, 1)]

# for line_idx, line_elmnt in enumerate(target_lines):
#     intermediary_list = []
#     href_cells_list.append(intermediary_list)
#     for col_idx, col_elmnt in enumerate(target_columns):
#         # print(str(target_lines[line_idx]) + target_columns[col_idx])
#         print(href_cells_list)


for line_idx, line_elmnt in enumerate(target_lines):
    for col_idx, col_elmnt in enumerate(target_columns):
        print(target_columns[col_idx] + str(target_lines[line_idx]))
    print("---")

# #first run
# print(result)
