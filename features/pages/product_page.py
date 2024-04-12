from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {

        "add to cart": "//button[contains(text(),'Add to cart')]",
        "plus": "//button[@class='plus']",
        "minus": "//button[@class='minus']",
        "quantity": "//input[@name='quantity']"
    }