from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:

    def generate_email_with_time_stamp(self):
        current_datetime = datetime.now()
        timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        timestamp = timestamp.replace(" ", "_").replace(":", "_")
        return "soumyaranjan" + timestamp + "@gmail.com"