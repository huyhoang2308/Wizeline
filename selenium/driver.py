from selenium import webdriver
import os


class Driver():

    def __init__(self, browser_name, base_url='https://www.saucedemo.com'):
        self.browser_name = browser_name.lower()
        self.base_url = base_url

    def setup_driver(self):
        if os.name == 'nt':
            gecko = '..\\libs\\geckodriver.exe'
            chrome = '..\\libs\\chromedriver.exe'
        else:
            gecko = '../libs/geckodriver'
            chrome = '../libs/chromedriver'
        if self.browser_name == 'firefox':
            driver = webdriver.Firefox(executable_path=gecko)
        elif self.browser_name == 'chrome':
            driver = webdriver.Chrome(executable_path=chrome)
        else:
            print ("browser not support")
        driver.get(self.base_url)
        return driver

