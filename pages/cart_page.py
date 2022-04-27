from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class CartPage(BasePage):
    url = 'https://tstprep.com/cart/'

    @property
    def coupon_input(self):
        lctr = Locator(By.CSS_SELECTOR, "input#coupon_code")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def apply_coupon_btn(self):
        lctr = Locator(By.CSS_SELECTOR, "button[name='apply_coupon']")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def proceed_to_checkout_btn(self):
        lctr = Locator(By.CSS_SELECTOR, "//a[text()[contains(.,'Proceed to checkout')]]")
        return BaseElement(driver = self.driver, locator=lctr)


