from selenium.webdriver.common.by import By

from .base_element import BaseElement

class PageWithOverview(object):
    url = None

    def __init__(self, driver, automation_nr):
        self.driver = driver
        self.url ="https://thethirdwave.activehosted.com/report/#/campaign/" + str(automation_nr) + "/overview"
        
    def go(self):
        self.driver.get(self.url)



    @property
    def totalsent(self):
        locator = (By.CSS_SELECTOR, 'span.sentto')
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    def total_revenue(self):
        locator = (By.XPATH, "//span[contains(@class, 'panel-summary-currency')][1]")
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])