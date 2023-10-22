from behave import *
from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


@given(u'I navigate to home page')
def step_impl(context):
    assert context.driver.title.__eq__("Your Store")


@when(u'I enter valid product say "{product}" into the search box field')
def step_impl(context,product):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_product_name_in_searchbox(product)


@when(u'I click on Search Button')
def step_impl(context):
    context.home_page= HomePage(context.driver)
    context.search_page =context.home_page.click_on_search_button()


@then(u'Proper error message should be displayed in search results')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria.1"
    assert context.search_page.display_invalid_product_message().__eq__(expected_text)


@when(u'I dont enter anything into the search box field')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_product_name_in_searchbox("")


@then(u'Valid product should get displayed in search results')
def step_impl(context):
    assert context.search_page.display_valid_product_message()


@when(u'I enter invalid product say "{product}" into the search box field')
def step_impl(context,product):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_product_name_in_searchbox(product)