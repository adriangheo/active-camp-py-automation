# Page Object Model Test
from selenium import webdriver
from pages.login_page import LoginPage

# Test Setup
browser = webdriver.Firefox()

login_page = LoginPage(driver=browser)
login_page.go()
login_page.username_field.input_text('josh@tstprep.com')
login_page.password_field.input_text('Z8kkh31SEVHm')
login_page.login_btn.click()







