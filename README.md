# Plato Webshop Automation Project
A python automation project using Behave and Selenium to test the plato webshop

## Install List:
- pip install selenium
- pip install behave
- pip install nose
- pip install allure-behave

## Run Commands

### Run all features
behave -f allure_behave.formatter:AllureFormatter -o reports/ features

### Generate the Allure report
allure serve reports/


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
do something

### Tests

Contains the tests, which are located inside Feature files. These feature files are written in natural language that even non technical people can understand.\

Example:

Scenario: Test a feature\
Given I have some context\
When I do something\
Then something happens

## Other Information

### Base URL
The url for the webpage is located in base_page.py, it is called base_url. If the url changes, modify it here

### Environment.py
The environment.py file contains setup and teardown methods that will occur before and after each scenario or feature. It also contains the method to capture screenshots on failure

### __init__.py
This file does not need to be modified and is left intentionally empty. 

### Base Page and Base Steps

Base_page should contain simple methods that can be used anywhere, such as clicking an element or sending text or asserting a value. 
This prevents repetition

Base_steps should contain any steps not specific to a page, such as the initial opening of the browser. 