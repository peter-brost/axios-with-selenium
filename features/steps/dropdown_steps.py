from behave import given, when, then


@given("the user is on the Dropdown page")
def step_impl(context):
    context.dropdown_page.open(context.base_url)

@when("the user selects Option 1 from the dropdown menu")
def step_impl(context):
    context.dropdown_page.select_option_1()

@then("Option 1 should be displayed as the selected option")
def step_impl(context):
    selected_option_text = context.dropdown_page.get_selected_option_text()
    assert selected_option_text == "Option 1", f"Expected 'Option 1', but got '{selected_option_text}'"

@when("the user selects Option 2 from the dropdown menu")
def step_impl(context):
    context.dropdown_page.select_option_2()

@then("Option 2 should be displayed as the selected option")
def step_impl(context):
    selected_option_text = context.dropdown_page.get_selected_option_text()
    assert selected_option_text == "Option 2", f"Expected 'Option 2', but got '{selected_option_text}'"
