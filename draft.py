# Python Selenium - imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Python GoogleSheetsAPI-imports
from googleapiclient.discovery import build
from google.oauth2 import service_account

from pages.automations_page import AutomationsPage
from pages.login_page import LoginPage
from apis.google_api import GoogleApi

import time 


# Python Selenium - code
browser = webdriver.Chrome()

login_page = LoginPage(driver=browser)

login_page.go()

login_page.username_field.input_text('marian@dacianempire.com')
login_page.password_field.input_text('daTIVoINgerymPolIzAR')
login_page.login_btn.click()

# browser.get('https://thethirdwave.activehosted.com/report/#/campaign/1/overview')

currentUrl = browser.current_url
wait = WebDriverWait(browser, 4)
flagUrlNonExistant = False

my_range = range(1, 50, 1)
all_overview_uls_list = []

for n in my_range:
    # browser.get("https://thethirdwave.activehosted.com/report/#/campaign/"+ str(n) +"/overview")
    all_overview_uls_list.append("https://thethirdwave.activehosted.com/report/#/campaign/"+ str(n) +"/overview")

index_current_url = 1

def waitForUrlChange():
    global currentUrl
    WebDriverWait(browser, 8).until(EC.url_changes(currentUrl)) 
    currentUrl = browser.current_url
    
for index in range(50):
    if(currentUrl == "https://thethirdwave.activehosted.com/report/#/campaign"):
        index_current_url = index_current_url + 1
        browser.get(all_overview_uls_list[index_current_url])
    waitForUrlChange()


# if(browser.current_url == 'https://thethirdwave.activehosted.com/report/#/campaign'):









    


