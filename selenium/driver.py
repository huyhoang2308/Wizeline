from selenium import webdriver


class Driver():

    def __init__(self, browser_name, base_url='https://www.saucedemo.com'):
        self.browser_name = browser_name.lower()
        self.base_url = base_url

    def setup_driver(self):
        if self.browser_name == 'firefox':
            driver = webdriver.Firefox(executable_path="..\\libs\\geckodriver.exe")
        elif self.browser_name == 'chrome':
            driver = webdriver.Chrome(executable_path="..\\libs\\chromedriver.exe")
        else:
            print ("browser not support")
        driver.get(self.base_url)
        return driver

