from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElements(object):
    def __init__(self, driver, value, by):
       self.driver = driver
       self.value = value
       self.by = by
       self.locator = (self.by, self.value)
       self.web_elements = None
       self.find()

    def find(self):
        element1 = WebDriverWait(
            self.driver,10).until(
                EC.presence_of_all_elements_located(self.locator))
        self.web_element = element1
        return None

        

    @property
    def urls_from_customise_link_modal(self):
        texts = ""
        for matched_element in self.web_elements:
            text = matched_element.text
            texts += " "
            texts += text
        return texts


