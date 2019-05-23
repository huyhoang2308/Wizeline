# from selenium import webdriver
from base import Keyword
from locators import *
import data


class LoginPage(Keyword):

    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    def enter_email(self, user):
        self.input(*self.locator.USER_NAME, text=data.get_user(user)["email"])

    def enter_password(self, user):
        self.input(*self.locator.PASSWORD, text=data.get_user(user)["password"])

    def click_login_button(self):
        self.click(*self.locator.LOGIN_BTN)

    def click_cancel_button(self):
        self.click(*self.locator.CANCEL_BTN)

    def login(self, user):
        self.enter_email(user)
        self.enter_password(user)
        self.click_login_button()
        return ProductPage(self.driver)

    def login_with_valid_user(self, user):
        self.login(user)
        return self.is_element_present(*HomePageLocators.HEADER)

class ProductPage(Keyword):

    def __init__(self, driver):
        self.product_locator = ProductPageLocators
        super().__init__(driver)

    def add_item_to_cart(self, item):
        items = self.find_elements(*self.product_locator.ITEMS)
        for _item in items:
            while _item.find_element_by_class_name('inventory_item_name').text == data.get_item(item)['title']:
                _item.find_element_by_class_name('btn_primary').click()
                break

    def add_items_to_cart(self, item):
        items = self.find_elements(*self.product_locator.ITEMS)
        for _item in items:
            if _item.find_element_by_class_name('inventory_item_name').text == data.get_item(item)['title']:
                _item.find_element_by_class_name('btn_primary').click()

    def click_my_cart_icon(self):
        self.click(*self.product_locator.MY_CART_ICON)

    def add_new_item_to_cart(self, item):
        self.add_item_to_cart(item)
        self.click_my_cart_icon()
        return YourCartPage(self.driver)

class YourCartPage(Keyword):

    def __init__(self, driver):
        self.your_cart_locator = YourCartLocators
        super().__init__(driver)
    
    def check_out(self):
        self.click(*self.your_cart_locator.CHECKOUT_BTN)

    def continue_shopping(self):
        self.click(*self.your_cart_locator.CONTINUE_BTN)

    def remove_item(self):
        self.click(*self.your_cart_locator.REMOVE_BTN)

    def checkout_item(self):
        self.check_out()
        return CheckOutInfoPage

class CheckOutInfoPage(Keyword):

    def __init__(self, driver):
        self.check_out_locator = CheckOutInformationLocators
        super().__init__(driver)

    def enter_first_name(self):
        self.input(*self.check_out_locator.FIRST_NAME, text='first name')

    def enter_last_name(self):
        self.input(*self.check_out_locator.LAST_NAME, text='last name')

    def enter_zip_code(self):
        self.input(*self.check_out_locator.ZIPCODE, text='123')

    def click_continue_button(self):
        self.click(*self.check_out_locator.CONTINUE_BTN)

    def enter_required_info(self):
        self.enter_first_name()
        self.enter_last_name()
        self.enter_zip_code()
        self.click_continue_button()
        return CheckoutOverviewPage

class CheckoutOverviewPage(Keyword):

    def __init__(self, driver):
        self.overview_locator = CheckOutOVerviewLocators
        super().__init__(driver)

    def click_finish(self):
        self.click(self.overview_locator.FINISH_BTN)

    def process_next(self):
        self.click_finish()
        return FinishLocatorsPage

class FinishLocatorsPage(Keyword):

    def __init__(self, driver):
        self.locator = FinishLocators
        super().__init__(driver)

    def get_text(self):
        results = []
        header = self.get_text(*self.locator.HEADER)
        # self.assertEqual(header, 'THANK YOU FOR YOUR ORDER')
        desc = self.get_text(*self.locator.DESCRIPTION)
        # self.assertEqual(desc, 'Your order has been dispatched, and will arrive just as fast as the pony can get there!')
        results.append(header)
        results.append(desc)
        return results

