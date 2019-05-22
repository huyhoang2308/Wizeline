import time
from selenium import webdriver


class Keyword(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def is_element_present(self, *locator):
        if self.find_element(*locator):
            return True
        else:
            return False

    def wait_for_element_present(self, *locator, timeout=10):
        for i in range(timeout):
            try:
                if self.is_element_present(*locator):
                    return True
            except:
                pass
            time.sleep(i)
        return False

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input(self, *locator, text=None):
        if self.wait_for_element_present(*locator):
            return self.find_element(*locator).send_keys(text)

    def click(self, *locator):
        if self.wait_for_element_present(*locator):
            return self.find_element(*locator).click()

    def get_text(self, *locator):
        if self.wait_for_element_present(*locator):
            return self.find_element(*locator).getText()

    # def open(self,url):
    #     url = self.base_url + url
    #     self.driver.get(url)
        
    def get_title(self):
        return self.driver.title
        
    def get_url(self):
        return self.driver.current_url
    
    # def hover(self, *locator):
    #     element = self.find_element(*locator)
    #     hover = ActionChains(self.driver).move_to_element(element)
    #     hover.perform()
