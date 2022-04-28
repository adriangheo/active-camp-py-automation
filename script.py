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

# browser1.get('https://tstprep.activehosted.com/app/automations?limit=100&offset=100&page=2')
browser1.get('https://tstprep.activehosted.com/app/automations?limit=100')


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


automations  = WebDriverWait(browser1, 5).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.automations_index_automation-list_list-row .automation_title > a'))
)

list_of_automations_data = []

for elmnt in automations :  
    automation_data = []
    automation_data.append(elmnt.get_attribute("href"))
    automation_data.append(elmnt.text)
    list_of_automations_data.append(automation_data)




# 
# 
# 

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

my_credentials = None
my_credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1dAFFThOXIuM-YKtKMEzSgHaD0HPpFLsUamiMZhlrOOk'

service = build('sheets', 'v4', credentials=my_credentials)

# Call the Sheets API
request = service.spreadsheets().values().append(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, 
        range="AC-Automations-List!A2", # where to start from in searching for the first empty row
        valueInputOption="USER_ENTERED", #how the input data should be interepreted. Either a)RAW (will not be parsed) or b)USER_ENTERED (ie. strings may be converted to nubmers, dates, etc)
        insertDataOption="INSERT_ROWS", #how the input data should be inserted. Either a) OVERWRITE or b)INSERT_ROWS
        body={"values":data} #
).execute()

print(request)



request = service.spreadsheets().values().append(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, 
        range="AC-Automations-List!A2", # where to start from in searching for the first empty row
        valueInputOption="USER_ENTERED", #how the input data should be interepreted. Either a)RAW (will not be parsed) or b)USER_ENTERED (ie. strings may be converted to nubmers, dates, etc)
        insertDataOption="INSERT_ROWS", #how the input data should be inserted. Either a) OVERWRITE or b)INSERT_ROWS
        body={"values":list_of_automations_data} #
).execute()