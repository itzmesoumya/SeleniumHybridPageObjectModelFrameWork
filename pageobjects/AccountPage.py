from selenium.webdriver.common.by import By

from pageobjects.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    edit_your_account_information_link_linktext = "Edit your account information"

    def display_status_of_edit_your_account_information_option(self):
        return self.driver.find_element(By.LINK_TEXT,self.edit_your_account_information_link_linktext)
