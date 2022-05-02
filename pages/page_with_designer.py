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
