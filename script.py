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
from pages.page_with_designer import PageWithDesigner
from pages.page_with_campaign_summary import PageWithCampaignSummary
from pages.page_with_overview import PageWithOverview


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

    page_with_designer = PageWithDesigner(driver=browser, automation_nr=automation_id)
    page_with_designer.go()

    myfile.write("automation-id:" + str(automation_id) + "\t")
    
    time.sleep(2)
    if "/designer" not in browser.current_url:
        myfile.write("\n")
        return False
    
    # 
    # Start of settings modal popup for page_with_designer
    open_modal = page_with_designer.btn_open_settings_modal
    open_modal.click()

    subject_text = page_with_designer.subject_from_modal.field_value
    myfile.write("" +  subject_text + "\t")
    print("subject_text: " + subject_text)

    preheader_text = page_with_designer.preheader_from_modal.field_value
    myfile.write("" +  preheader_text + "\t")
    print("preheader_text: " + preheader_text)

    sender_name = page_with_designer.sender_name_from_modal.field_value
    myfile.write("" +  sender_name + "\t")
    print("sender_text: " + sender_name)   

    sender_email = page_with_designer.sender_email_from_modal.field_value
    myfile.write("" +  sender_email + "\t")
    print("sender_email: " + sender_email)   

    reply_email = page_with_designer.reply_email_from_modal.field_value
    myfile.write("" +  reply_email + "\t")
    print("reply_email: " + reply_email)   

    close_modal = page_with_designer.btn_close_settings_modal
    close_modal.click()
    # # print("input() function call. Please hit Enter inside the terminal")
    # # input()
    # End of settings modal popup for page_with_designer
    # 


    # 
    # Opening page_with_campaign_summary
    next_btn = page_with_designer.btn_to_campaign_summary
    next_btn.click()
    # # print("input() function call. Please hit Enter inside the terminal")
    # # input()

    page_with_campaign_summary = PageWithCampaignSummary(driver=browser)

    # swith-01
    switch_btn1 = page_with_campaign_summary.switch_btn_read_tracking
    bnt_value1 = switch_btn1.switch_btn_value
    myfile.write(bnt_value1)
    print('switch is ' + bnt_value1)
    
    open_read_tracking_modal = page_with_campaign_summary.btn_read_tracking_open_modal
    open_read_tracking_modal.click()

    o_r_automations_text = page_with_campaign_summary.o_r_field_from_modal.text
    myfile.write("" +  o_r_automations_text + "\t")
    print("" + o_r_automations_text)
    
    close_read_tracking_modal = page_with_campaign_summary.btn_read_tracking_close_modal
    close_read_tracking_modal.click() 


    # swith-02
    switch_btn2 = page_with_campaign_summary.switch_btn_link_tracking
    bnt_value2 = switch_btn2.switch_btn_value
    myfile.write(bnt_value2)
    print('switch is ' + bnt_value2)

    open_link_tracking_modal = page_with_campaign_summary.btn_link_tracking_open_modal
    open_link_tracking_modal.click()

    cstmize_lnk_traking_urls = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody[id='tlinkshtmllist'] .text_left"))
    )
    texts = ""
    for matched_element in cstmize_lnk_traking_urls:
        text = matched_element.text
        texts += " "
        texts += text
    print(texts)

    close_link_tracking_modal = page_with_campaign_summary.btn_link_tracking_close_modal
    close_link_tracking_modal.click()


    # swith-03
    switch_btn3 = page_with_campaign_summary.switch_btn_reply_tracking
    bnt_value3 = switch_btn3.switch_btn_value
    myfile.write(bnt_value3)
    print('switch is ' + bnt_value3)


    # swith-04
    switch_btn3 = page_with_campaign_summary.switch_btn_analytics_tracking
    bnt_value3 = switch_btn3.switch_btn_value
    myfile.write(bnt_value3)
    print('switch is ' + bnt_value3)

    open_analytics_tracking_modal = page_with_campaign_summary.btn_analytics_tracking_open_modal
    open_analytics_tracking_modal.click()


    analytics_campaing_name = page_with_campaign_summary.analytics_field_from_modal.field_value
    myfile.write("" +  analytics_campaing_name + "\t")
    print("" + analytics_campaing_name)


    # # Start of Overview
    page_with_overview = PageWithOverview(driver=browser, automation_nr=automation_id)
    page_with_overview.go()

    total_sent =  page_with_overview.totalsent
    myfile.write("" +  total_sent + "\t")
    print("total_sent: " + total_sent)

    revenue =  page_with_overview.revenue #this is used later
    # # End of Overview
    #

    #
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
for index in range(1154, 1155, 1):
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
