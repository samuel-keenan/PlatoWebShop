from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from nose.tools import assert_equal
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.implicit_wait = 15

    def click_element(self, locator_value):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        element.click()

    def input_text(self, locator_value, text):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        element.send_keys(text)

    def select_dropdown(self, locator_value, option_text):
        dropdown = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator_value))))
        dropdown.select_by_visible_text(option_text)

base_url = "http://18.225.209.250:8203/"