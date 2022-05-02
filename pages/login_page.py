from selenium.webdriver.common.by import By

from .base_element import BaseElement


class LoginPage(object):
    url = 'https://thethirdwave.activehosted.com/'

    def __init__(self, driver):
        self.driver = driver
        
    def go(self):
        self.driver.get(self.url)

    @property
    # def courses_for_duolingo(self):
    def username_field(self):
        locator = (By.CSS_SELECTOR, "input#user")
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    # def private_lessons_for_duolingo(self):
    def password_field(self):
        locator = (By.CSS_SELECTOR, "input#pass")
        return BaseElement(
            driver = self.driver, 
            by = locator[0],
            value = locator[1])

    @property
    # def score_evaluation_for_duolingo(self):
    def login_btn(self):
        locator = (By.CSS_SELECTOR, "input[value='Login']")
        return BaseElement(driver = self.driver, 
            by = locator[0],
            value = locator[1])


