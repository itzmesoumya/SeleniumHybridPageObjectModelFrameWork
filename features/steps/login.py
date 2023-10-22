from behave import *
from features.pages.HomePage import HomePage


@given(u'I navigated to login page')
def step_impl(context):
    context.home_page=HomePage(context.driver)
    context.home_page.click_on_myaccount_option()
    context.login_page = context.home_page.click_on_login_option()

@when(u'I enter valid eamil address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context,email,password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)

@when(u'I click on Login button')
def step_impl(context):
    context.account_page =context.login_page.click_on_login_button()

@then(u'I should get logged in')
def step_impl(context):
    assert context.account_page.display_status_edit_account_info()


@when(u'I enter invalid eamil address and valid password say "{password}" into the fields')
def step_impl(context,password):
    context.login_page.enter_email_address("demo@gmail.com")
    context.login_page.enter_password(password)


@then(u'I should get propper warning message')
def step_impl(context):
    expected_text = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.display_status_check().__eq__(expected_text)


@when(u'I enter valid eamil address and invalid password say "{password}" into the fields')
def step_impl(context,password):
    context.login_page.enter_email_address("demoauto@gmail.com")
    context.login_page.enter_password(password)

@when(u'I enter invalid eamil address and invalid password say "{password}" into the fields')
def step_impl(context,password):
    context.login_page.enter_email_address("demo@gmail.com")
    context.login_page.enter_password(password)

@when(u'I  dont enter anything into  the fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")