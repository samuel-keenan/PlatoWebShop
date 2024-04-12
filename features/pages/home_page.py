from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # A dictionary of elements for the home page
    locators = {

        "name": 'xpath'

        }