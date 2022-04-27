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
browser1.get('https://tstprep.activehosted.com')


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


# element_to_be_removed = browser2.find_element_by_class_name('classname')
# driver.execute_script("""
# var element = arguments[0];
# element.parentNode.removeChild(element);
# """, element)


# 
# 
# new tabs
# 
# 


# # the code bellow opens the link in the new tabs
# browser1.execute_script('window.open("' + first_link + '", "_blank");')

# handles = browser1.window_handles

# #TABS switch
# # keep note that if you open more than 2 tabs, these window handles 
# # are not going to be in the same order that we called them in, 
# browser1.switch_to.window(handles[1])

# # browser1.execute_script('window.open("https://techstepacademy.com/training-ground", "_blank");')
# # browser1.execute_script('window.open("http://google.com", "_blank");')
# # browser1.execute_script('window.open("http://yahoo.com", "_blank");')
# # browser1.execute_script('window.open("http://google.com", "_blank");')

# viewemails_btn = WebDriverWait(browser1, 5).until(     EC.presence_of_element_located((By.CSS_SELECTOR, ".viewemails .ac_button")) )
# viewemails_btn.click()


# browser1.find_element(By.CSS_SELECTOR, ".viewemails .ac_button")  



# viewemails_btn1 = WebDriverWait(browser1, 2).until(        EC.presence_of_element_located((By.CSS_SELECTOR, ".viewemails .ac_button")) )
# viewemails_btn.execute_script("arguments[0].click();",product)