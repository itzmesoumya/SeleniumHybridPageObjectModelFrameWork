from datetime import datetime

import pytest

from BaseTest import BaseTest
from pageobjects.HomePage import HomePage
from utilities import ExcelUtilis


class TestLogin(BaseTest):

    @pytest.mark.parametrize("email_address,password",
                             ExcelUtilis.get_data_from_excel("ExcelFiles/Testone.xlsx", "LoginSheet"))
    def test_login_with_valid_credentials(self, email_address, password):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application(email_address,password)
        assert account_page.display_status_of_edit_your_account_information_option()

    def test_login_with_invalid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(),"soumyadmin")
        expected_response = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrive_warning_message().__eq__(
            expected_response)

    def test_login_with_valid_email_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("demoauto@gmail.com","soumyadmin")
        expected_response = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrive_warning_message().__eq__(
            expected_response)

    def test_login_with_invalid_email_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(),"soumyadmin")
        login_page.click_on_login_button()
        expected_response = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrive_warning_message().__eq__(
            expected_response)