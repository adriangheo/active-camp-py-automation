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


def traversePages(page_number):
    page_with_overview = "https://thethirdwave.activehosted.com/report/#/campaign/" +  str(page_number) + "/overview"
    page_with_opens = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(page_number) + "/opens"
    page_with_clicks = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(page_number) + "/clicks"
    page_with_preview = "https://thethirdwave.activehosted.com/preview.php?c=" + str(page_number) + "&preview"
    page_with_designer = "https://thethirdwave.activehosted.com/campaign/" + str(page_number) + "/designer"
    page_with_unsubscribes = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(page_number) + "/unsubscribes"
    page_with_bounces = "https://thethirdwave.activehosted.com/report/#/campaign/" + str(page_number) + "/bounces"

    browser.get(page_with_designer)

    try:
        btn_temp_settings = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.temp-settings'))
        )
        btn_temp_settings.click()

        subject_text = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input[name="subject"]'))
        ).get_attribute('value')
        target_values_list.append(subject_text)

        print("subject_text: " + subject_text)

        preheader_text = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input[name="preheader_text"]'))
        ).get_attribute('value')
        if(preheader_text == ""):
            preheader_text = "n/a"
        target_values_list.append(preheader_text)
        print("preheader_text: " + preheader_text)

        sender_name = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input[name="fromname_display"]'))
        ).get_attribute('value')
        target_values_list.append(sender_name)
        print("sender_text: " + sender_name)

        sender_email = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input[name="fromemail_display"]'))
        ).get_attribute('value')
        target_values_list.append(sender_email)
        print("sender_email: " + sender_email)

        reply_email = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input[name="reply2"]'))
        ).get_attribute('value')
        if(reply_email == ""):
            reply_email = "n/a"
        target_values_list.append(reply_email)
        print("reply_email: " + reply_email)

        popup_close_btn = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="template-setting"] a[class="close"]'))
        )
        popup_close_btn.click()

        next_btn = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.ac_button.next.alt1.alt2'))
        )
        next_btn.click()

        # swith-01
        read_tracking_switch = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-section="read_tracking"]'))
        )
        if 'switch_on' in read_tracking_switch.get_attribute('class').split():
            print('switch is on')
            target_values_list.append("ON")
        else:
            target_values_list.append("OFF")
            print('switch is off')

        open_read_automations = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.open-read-automations'))
        )
        open_read_automations.click()

        O_R_Automations_text = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.text_left.ac_fs-shmedium'))
        ).text
        target_values_list.append(O_R_Automations_text)
        print("O_R_Automations_text: " + O_R_Automations_text)

        popup_close_btn = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"When this message is opened")]/preceding-sibling::a[1]'))
        )
        popup_close_btn.click()

        # swith-02
        link_tracking_switch = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-section="link_tracking"]'))
        )
        if 'switch_on' in link_tracking_switch.get_attribute('class').split():
            print('switch is on')
            target_values_list.append("ON")
        else:
            target_values_list.append("OFF")
            print('switch is off')

        open_cstmize_lnk_traking = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='options-row link_tracking']/div[position()=3]/a"))
        )
        open_cstmize_lnk_traking.click()

        cstmize_lnk_traking_urls = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody[id='tlinkshtmllist'] .text_left"))
        )
        # print("cstmize_lnk_traking_urls: " + cstmize_lnk_traking_urls)  # error can only concatenate strings to strings, not arrays
        texts = []
        for matched_element in cstmize_lnk_traking_urls:
            text = matched_element.text
            texts.append(text)

        target_values_list.append(texts)

        popup_close_btn = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Customize Link Tracking")]/preceding-sibling::a[1]'))
        )
        popup_close_btn.click()

        # swith-03
        link_tracking_switch = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-section="reply_tracking"]'))
        )

        if 'switch_on' in link_tracking_switch.get_attribute('class').split():
            print('switch is on')
            target_values_list.append("ON")
        else:
            target_values_list.append("OFF")
            print('switch is off')

        # swith-04
        google_analytics_switch = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-section="analytics"]'))
        )
        if 'switch_on' in google_analytics_switch.get_attribute('class').split():
            print('switch is on')
            target_values_list.append("ON")
        else:
            target_values_list.append("OFF")
            print('switch is off')

        open_cstmize_lnk_traking = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='options-row analytics']/div[contains(@class,'options-link')]//a"))
        )
        open_cstmize_lnk_traking.click()

        analytics_campaign_name = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="analytics_campaign_name"]'))
        ).get_attribute("value")
        target_values_list.append(analytics_campaign_name)
        print("analytics_campaign_name: " + analytics_campaign_name)

        # End of Campaign Summary
        #

        #
        # Start of Overview
        browser.get(page_with_overview)

        total_sent = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.sentto'))
        ).text
        target_values_list.append(total_sent)
        print("total_sent: " + total_sent)

        revenue = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'panel-summary-currency')][1]"))
        ).text #this is added later in the   target_values_list
        # End of Overview
        #

        #
        # Start of page_with_opens
        browser.get(page_with_opens)
        time.sleep(1) # necesary because total_open_links field initially loads with the value 0
        total_opens = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#open_total_t'))
        ).text
        target_values_list.append(total_opens)
        print("total_opens: " + total_opens)

        unique_opens = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#open_unique_t'))
        ).text
        target_values_list.append(unique_opens)
        print("unique_opens: " + unique_opens)
        # End of page_with_opens
        #

        #
        # Start of page_with_links
        browser.get(page_with_clicks)
        time.sleep(1) # necesary because total_open_links field initially loads with the value 0
        total_link_clicks = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#link_total_t'))
        ).text
        target_values_list.append(total_link_clicks)
        print("total_link_clicks: " + total_link_clicks)

        unique_link_clicks = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#link_unique_t'))
        ).text
        target_values_list.append(unique_link_clicks)
        print("unique_link_clicks: " + unique_link_clicks)
        # End of page_with_links
        #

        #
        # Start of page_with_unsubscribes
        browser.get(page_with_unsubscribes)
        time.sleep(1) # necesary because total_open_links field initially loads with the value 0
        total_unsubscribes = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#unsubscribe_total_t'))
        ).text
        target_values_list.append(total_unsubscribes)
        print("total_unsubscribes: " + total_unsubscribes)
        # End of page_with_unsubscribes
        #

        #
        # Start of page_with_bounces
        browser.get(page_with_bounces)
        time.sleep(1) # necesary because total_open_links field initially loads with the value 0
        total_bounces = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#bounce_total_t'))
        ).text
        target_values_list.append(total_bounces)
        print("total_bounces: " + total_bounces)
        # End of page_with_bounces

        target_values_list.append(revenue)
    except TimeoutException as ex:
        print("Exception has been thrown. " + str(ex))
    finally:
        print("went though one try block")


# 1154, and 1154 are ok, but it breaks at 1155
for index in range(1155, 1159, 1):
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
