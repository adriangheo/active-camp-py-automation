# Page Object Model Test
from selenium import webdriver

from pages.store_page import StorePage
from pages.cart_page import CartPage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Test Setup
browser = webdriver.Firefox()

browser.get('https://staging4.tstprep.com/store/')

store_page = StorePage(driver=browser)
store_page.go()
store_page.private_lessons_for_duolingo.click()

store_page.second_pricebox_btn.click()
 
cartPage = CartPage(driver=browser)
cartPage.coupon_input.input_text("ALEX100TEST")
cartPage.apply_coupon_btn.click()
# cartPage.proceed_to_checkout_btn.click()






