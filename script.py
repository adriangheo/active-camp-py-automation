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




# Python Selenium - code
browser = webdriver.Chrome()

login_page = LoginPage(driver=browser)

# browser.get('https://tstprep.activehosted.com/app/automations?limit=100&offset=100&page=2')
login_page.go()

login_page.username_field.input_text('marian@dacianempire.com')
login_page.password_field.input_text('daTIVoINgerymPolIzAR')
login_page.login_btn.click()


browser.get('https://thethirdwave.activehosted.com/report/#/campaign/1153/overview')

target_values_list = []

total_sent = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.sentto'))
).text
target_values_list.append(total_sent)


def ac_camp_nr():
    str_url = browser.current_url
    start = str_url.find("campaign/") + len("campaign/")
    end = str_url.find("/overview")
    campaign_nr = str_url[start:end]
    return campaign_nr

camp_nr = ac_camp_nr()

opens_link = "https://thethirdwave.activehosted.com/report/#/campaign/"+ camp_nr +"/opens"
clicks_link = "https://thethirdwave.activehosted.com/report/#/campaign/"+ camp_nr +"/clicks"
preview_link = "https://thethirdwave.activehosted.com/preview.php?c="+ camp_nr + "&preview"
designer_link = "https://thethirdwave.activehosted.com/campaign/" + camp_nr + "/designer"


browser.get(designer_link)

btn_temp_settings = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.temp-settings'))
)
btn_temp_settings.click()


subject_text =  WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="subject"]'))
).get_attribute('value')
print("subject_text: " + subject_text)


preheader_text = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="preheader_text"]'))
).get_attribute('value')
if(preheader_text == ""):
    preheader_text = "n/a"
print("preheader_text: " + preheader_text)


sender_name = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="fromname_display"]'))
).get_attribute('value')
print("sender_text: " + sender_name)


sender_email = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="fromemail_display"]'))
).get_attribute('value')
print("sender_email: " + sender_email)


reply_email = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="reply2"]'))
).get_attribute('value')
if(reply_email == ""):
    reply_email = "n/a"

print("reply_email: " + reply_email)

popup_close_btn = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="template-setting"] a[class="close"]'))
)
popup_close_btn.click()

next_btn = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.ac_button.next.alt1.alt2'))
)
next_btn.click()




read_tracking_switch = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-section="read_tracking"]'))
)

if 'switch_on' in read_tracking_switch.get_attribute('class').split():
    print('switch is on')
else:
    print('switch is off')


open_read_automations = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.open-read-automations'))
)
open_read_automations.click()

O_R_Automations_text = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.XPATH, '.modal-dialog tbody'))
)




link_tracking_switch = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-section="link_tracking"]'))
)

if 'switch_on' in link_tracking_switch.get_attribute('class').split():
    print('switch is on')
else:
    print('switch is off')


google_analytics_switch = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-section="analytics"]'))
)

if 'switch_on' in google_analytics_switch.get_attribute('class').split():
    print('switch is on')
else:
    print('switch is off')



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
