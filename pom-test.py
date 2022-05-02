# Page Object Model Test
from selenium import webdriver

# Test Setup
browser = webdriver.Firefox()
automations_page = AutomationsPage(driver=browser)

# login
automations_page.go()
# automations_page.username_field.input_text('josh@tstprep.com')
# automations_page.password_field.input_text('Z8kkh31SEVHm')
# automations_page.login_btn.click()



# for elmnt in automations_page.list_of_automations:  
#     print(elmnt.get_attribute("href"))
#     print(elmnt.text)
print("line20")
print(type(automations_page.list_of_automations.web_elements))
print("line22")

for elmnt in automations_page.list_of_automations.web_elements:  
    print(elmnt)


# for elmnt in automations_page.list_of_divs:  
#     print(elmnt.get_attribute("href"))
#     print(elmnt.text)

