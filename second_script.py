# Python Selenium - imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException        


# Python GoogleSheetsAPI-imports
from googleapiclient.discovery import build
from google.oauth2 import service_account

from pages.login_page import LoginPage
from apis.google_api import GoogleApi

import time


# Python Selenium - code
browser = webdriver.Chrome()

login_page = LoginPage(driver=browser)

# browser.get('https://tstprep.activehosted.com/app/automations?limit=100&offset=100&page=2')
login_page.go()

login_page.username_field.input_text('marian@dacianempire.com')
login_page.password_field.input_text('daTIVoINgerymPolIzAR')
login_page.login_btn.click()

target_values_list = []


def check_exists_by_css(cssselector):
    try:
        browser.find_element_by_css_selector(cssselector)
    except NoSuchElementException:
        return False
    return True



def check_exists_by_css_selector(cssselector):
    try:
        element = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, cssselector))
        )
    except TimeoutException:
        print("element was NOT found")
        return False
    else:
        print("element was found")
    return element


def traversePages(page_number):
    page_with_overview = "https://thethirdwave.activehosted.com/report/#/campaign/" +  str(page_number) + "/overview"
    page_with_opens = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(page_number) + "/opens"
    page_with_clicks = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(page_number) + "/clicks"
    page_with_preview = "https://thethirdwave.activehosted.com/preview.php?c=" + str(page_number) + "&preview"
    page_with_designer = "https://thethirdwave.activehosted.com/campaign/" + str(page_number) + "/designer"
    page_with_unsubscribes = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(page_number) + "/unsubscribes"
    page_with_bounces = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(page_number) + "/bounces"

    browser.get(page_with_designer)

    check_exists_by_css_selector('.ac_buttonnext')






# 1154, and 1154 are ok, but it breaks at 1155
for index in range(1157, 1158, 1):
    target_values_list.append("-----")
    traversePages(index)


# links_file = open('list-of-links.txt', 'r')
# lines = links_file.readlines()

# for line in lines:
#     if "overview" in line:
#         print("--------------")
#         print("found overview")

#         total_sent = browser.find_element(By.CSS_SELECTOR, 'span.sentto')


#     elif "opens" in line:
#         print("found opens")
#     elif "clicks" in line:
#         print("found clicks")
#     elif "preview" in line:
#         print("found preview")
#     elif "designer" in line:
#         print("found designer")
#     elif "summary" in line:
#         print("found summary")


#
#
#


#
#
#

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
