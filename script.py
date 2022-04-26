# Python Selenium - imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Python GoogleSheetsAPI-imports
from googleapiclient.discovery import build
from google.oauth2 import service_account



# Python Selenium - code
browser1 = webdriver.Chrome()
browser1.get('https://tstprep.activehosted.com/app/automations')

element_usr = WebDriverWait(browser1, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input#user"))
)
element_usr.send_keys('josh@tstprep.com')


element_pas = WebDriverWait(browser1, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input#pass"))
)
element_pas.send_keys('Z8kkh31SEVHm')

element_pas = WebDriverWait(browser1, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='Login']"))
)
element_pas.click()





# Python GoogleSheetsAPI - code
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

my_credentials = None
my_credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1dAFFThOXIuM-YKtKMEzSgHaD0HPpFLsUamiMZhlrOOk'


service = build('sheets', 'v4', credentials=my_credentials)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1!A1:O2").execute()

# #first run
# print(result)

values = result.get('values', [])
print(values)

