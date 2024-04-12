# Plato Webshop Automation Project
A python automation project using Behave and Selenium to test the plato webshop

## Install List:
- pip install selenium
- pip install behave
- pip install nose
- pip install allure-behave

## Project Structure
This is a Page Object Model project, and it uses the Behave framework to structure tasks. 

Files are located one of three directories:

- pages
- steps
- tests

### Pages

Contains information specific to each 'page' of the website. Each page contains a dictionary called 'locators' that contains xpaths for the elements on the page.

### Steps

Contains the test steps. These test steps are written using Gherkin keywords such as Given, When, and Then.\
Example:\
@when('I do something')\
def step_definition(context)\
    do something\

### Tests

Contains the tests, which are located inside Feature files. These feature files are written in natural language that even non technical people can understand.\

Example:\
Feature: Test 001\

  Scenario: Test a feature\
    Given I have some context\
    When I do something\
    Then something happens\