from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_elements import BaseElements
from .base_page import BasePage


class PageWithCampaignSummary(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def switch_btn_open_read_tracking(self):
        locator = (By.CSS_SELECTOR, '[data-section="read_tracking"]')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])
