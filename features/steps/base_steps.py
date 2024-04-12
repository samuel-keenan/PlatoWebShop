from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.base_page import *

@given('I open the Plato Shop')
def navigate_to_home_page(context):
    context.driver.get(base_url)
    context.driver.maximize_window()
    context.home_page = HomePage(context.driver)