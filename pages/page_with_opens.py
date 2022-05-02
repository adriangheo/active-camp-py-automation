from selenium.webdriver.common.by import By

from .base_element import BaseElement

class PageWithOpens(object):
    url = None

    def __init__(self, driver, automation_nr):
        self.driver = driver
        self.url ="https://thethirdwave.activehosted.com/report/#/campaign/" + str(automation_nr) + "/opens"
        
    def go(self):
        self.driver.get(self.url)



    @property
    def prop_total_number(self):
        locator = (By.CSS_SELECTOR, '#open_total_t')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    def prop_unique_opens(self):
        locator = (By.CSS_SELECTOR, '#open_total_t')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])