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

google_api = GoogleApi()

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



print(google_api.target_cells)

for sublist in google_api.target_cells:
    for cell in sublist:
         print(cell)
    print('---')


# for line_idx, line_elmnt in enumerate(target_lines):
#     for col_idx, col_elmnt in enumerate(target_columns):
#         print(target_columns[col_idx] + str(target_lines[line_idx]))
#     print("---")

# #first run
# print(result)
