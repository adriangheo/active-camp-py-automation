# Page Object Model Test
from selenium import webdriver
from pages.automations_page import AutomationsPage

# Test Setup
browser = webdriver.Firefox()
automations_page = AutomationsPage(driver=browser)

# login
automations_page.go()
automations_page.username_field.input_text('josh@tstprep.com')
automations_page.password_field.input_text('Z8kkh31SEVHm')
automations_page.login_btn.click()







