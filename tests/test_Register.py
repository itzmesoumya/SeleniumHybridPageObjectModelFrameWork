from pageobjects.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):

    def test_create_account_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        rester_page = home_page.navigate_to_register_page()
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_page = register_page.register_an_account("soumya", "mohanty", "demoauto@gmail.com",
                                                         "9090874537", "soumya", "soumya", "yes", "select")
        retrive_text = account_page.retrive_account_creation_message()
        expected_text = "Your Account Has Been Created!"
        assert retrive_text.__eq__(expected_text)

        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_page = register_page.register_an_account("soumya", "mohanty", self.generate_email_time_stamp(),
                                                         "9090874537", "soumya", "soumya", "no", "select")
        retrive_text = account_page.retrive_account_creation_message()
        expected_text = "Your Account Has Been Created!"
        assert retrive_text.__eq__(expected_text)

    def test_create_account_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_page = register_page.register_an_account("soumya", "mohanty", self.generate_email_time_stamp(),
                                                         "9090874537", "soumya", "soumya", "yes", "select")
        retrive_text = account_page.retrive_account_creation_message()
        expected_text = "Your Account Has Been Created!"
        assert retrive_text.__eq__(expected_text)

    def test_create_account_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        rester_page = home_page.navigate_to_register_page()
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_page = register_page.register_an_account("soumya", "mohanty", "demoauto@gmail.com",
                                                         "9090874537", "soumya", "soumya", "yes", "select")
        retrive_text = register_page.retrive_duplicate_warning_message()
        expected_text = "Warning: E-Mail Address is already registered!"
        assert retrive_text.__eq__(expected_text)

    def test_login_without_entering_any_field(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.click_on_continue_button()
        retrive_text = register_page.retrive_warning_message()
        expected_text = "Warning: You must agree to the Privacy Policy!"
        assert retrive_text.__eq__(expected_text)