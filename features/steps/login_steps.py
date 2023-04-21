from behave import given, when, then

@given("I am on the /login page")
def step_impl(context):
    context.login_page.open(context.base_url)

@when('I enter "{username}" in the username field')
def step_impl(context, username):
    context.login_page.enter_username(username)

@when('I enter "{password}" into the password field')
def step_impl(context, password):
    context.login_page.enter_password(password)

@when("I click on the login button")
def step_impl(context):
    context.login_page.click_login_button()

@then('I should see "{url_part}" in the current page\'s url')
def step_impl(context, url_part):
    current_url = context.driver.current_url
    assert url_part in current_url, f"Expected '{url_part}' to be in the current URL, but it wasn't."

@then("I should see the logout button on the current page")
def step_impl(context):
    logout_button = context.login_page.get_logout_button()
    assert logout_button.is_displayed(), "Logout button not found or not visible on the current page."
