from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # A dictionary of elements for the home page
    locators = {

        "cart": 'xpath',
        #product contains the text for various products
        "product": "//h2[contains(text(),'{}')]",
        "add to cart": "//h2[contains(text(),'{}')]/ancestor::a/preceding-sibling::div//a[contains(text(),'Add to cart')]",
        "load more": "//a[contains(text(),'Load More')]"

    }