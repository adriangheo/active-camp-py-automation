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

from pages.login_page import LoginPage

google_api = GoogleApi()

# Python Selenium - code
browser1 = webdriver.Chrome()

login_page = LoginPage(driver=browser1)

# browser1.get('https://tstprep.activehosted.com/app/automations?limit=100&offset=100&page=2')
login_page.go()

login_page.username_field.input_text('josh@tstprep.com')
login_page.password_field.input_text('Z8kkh31SEVHm')
login_page.login_btn.click()


browser1.get('https://tstprep.activehosted.com/app/automations?limit=100')

automations  = WebDriverWait(browser1, 5).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.automations_index_automation-list_list-row .automation_title > a'))
)

list_of_automations_data = []

for elmnt in automations :  
    automation_data = []
    automation_data.append(elmnt.get_attribute("href"))
    automation_data.append(elmnt.text)
    list_of_automations_data.append(automation_data)


# xpath
#  $x('//ul[@class="pager-wrap"]/li[@class="active"]/following-sibling::li[1]')
#  $x('//ul[@class="pager-wrap"]/li[@class="active"]/following-sibling::li[1] [not(@class="next")]')
#  $x('//ul[@class="pager-wrap"]/li[@class="active"]/following-sibling::li[1][not(contains(@class, "disabled"))]')





google_api.appendToActCampAutomationsSheet(list_of_automations_data)


