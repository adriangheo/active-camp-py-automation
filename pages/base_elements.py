from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElements(object):
    def __init__(self, driver, locator):
       self.driver = driver
       self.locator =  locator
       self.web_element = []
       self.find()

    def find(self):
        # self.driver.find_element(by=self.by, value=self.locator)
        element1 = WebDriverWait(
            self.driver,10).until(
                EC.element_to_be_clickable(self.locator))
        # self.web_element.append('aaa')
        # self.web_element.append('bbb')
        print("base elm start")
        print(type(self.web_element))
        print("base elm end")

        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        WebDriverWait(
            self.driver,10).until(
                EC.element_to_be_clickable(self.locator))
        self.driver.execute_script("arguments[0].click();",self.web_element )

        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute
    
    @property
    def text(self):
        text = self.web_element.text
        return text