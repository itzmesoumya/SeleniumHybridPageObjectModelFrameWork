from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.RegisterPage import RegisterPage
from features.pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_linktext = "Login"
    register_option_linktext = "Register"
    enter_product_name="search"
    search_button_xpath = "//div[@id='search']//button[@class='btn btn-default btn-lg']"

    def enter_product_name_in_searchbox(self,product_name):
        self.driver.find_element(By.NAME,self.enter_product_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_on_myaccount_option(self):
        self.driver.find_element(By.XPATH,self.my_account_option_xpath).click()

    def click_on_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_option_linktext).click()
        return LoginPage(self.driver)

    def click_on_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.register_option_linktext).click()
        return RegisterPage(self.driver)