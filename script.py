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


list_of_automations  = WebDriverWait(browser1, 5).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.automations_index_automation-list_list-row .automation_title > a'))
)


for elmnt in list_of_automations :  
    print(elmnt.get_attribute("href"))
    print(elmnt.text)

# first_link = list_of_automations[0].get_attribute("href")

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

data = [["8/1/2020","Joe3","MidWest","IL","New Brand",563.65,342.45]]

# Call the Sheets API
request = service.spreadsheets().values().append(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, 
        range="AC-Automations-List!A1:G1", # where to start from in searching for the first empty row
        valueInputOption="USER_ENTERED", #how the input data should be interepreted. Either a)RAW (will not be parsed) or b)USER_ENTERED (ie. strings may be converted to nubmers, dates, etc)
        insertDataOption="INSERT_ROWS", #how the input data should be inserted. Either a) OVERWRITE or b)INSERT_ROWS
        body={"values":data} #
).execute()

print(request)
