from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_text_field_id = "input-email"
    telephone_text_field_id = "input-telephone"
    password_text_field_id = "input-password"
    confirm__password_text_field_id = "input-confirm"
    policy_check_field_name = "agree"
    yes_radio_button_xpath ="//label[text()='Yes']//input[@name='newsletter']"
    continue_button_xpath ="//input[@class='btn btn-primary']"
    duplicate_warning_message_xpath="//div[@class='alert alert-danger alert-dismissible']"
    first_name_warning_message_xpath="//div[@class='col-sm-10']//div[text()='First Name must be between 1 and 32 characters!']"
    last_name_warning_message_xpath="//div[@class='col-sm-10']//div[text()='Last Name must be between 1 and 32 characters!']"
    email_warning_message_xpath ="//div[@class='col-sm-10']//div[text()='E-Mail Address does not appear to be valid!']"
    telephone_warning_message_xpath ="//div[@class='col-sm-10']//div[text()='Telephone must be between 3 and 32 characters!']"
    password_warning_message_xpath ="//div[@class='col-sm-10']//div[text()='Password must be between 4 and 20 characters!']"

    def display_first_name_warning_message(self):
        return self.driver.find_element(By.XPATH,self.first_name_warning_message_xpath).text

    def display_last_name_warning_message(self):
        return self.driver.find_element(By.XPATH,self.last_name_warning_message_xpath).text

    def display_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.email_warning_message_xpath).text

    def display_telephone_warning_message(self):
        return self.driver.find_element(By.XPATH,self.email_warning_message_xpath).text

    def display_password_warning_message(self):
        return self.driver.find_element(By.XPATH,self.password_warning_message_xpath).text

    def display_duplicate_warning_message(self):
        return self.driver.find_element(By.XPATH,self.duplicate_warning_message_xpath).text
    def first_name_text_field(self,firstname):
        self.driver.find_element(By.ID,self.first_name_field_id).send_keys(firstname)

    def last_name_text_field(self,lastname):
        self.driver.find_element(By.ID,self.last_name_field_id).send_keys(lastname)

    def email_text_field(self,email):
        self.driver.find_element(By.ID,self.email_text_field_id).send_keys(email)

    def phone_number_field(self,phonenumber):
        self.driver.find_element(By.ID,self.telephone_text_field_id).send_keys(phonenumber)

    def password_text_field(self,password):
        self.driver.find_element(By.ID,self.password_text_field_id).send_keys(password)

    def confirm_password_text_field(self,confirmpassword):
        self.driver.find_element(By.ID,self.confirm__password_text_field_id).send_keys(confirmpassword)

    def yes_radio_button(self):
        self.driver.find_element(By.XPATH,self.yes_radio_button_xpath).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH,self.continue_button_xpath).click()
        return AccountPage(self.driver)


