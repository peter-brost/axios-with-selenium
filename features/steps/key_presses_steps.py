from behave import given, when, then
from random import choice
import string


@given("the user is on the Key Presses page")
def given_user_on_key_presses_page(context):
    context.key_presses_page.open(context.base_url)


@when("the user enters a random character")
def when_user_enters_random_character(context):
    context.random_character = choice(string.ascii_uppercase)
    context.key_presses_page.enter_text(context.random_character)


@then('the page should display the message "You entered: [character]"')
def then_page_displays_message_with_entered_character(context):
    expected_result_text = f"You entered: {context.random_character}"
    actual_result_text = context.key_presses_page.get_result_text()
    assert (
        actual_result_text == expected_result_text
    ), f"Expected text '{expected_result_text}', but got '{actual_result_text}'"
