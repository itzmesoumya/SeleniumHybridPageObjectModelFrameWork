from selenium.webdriver.common.by import By

from pageobjects.AccountPage import AccountPage

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_address_field_name = "email"
    password_field_name = "password"
    login_button_xpath = "//input[@class='btn btn-primary']"
    warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self, email_address):
        self.driver.find_element(By.NAME,self.email_address_field_name).click()
        self.driver.find_element(By.NAME,self.email_address_field_name).clear()
        self.driver.find_element(By.NAME,self.email_address_field_name).send_keys(email_address)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_field_name).click()
        self.driver.find_element(By.NAME, self.password_field_name).clear()
        self.driver.find_element(By.NAME, self.password_field_name).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()
        return AccountPage(self.driver)

    def retrive_warning_message(self):
        return self.driver.find_element(By.XPATH,self.warning_message_xpath).text

    def login_to_application(self,email_address,password):
        self.enter_email_address(email_address)
        self.enter_password(password)
        return self.click_on_login_button()
