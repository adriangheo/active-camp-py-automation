from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, value, by):
       self.driver = driver
       self.value = value
       self.by = by
       self.locator = (self.by, self.value)
       self.web_element = None
       self.find()

    def check_element_exists(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (self.locator))
            )
        except Exception:
            print("element was NOT found")
            return False
        else:
            print("element was found")
        return True

    def find(self):
        if(self.check_element_exists() ==True):
            element1 = WebDriverWait(
                self.driver,10).until(
                    EC.visibility_of_element_located(self.locator))
            self.web_element = element1
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        if(self.check_element_exists() ==True):
            element2 = WebDriverWait(
                self.driver,10).until(
                    EC.element_to_be_clickable(self.locator))
            element2.click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute
    
    @property
    def text(self):
        if(self.check_element_exists() ==True):
            text = self.web_element.text
            return text
        else:
            return ""

    @property
    def field_value(self):
        if(self.check_element_exists() ==True):
            field_value = self.web_element.get_attribute('value')
            if(field_value == ""):
                field_value = "n/a"
            return field_value
        else:
            return ""

    @property
    def switch_btn_value(self):
        if(self.check_element_exists() ==True):
            classes_of_switch_btn1 = self.web_element.get_attribute('class').split()
            field_value = "n/a"
            if 'switch_on' in classes_of_switch_btn1:
                field_value = "ON"
            else:
                field_value = "OFF"
            return field_value
        else:
            return ""

