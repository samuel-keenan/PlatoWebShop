from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {

        "name": 'xpath',
        "product": "//h2[contains(text(),'{}')]",
        "update all": "//button[@name='update_cart']",
        "clear all": "//button[@name='empty_cart']",
        "proceed to checkout": "//a[contains(text(),'Proceed to checkout')]",
    #coupon code section
        "enter your code": "//button[contains(text(),'Click here to enter your code')]",
        "coupon code": "//input[@id='coupon_code']",
        "apply coupon": "//button[contains(text(),'Apply coupon')]",

        }