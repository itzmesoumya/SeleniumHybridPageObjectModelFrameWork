from BaseTest import BaseTest
from pageobjects.HomePage import HomePage

class TestReister(BaseTest):

    def test_create_account_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("soumya","ranjan",self.generate_email_with_time_stamp(),"1234567890",
                                                                 "soumya123","soumya123","no","select")
        expected_text = "Your Account Has Been Created!"
        assert account_success_page.retrive_account_creation_message().__eq__(expected_text)

    def test_create_account_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("soumya", "ranjan", self.generate_email_with_time_stamp(), "1234567890",
                                          "soumya123", "soumya123", "yes", "select")

        expected_text = "Your Account Has Been Created!"
        assert account_success_page.retrive_account_creation_message().__eq__(expected_text)

    def test_create_account_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("soumya", "ranjan","demoauto@gmail.com", "1234567890",
                                          "soumya123", "soumya123", "yes", "select")
        expected_text = "Warning: E-Mail Address is already registered!"
        assert register_page.retrive_duplicate_warning_message().__eq__(expected_text)

    def test_login_without_entering_any_field(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("", "", "", "",
                                          "", "", "", "")
        expected_text = "Warning: You must agree to the Privacy Policy123"
        assert register_page.retrive_warning_message().__eq__(expected_text)