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

# google_api = GoogleApi()

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
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="WorkSheet!D1:I1300").execute()

# # #first run
# # print(result)

# values = result.get('values', [])

# f = open("demofile2.txt", "a")
# f.write(str(values))
# f.close()


# print(values)



file1 = open('list-of-links.txt', 'r')

Lines = file1.readlines()

for line in Lines:
    print(line)