from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    edit_account_information_option_linktext= "Edit your account information"
    create_account_message_xpath ="//div[@id='content']/h1"

    def display_status_edit_account_info(self):
        return self.driver.find_element(By.LINK_TEXT,self.edit_account_information_option_linktext).is_displayed()

    def display_create_account_message(self):
        return self.driver.find_element(By.XPATH,self.create_account_message_xpath).text