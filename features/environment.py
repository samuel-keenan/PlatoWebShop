from behave import *
import allure
from datetime import datetime
from selenium import webdriver


def after_scenario(context, scenario):
    if scenario.status == "failed":
        step_name = getattr(context, "current_step", "unknown_step")
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"screenshot_{scenario.name}_{step_name}_{current_datetime}.png"
        capture_screenshot(context, filename)


def capture_screenshot(context, title='captured_screenshot'):
    allure.attach(
        context.driver.get_screenshot_as_png(),
        name=f'{title}', attachment_type=allure.attachment_type.PNG
        )

def before_step(context, step):
    # Store the current step name in context
    context.current_step = step.name

def before_feature(context, feature):
    context.driver = webdriver.Chrome()

def after_feature(context, feature):
    context.driver.quit()
