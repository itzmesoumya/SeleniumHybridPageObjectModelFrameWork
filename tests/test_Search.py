from BaseTest import BaseTest
from pageobjects.HomePage import HomePage

class TestSearch(BaseTest):
    def test_search_for_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("HP")
        assert search_page.display_status_of_valid_product()

    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("HONDA")
        expected_response = "There is no product that matches the search criteria."
        assert search_page.retrive_no_product_messsage.__eq__(expected_response)

    def test_search_without_entering_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrive_no_product_messsage.__eq__(expected_text)