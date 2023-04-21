import random
from behave import given, when, then

@given("the user is on the Add/Remove Elements page")
def step_impl(context):
    context.add_remove_elements_page.open(context.base_url)

@when("the user adds a random number of elements")
def step_impl(context):
    context.number_of_elements = random.randint(1, 10)
    for _ in range(context.number_of_elements):
        context.add_remove_elements_page.click_add_element_button()

@then("the page should display the correct number of delete buttons")
def step_impl(context):
    delete_button_count = context.add_remove_elements_page.get_delete_element_button_count()
    assert delete_button_count == context.number_of_elements, f"Expected {context.number_of_elements} delete buttons, but found {delete_button_count}."

@when("the user removes all added elements")
def step_impl(context):
    for _ in range(context.number_of_elements):
        context.add_remove_elements_page.click_delete_element_button()

@then("the page should display zero delete buttons")
def step_impl(context):
    delete_button_count = context.add_remove_elements_page.get_delete_element_button_count()
    assert delete_button_count == 0, f"Expected 0 delete buttons, but found {delete_button_count}."
