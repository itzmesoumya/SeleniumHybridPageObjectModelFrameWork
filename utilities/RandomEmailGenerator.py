from datetime import datetime


def get_email_address_generator():
    current_datetime = datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    timestamp = timestamp.replace(" ", "_").replace(":", "_")
    return  "soumyaranjan" + timestamp + "@gmail.com"