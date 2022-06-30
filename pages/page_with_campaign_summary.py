from selenium.webdriver.common.by import By

from .base_element import BaseElement


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageWithCampaignSummary(object):
    def __init__(self, driver):
        self.driver = driver

    #switch btn1 
    @property
    def switch_btn_read_tracking(self):
        locator = (By.CSS_SELECTOR, '[data-section="read_tracking"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    def btn_read_tracking_open_modal(self):
        locator = (By.CSS_SELECTOR, '.open-read-automations')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])
    
    @property
    def o_r_field_from_modal(self):
        locator = (By.CSS_SELECTOR, '.text_left.ac_fs-shmedium')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    def btn_read_tracking_close_modal(self):
        locator = (By.CSS_SELECTOR, '[id="link_series0"] [class="close"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])


    #switch btn2
    @property
    def switch_btn_link_tracking(self):
        locator = (By.CSS_SELECTOR, '[data-section="link_tracking"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])
    

    @property
    def btn_link_tracking_open_modal(self):
        locator = (By.XPATH, "//div[@class='options-row link_tracking']/div[position()=3]/a")
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])
   

    @property
    def btn_link_tracking_close_modal(self):
        locator = (By.XPATH, '//*[contains(text(),"Customize Link Tracking")]/preceding-sibling::a[1]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])
   
  
    #switch btn3
    @property
    def switch_btn_reply_tracking(self):
        locator = (By.CSS_SELECTOR, '[data-section="reply_tracking"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    #switch btn4
    @property
    def switch_btn_analytics_tracking(self):
        locator = (By.CSS_SELECTOR, '[data-section="analytics"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    def btn_analytics_tracking_open_modal(self):
        locator = (By.XPATH, "//div[@class='options-row analytics']/div[contains(@class,'options-link')]//a")
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])
    
    @property
    def analytics_field_from_modal(self):
        locator = (By.CSS_SELECTOR, 'input[name="analytics_campaign_name"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])


        
    @property
    def prop_automation_name(self):
        locator = (By.CSS_SELECTOR, 'input[name="campaign_name"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])