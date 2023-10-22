import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import ConfigReader


def before_scenario(context, driver):
    selected_browser = ConfigReader.read_configuration("basic info","browser")
    if selected_browser.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif selected_browser.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif selected_browser.__eq__("edge"):
        context.driver = webdriver.Edge()
    else:
        context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info","url"))


def after_scenario(context, driver):
    context.driver.quit()

def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)