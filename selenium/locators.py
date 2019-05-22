from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class LoginPageLocators(object):
    USER_NAME         = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD          = (By.XPATH, '//*[@id="password"]')
    LOGIN_BTN         = (By.XPATH, '//*[@id="login_button_container"]/div/form/input[3]')

class ProductPageLocators(object):
    HEADER            = (By.XPATH, '//*[@id="inventory_filter_container"]/div')
    ITEMS             = (By.CLASS_NAME, 'inventory_item')
    ITEM_NAME         = (By.CLASS_NAME, 'inventory_item_name')
    ITEM_DESCRIPTION  = (By.CLASS_NAME, 'inventory_item_desc')
    ITEM_PRICE        = (By.CLASS_NAME, 'inventory_item_price')
    ADD_TO_CART_BTN   = (By.CLASS_NAME, 'btn_primary btn_inventory')
    MY_CART_ICON      = (By.CLASS_NAME, 'shopping_cart_link fa-layers fa-fw')

class YourCartLocators(object):
    REMOVE_BTN        = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/button')
    CHECKOUT_BTN      = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/a[2]')
    CONTINUE_BTN      = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/a[1]')

class CheckOutInformationLocators(object):
    FIRST_NAME        = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME         = (By.XPATH, '//*[@id="last-name"]')
    ZIPCODE           = (By.XPATH, '//*[@id="postal-code"]')
    CANCEL_BTN        = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[2]/a')
    CONTINUE_BTN      = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[2]/input')

class CheckOutOVerviewLocators(object):
    CANCEL_BTN        = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]/a[1]')
    FINISH_BTN        = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]/a[2]')

class FinishLocators(object):
    HEADER            = (By.XPATH, '//*[@id="checkout_complete_container"]/h2')
    DESCRIPTION       = (By.XPATH, '//*[@id="checkout_complete_container"]/div[1]')
    LOGO              = (By.XPATH, '//*[@id="checkout_complete_container"]/div[2]')