from behave import given, when, then


@given("the user is on the Dropdown page")
def given_user_on_dropdown_page(context):
    context.dropdown_page.open(context.base_url)


@when("the user selects Option 1 from the dropdown menu")
def when_user_selects_option_1(context):
    context.dropdown_page.select_option_1()


@then("Option 1 should be displayed as the selected option")
def then_option_1_displayed_as_selected(context):
    selected_option_text = context.dropdown_page.get_selected_option_text()
    assert (
        selected_option_text == "Option 1"
    ), f"Expected 'Option 1', but got '{selected_option_text}'"


@when("the user selects Option 2 from the dropdown menu")
def when_user_selects_option_2(context):
    context.dropdown_page.select_option_2()


@then("Option 2 should be displayed as the selected option")
def then_option_2_displayed_as_selected(context):
    selected_option_text = context.dropdown_page.get_selected_option_text()
    assert (
        selected_option_text == "Option 2"
    ), f"Expected 'Option 2', but got '{selected_option_text}'"
