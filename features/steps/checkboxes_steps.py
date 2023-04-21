from behave import given, when, then

@given("the user is on the Checkboxes page")
def step_impl(context):
    context.checkboxes_page.open(context.base_url)

@when("the user checks the first checkbox")
def step_impl(context):
    context.checkboxes_page.click_checkbox_1()

@when("the user unchecks the second checkbox")
def step_impl(context):
    context.checkboxes_page.click_checkbox_2()

@then("the first checkbox should be checked")
def step_impl(context):
    assert context.checkboxes_page.get_checkbox_1_status(), "The first checkbox is not checked."

@then("the second checkbox should be unchecked")
def step_impl(context):
    assert not context.checkboxes_page.get_checkbox_2_status(), "The second checkbox is checked."
