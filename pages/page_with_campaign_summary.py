from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_elements import BaseElements
from .base_page import BasePage

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
    def link_tracking_urls(self):
        elements = WebDriverWait(
            self.driver,10).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody[id='tlinkshtmllist'] .text_left")))
        print(elements)

WebDriverWait(browser, 8).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.sentence-and-translations.md-whiteframe-1dp.flex")))

