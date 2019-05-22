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
        for sitem in items:
            if item.find_element(*self.product_locator.ITEM_NAME) == data.get_item(item)['title']:
                item.find_element(*self.product_locator.ADD_TO_CART_BTN).click()

    def click_my_cart(self):
        self.click(*self.product_locator.MY_CART_ICON)

    def add_new_item_to_cart(self, item):
        self.add_item_to_cart(item)
        self.click_my_cart()
        return YourCartPage(self.driver)

class YourCartPage(Keyword):
    pass
