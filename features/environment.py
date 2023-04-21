from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.dropdown_page import DropdownPage
from pages.login_page import LoginPage
from pages.key_presses_page import KeyPressesPage
from pages.checkboxes_page import CheckBoxesPage
from pages.add_remove_elements_page import AddRemoveElementsPage

def create_webdriver_instance(context, test_type):
    chrome_options = Options()

    if test_type == "mobile":
        mobile_emulation = {"deviceName": "iPhone X"}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    else:
        chrome_options.add_argument("start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def before_scenario(context, scenario):
    test_type = "desktop" if "desktop" in context.feature.filename else "mobile"
    context.driver = create_webdriver_instance(context, test_type)

    # Initialize page objects
    context.dropdown_page = DropdownPage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.key_presses_page = KeyPressesPage(context.driver)
    context.checkboxes_page = CheckBoxesPage(context.driver)
    context.add_remove_elements_page = AddRemoveElementsPage(context.driver)

    context.base_url = "https://the-internet.herokuapp.com/"

def after_scenario(context, scenario):
    context.driver.quit()
