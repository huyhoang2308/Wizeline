import unittest
import data
from selenium import webdriver
from driver import Driver
from pages import *
from testCases import test_cases
from locators import *
# import time

# If you want to run it, you should type: python <module-name.py>

class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = Driver('firefox').setup_driver()

    def test_sign_in_with_valid_user(self):
        loginPage = LoginPage(self.driver)
        productPage = loginPage.login("standard_user")
        yourCartPage = productPage.add_new_item_to_cart('Sauce Labs Backpack')
        checkOutInfo = yourCartPage.checkout_item()
        checkOutOverview = checkOutInfo.enter_required_info()
        finishPage = checkOutOverview.process_next()
        result = finishPage.get_text()
        self.assertEqual(result, ['THANK YOU FOR YOUR ORDER',\
           'Your order has been dispatched, and will arrive just as fast as the pony can get there!'])


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)

