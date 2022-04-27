from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_elements import BaseElements
from .base_page import BasePage
from .locator import Locator

class AutomationsPage(BasePage):
    url = 'https://tstprep.activehosted.com'

    @property
    # def courses_for_duolingo(self):
    def username_field(self):
        lctr = Locator(By.CSS_SELECTOR, "input#user")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    # def private_lessons_for_duolingo(self):
    def password_field(self):
        lctr = Locator(By.CSS_SELECTOR, "input#pass")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    # def score_evaluation_for_duolingo(self):
    def login_btn(self):
        lctr = Locator(By.CSS_SELECTOR, "input[value='Login']")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def list_of_automations(self):
        lctr = Locator(By.CSS_SELECTOR, ".inner.flex.flex-column.p-4")
        return BaseElements(driver = self.driver, locator=lctr)




    @property
    def list_of_divs(self):
        lctr = Locator(By.CSS_SELECTOR, ".inner.flex.flex-column.p-4")
        return BaseElements(driver = self.driver, locator=lctr)






