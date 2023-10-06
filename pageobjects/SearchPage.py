from pageobjects.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_linkext = "HP LP3065"
    no_product_mesage_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_valid_product(self):
        return self.check_display_status_of_element("valid_hp_product_linkext",self.valid_hp_product_linkext)

    def retrive_no_product_messsage(self):
        return self.retrieve_element_text("no_product_mesage_xpath",self.no_product_mesage_xpath)