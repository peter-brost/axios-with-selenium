from behave import given, when, then


@given("I am on the /login page")
def given_user_on_login_page(context):
    context.login_page.open(context.base_url)


@when('I enter "{username}" in the username field')
def when_user_enters_username(context, username):
    context.login_page.enter_username(username)


@when('I enter "{password}" into the password field')
def when_user_enters_password(context, password):
    context.login_page.enter_password(password)


@when("I click on the login button")
def when_user_clicks_login_button(context):
    context.login_page.click_login_button()


@then('I should see "{url_part}" in the current page\'s url')
def then_url_contains_expected_part(context, url_part):
    current_url = context.driver.current_url
    assert (
        url_part in current_url
    ), f"Expected '{url_part}' to be in the current URL, but it wasn't."


@then("I should see the logout button on the current page")
def then_logout_button_visible_on_page(context):
    logout_button = context.login_page.get_logout_button()
    assert (
        logout_button.is_displayed()
    ), "Logout button not found or not visible on the current page."
