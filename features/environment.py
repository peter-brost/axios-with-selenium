from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.checkboxes_page import CheckBoxesPage
from pages.dropdown_page import DropdownPage
from pages.login_page import LoginPage
from pages.key_presses_page import KeyPressesPage


BASE_URL = 'https://the-internet.herokuapp.com/'

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()

    context.base_url = BASE_URL
    context.add_remove_elements_page = AddRemoveElementsPage(context.driver)
    context.checkboxes_page = CheckBoxesPage(context.driver)
    context.dropdown_page = DropdownPage(context.driver)
    context.key_presses_page = KeyPressesPage(context.driver)
    context.login_page = LoginPage(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()
