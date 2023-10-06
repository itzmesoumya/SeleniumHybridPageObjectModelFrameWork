from selenium.webdriver.common.by import By

from pageobjects.BasePage import BasePage
from pageobjects.LoginPage import LoginPage
from pageobjects.RegisterPage import RegisterPage
from pageobjects.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    my_account_drop_menu_xpath = "//ul[@class='list-inline']//li[@class='dropdown']"
    login_option_linktext = "Login"
    register_option_linktext = "Register"

    def enter_product_into_search_box_field(self, product_name):
        self.type_into_element(product_name, "search_box_field_name", self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.element_click("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)

    def click_on_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_option_linktext).click()
        return LoginPage(self.driver)

    def click_on_register_option(self):
        self.driver.find_element(By.LINK_TEXT,self.register_option_linktext).click()
        return RegisterPage(self.driver)

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        self.click_on_search_button()
        return SearchPage(self.driver)

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        self.click_on_login_option()
        return LoginPage(self.driver)

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.click_on_register_option()
