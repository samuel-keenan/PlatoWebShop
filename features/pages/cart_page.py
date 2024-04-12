from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {

        "name": 'xpath',
        "product": "//h2[contains(text(),'{}')]",
        "clear all": "//button[@name='empty_cart']",
        "proceed to checkout": "//a[contains(text(),'Proceed to checkout')]"

        }