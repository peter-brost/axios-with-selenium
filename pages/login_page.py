from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # TODO - doc string here

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.path = "login"

    # Locators
    username_input_locator = (By.ID, "username")
    password_input_locator = (By.ID, "password")
    login_button_locator = (By.CSS_SELECTOR, "button[type='submit']")

    # Helper methods
    def enter_username(self, username):
        self.driver.find_element(*self.username_input_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input_locator).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_locator).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
