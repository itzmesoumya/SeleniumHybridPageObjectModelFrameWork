from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    invalid_product_message_xpath ="//input[@id='button-search']/following-sibling::p"
    valid_product_message_linktext= "HP LP3065"


    def display_invalid_product_message(self):
        return self.driver.find_element(By.XPATH,self.invalid_product_message_xpath).text

    def display_valid_product_message(self):
        return self.driver.find_element(By.LINK_TEXT,self.valid_product_message_linktext).is_displayed()