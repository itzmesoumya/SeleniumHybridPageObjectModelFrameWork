from pageobjects.AccountPage import AccountPage
from pageobjects.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_name = "email"
    password_field_name = "password"
    login_button_xpath = "//input[@class='btn btn-primary']"
    warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self, email_address):
        self.type_into_element(email_address,"email_address_field_name",self.email_address_field_name)

    def enter_password(self, password):
        self.type_into_element(password,"password_field_name",self.password_field_name)

    def click_on_login_button(self):
        self.element_click("login_button_xpath",self.login_button_xpath)
        return AccountPage(self.driver)

    def retrive_warning_message(self):
        return self.retrieve_element_text("warning_message_xpath",self.warning_message_xpath)

    def login_to_application(self,email_address,password):
        self.enter_email_address(email_address)
        self.enter_password(password)
        return self.click_on_login_button()
