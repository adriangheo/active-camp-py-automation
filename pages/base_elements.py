from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElements(object):
    def __init__(self, driver,  value, by):
       self.driver = driver
       self.value = value
       self.by = by
       self.locator =  (self.by, self.value)
       self.web_elements = []
       self.find()

    def find(self):
        # self.driver.find_element(by=self.by, value=self.locator)
        elements = WebDriverWait(
            self.driver,10).until(
                EC.visibility_of_all_elements_located(self.locator))

        for elm in elements:
            self.web_elements.append(elm)
            print(elm)
                
        # # self.web_element.append('aaa')
        # # self.web_element.append('bbb')
        # print("base elm start")
        # self.web_elements.append(5)
        # self.web_elements.append(7)
        # print(type(self.web_elements))
        # print("base elm end")

        return None
