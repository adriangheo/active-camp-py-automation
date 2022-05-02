# Python Selenium - imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Python GoogleSheetsAPI-imports
from googleapiclient.discovery import build
from google.oauth2 import service_account

from pages.automations_page import AutomationsPage
from pages.login_page import LoginPage
from pages.page_with_designer import PaveWithDesigner
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

def check_exists_by_css_selector(cssselector):
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, cssselector))
        )
    except Exception:
        print("element was NOT found")
        return False
    else:
        print("element was found")
    return True

myfile = None


def traversePages(automation_id):
    # page_with_overview = "https://thethirdwave.activehosted.com/report/#/campaign/" +  str(automation_id) + "/overview"
    # page_with_opens = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(automation_id) + "/opens"
    # page_with_clicks = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(automation_id) + "/clicks"
    # page_with_preview = "https://thethirdwave.activehosted.com/preview.php?c=" + str(automation_id) + "&preview"
    # page_with_designer = "https://thethirdwave.activehosted.com/campaign/" + str(automation_id) + "/designer"
    # page_with_unsubscribes = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(automation_id) + "/unsubscribes"
    # page_with_bounces = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(automation_id) + "/bounces"

    page_with_designer = PaveWithDesigner(driver=browser, automation_nr=automation_id)
    page_with_designer.go()

    myfile.write("automation-id:" + str(automation_id) + "\t")
    
    time.sleep(2)
    if "/designer" not in browser.current_url:
        myfile.write("\n")
        return False
    
    page_with_designer.btn_open_settings_modal.click()

    subject_text = page_with_designer.subject_from_modal.field_value
    myfile.write("" +  subject_text + "\t")
    print("subject_text: " + subject_text)

    preheader_text = page_with_designer.preheader_from_modal.field_value
    myfile.write("" +  preheader_text + "\t")
    print("preheader_text: " + preheader_text)

    # preheader_text = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located(
    #         (By.CSS_SELECTOR, 'input[name="preheader_text"]'))
    # ).get_attribute('value')
    # if(preheader_text == ""):
    #     preheader_text = "n/a"
    # myfile.write("" +  preheader_text + "\t")
    # print("preheader_text: " + preheader_text)

    # sender_name = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located(
    #         (By.CSS_SELECTOR, 'input[name="fromname_display"]'))
    # ).get_attribute('value')
    # myfile.write("" +  sender_name + "\t")
    # print("sender_text: " + sender_name)

    # sender_email = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located(
    #         (By.CSS_SELECTOR, 'input[name="fromemail_display"]'))
    # ).get_attribute('value')
    # myfile.write("" +  sender_email + "\t")
    # print("sender_email: " + sender_email)

    # reply_email = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located(
    #         (By.CSS_SELECTOR, 'input[name="reply2"]'))
    # ).get_attribute('value')
    # if(reply_email == ""):
    #     reply_email = "n/a"
    # myfile.write("" +  reply_email + "\t")
    # print("reply_email: " + reply_email)

    # popup_close_btn = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="template-setting"] a[class="close"]'))
    # ) 
    # popup_close_btn.click()

    # # print("input() function call. Please hit Enter inside the terminal")
    # # input()


    # next_btn = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, '.ac_button.next.alt1.alt2'))
    # )
    # next_btn.click()

    # # print("input() function call. Please hit Enter inside the terminal")
    # # input()


    # if(check_exists_by_css_selector('[data-section="read_tracking"]')):
    #     # swith-01
    #     read_tracking_switch = WebDriverWait(browser, 5).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-section="read_tracking"]'))
    #     )
    #     # print("input() function call. Please hit Enter inside the terminal")
    #     # input()



    #     if 'switch_on' in read_tracking_switch.get_attribute('class').split():
    #         myfile.write("ON\t")
    #         print('switch is on')
    #     else:
    #         myfile.write("OFF\t")
    #         print('switch is off')


    #     open_read_automations = WebDriverWait(browser, 5).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, '.open-read-automations'))
    #     )
    #     open_read_automations.click()

    #     O_R_Automations_text = WebDriverWait(browser, 5).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, '.text_left.ac_fs-shmedium'))
    #     ).text
    #     myfile.write("" +  O_R_Automations_text + "\t")
    #     print("" + O_R_Automations_text)


    #     popup_close_btn = WebDriverWait(browser, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"When this message is opened")]/preceding-sibling::a[1]'))
    #     )
    #     popup_close_btn.click()


    #     # swith-02
    #     link_tracking_switch = WebDriverWait(browser, 5).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-section="link_tracking"]'))
    #     )



    #     if 'switch_on' in link_tracking_switch.get_attribute('class').split():
    #         myfile.write("ON\t")
    #         print('switch is on')
    #     else:
    #         myfile.write("OFF\t")
    #         print('switch is off')

    #     open_cstmize_lnk_traking = WebDriverWait(browser, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[@class='options-row link_tracking']/div[position()=3]/a"))
    #     )
    #     open_cstmize_lnk_traking.click()

    #     cstmize_lnk_traking_urls = WebDriverWait(browser, 5).until(
    #         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody[id='tlinkshtmllist'] .text_left"))
    #     )
    #     # print("cstmize_lnk_traking_urls: " + cstmize_lnk_traking_urls)  # error can only concatenate strings to strings, not arrays
    #     texts = ""
    #     for matched_element in cstmize_lnk_traking_urls:
    #         text = matched_element.text
    #         texts += " "
    #         texts += text


    #     myfile.write("" +  texts + "\t")

    #     popup_close_btn = WebDriverWait(browser, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Customize Link Tracking")]/preceding-sibling::a[1]'))
    #     )
    #     popup_close_btn.click()

    #     # swith-03
    #     link_tracking_switch = WebDriverWait(browser, 5).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-section="reply_tracking"]'))
    #     )

    #     if 'switch_on' in link_tracking_switch.get_attribute('class').split():
    #         myfile.write("ON\t")
    #         print('switch is on')
    #     else:
    #         print('switch is off')
    #         myfile.write("OFF\t")

    #     # swith-04
    #     google_analytics_switch = WebDriverWait(browser, 5).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-section="analytics"]'))
    #     )
    #     if 'switch_on' in google_analytics_switch.get_attribute('class').split():
    #         myfile.write("ON\t")
    #         print('switch is on')
    #     else:
    #         myfile.write("OFF\t")
    #         print('switch is off')

    #     open_cstmize_lnk_traking = WebDriverWait(browser, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[@class='options-row analytics']/div[contains(@class,'options-link')]//a"))
    #     )
    #     open_cstmize_lnk_traking.click()

    #     analytics_campaign_name = WebDriverWait(browser, 5).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="analytics_campaign_name"]'))
    #     ).get_attribute("value")
    #     myfile.write("" +  analytics_campaign_name + "\t")
    #     print("analytics_campaign_name: " + analytics_campaign_name)
    # else:
    #     myfile.write("\t\t\t\t\t\t\t\t")
    #     # End of Campaign Summary
    #     #

    # myfile.write("\t\t")
    # #
    # # Start of Overview
    # browser.get(page_with_overview)

    # total_sent = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.sentto'))
    # ).text
    # myfile.write("" +  total_sent + "\t")
    # print("total_sent: " + total_sent)

    # revenue = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'panel-summary-currency')][1]"))
    # ).text #this is used later
    # # End of Overview
    # #

    # #
    # # Start of page_with_opens
    # browser.get(page_with_opens)
    # time.sleep(1) # necesary because total_open_links field initially loads with the value 0
    # total_opens = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, '#open_total_t'))
    # ).text
    # myfile.write("" +  total_opens + "\t\t")
    # print("total_opens: " + total_opens)

    # unique_opens = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, '#open_unique_t'))
    # ).text
    # myfile.write("" +  unique_opens + "\t\t")
    # print("unique_opens: " + unique_opens)
    # # End of page_with_opens
    # #

    # #
    # # Start of page_with_links
    # browser.get(page_with_clicks)
    # time.sleep(1) # necesary because total_open_links field initially loads with the value 0
    # total_link_clicks = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, '#link_total_t'))
    # ).text
    # myfile.write("" +  total_link_clicks + "\t\t")
    # print("total_link_clicks: " + total_link_clicks)

    # unique_link_clicks = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, '#link_unique_t'))
    # ).text
    # myfile.write("" +  unique_link_clicks + "\t\t")
    # print("unique_link_clicks: " + unique_link_clicks)
    # # End of page_with_links
    # #

    # #
    # # Start of page_with_unsubscribes
    # browser.get(page_with_unsubscribes)
    # time.sleep(1) # necesary because total_open_links field initially loads with the value 0
    # total_unsubscribes = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, '#unsubscribe_total_t'))
    # ).text
    # myfile.write("" +  total_unsubscribes + "\t\t")
    # print("total_unsubscribes: " + total_unsubscribes)
    # # End of page_with_unsubscribes
    # #

    # #
    # # Start of page_with_bounces
    # browser.get(page_with_bounces)
    # time.sleep(1) # necesary because total_open_links field initially loads with the value 0
    # total_bounces = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, '#bounce_total_t'))
    # ).text
    # myfile.write("" +  total_bounces + "\t\t")
    # print("total_bounces: " + total_bounces)
    # # End of page_with_bounces

    # myfile.write("" +  revenue + "")
    # myfile.write("\n")


# 1154, and 1154 are ok, but it breaks at 1155
for index in range(1154, 1160, 1):
    myfile = open("output.txt", 'a')
    traversePages(index)
    myfile.close()





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
