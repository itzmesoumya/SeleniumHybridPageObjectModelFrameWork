from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    valid_hp_product_linkext = "HP LP3065"
    no_product_mesage_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_valid_product(self):
        return self.driver.find_element(By.LINK_TEXT,self.valid_hp_product_linkext).is_displayed()

    def retrive_no_product_messsage(self):
        return self.driver.find_element(By.XPATH,self.no_product_mesage_xpath).text