from selenium.webdriver.common.by import By
from pageobjects.AccountSuccessPage import AccountSuccessPage
from pageobjects.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    policy_name = "agree"
    newsletter_radio_button_yes_xpath = "//input[@value='1'][@name='newsletter']"
    continue_button_xpath = "//input[@value='Continue']"
    duplicate_warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def first_name_text_field(self, first_name):
        self.type_into_element(first_name,"first_name_field_id",self.first_name_field_id)

    def last_name_text_field(self, last_name):
        self.type_into_element(last_name,"last_name_field_id",self.last_name_field_id)

    def email_text_field(self, email):
        self.type_into_element(email,"email_field_id",self.email_field_id)

    def telephone_text_field(self, telephoneNo):
        self.type_into_element(telephoneNo,"telephone_field_id",self.telephone_field_id)

    def password_text_field(self, password):
        self.type_into_element(password, "password_field_id",self.password_field_id)

    def confirm_password_text_field(self, confirm_password):
        self.type_into_element(confirm_password,"confirm_password_field_id",self.confirm_password_field_id)

    def radio_button_yes(self):
        self.driver.find_element(By.XPATH,"newsletter_radio_button_yes_xpath",self.newsletter_radio_button_yes_xpath)

    def policy_checkbox(self):
        self.driver.find_element(By.NAME,self.policy_name).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH,self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def retrive_duplicate_warning_message(self):
        return self.retrieve_element_text("duplicate_warning_message_xpath",self.duplicate_warning_message_xpath)

    def retrive_warning_message(self):
        return self.retrieve_element_text("warning_message_xpath",self.warning_message_xpath)

    def register_an_account(self,first_name,last_name,email,telephoneNo,password,confirm_password,yes_or_no,privacy_policy):
        self.first_name_text_field(first_name)
        self.last_name_text_field(last_name)
        self.email_text_field(email)
        self.telephone_text_field(telephoneNo)
        self.password_text_field(password)
        self.confirm_password_text_field(confirm_password)
        if yes_or_no.__eq__("yes"):
            self.radio_button_yes()
        if privacy_policy.__eq__("select"):
            self.policy_checkbox()
        return self.click_on_continue_button()
