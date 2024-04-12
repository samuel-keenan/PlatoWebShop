from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
@when('I click on "{element}"')
def click_on_home_page_element(context, element):
    context.home_page.click_on_element(context.home_page.locators[element])
