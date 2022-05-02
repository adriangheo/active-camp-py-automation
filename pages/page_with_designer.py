from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_elements import BaseElements
from .base_page import BasePage


class PaveWithDesigner(object):
    url = None

    def __init__(self, driver, automation_nr):
        self.driver = driver
        self.url ="https://thethirdwave.activehosted.com/campaign/" + str(automation_nr) + "/designer"
        
    def go(self):
        self.driver.get(self.url)


    @property
    def btn_open_settings_modal(self):
        locator = (By.CSS_SELECTOR, '.temp-settings')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    def subject_from_modal(self):
        locator = (By.CSS_SELECTOR, 'input[name="subject"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    def preheader_from_modal(self):
        locator = (By.CSS_SELECTOR, 'input[name="preheader_text"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    def sender_name_from_modal(self):
        locator = (By.CSS_SELECTOR, 'input[name="fromname_display"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    def sender_email_from_modal(self):
        locator = (By.CSS_SELECTOR, 'input[name="fromemail_display"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    def reply_email_from_modal(self):
        locator = (By.CSS_SELECTOR, 'input[name="reply2"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    def btn_close_settings_modal(self):
        locator = (By.CSS_SELECTOR, 'div[id="template-setting"] a[class="close"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])