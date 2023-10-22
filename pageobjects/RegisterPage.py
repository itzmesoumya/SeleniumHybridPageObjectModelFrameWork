from selenium.webdriver.common.by import By
from pageobjects.AccountSuccessPage import AccountSuccessPage


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

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
        self.driver.find_element(By.ID,self.first_name_field_id).click()
        self.driver.find_element(By.ID,self.first_name_field_id).clear()
        self.driver.find_element(By.ID,self.first_name_field_id).send_keys(first_name)

    def last_name_text_field(self, last_name):
        self.driver.find_element(By.ID,self.last_name_field_id).click()
        self.driver.find_element(By.ID,self.last_name_field_id).click()
        self.driver.find_element(By.ID,self.last_name_field_id).send_keys(last_name)

    def email_text_field(self, email):
        self.driver.find_element(By.ID,self.email_field_id).click()
        self.driver.find_element(By.ID,self.email_field_id).clear()
        self.driver.find_element(By.ID,self.email_field_id).send_keys(email)

    def telephone_text_field(self, telephoneNo):
        self.driver.find_element(By.ID,self.telephone_field_id).click()
        self.driver.find_element(By.ID,self.telephone_field_id).clear()
        self.driver.find_element(By.ID,self.telephone_field_id).send_keys(telephoneNo)

    def password_text_field(self, password):
        self.driver.find_element(By.ID,self.password_field_id).click()
        self.driver.find_element(By.ID,self.password_field_id).clear()
        self.driver.find_element(By.ID,self.password_field_id).send_keys(password)

    def confirm_password_text_field(self, confirm_password):
        self.driver.find_element(By.ID,self.confirm_password_field_id).click()
        self.driver.find_element(By.ID,self.confirm_password_field_id).clear()
        self.driver.find_element(By.ID,self.confirm_password_field_id).send_keys(confirm_password)

    def radio_button_yes(self):
        self.driver.find_element(By.XPATH,self.newsletter_radio_button_yes_xpath).click()

    def policy_checkbox(self):
        self.driver.find_element(By.NAME,self.policy_name).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH,self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def retrive_duplicate_warning_message(self):
        return self.driver.find_element(By.XPATH,self.duplicate_warning_message_xpath).text

    def retrive_warning_message(self):
        return self.driver.find_element(By.XPATH,self.warning_message_xpath).text

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
