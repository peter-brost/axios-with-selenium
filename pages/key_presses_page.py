from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class KeyPressesPage(BasePage):
    # TODO - doc string here

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.path = "key_presses"

    # Locators
    text_input_locator = (By.ID, "target")
    result_text_locator = (By.ID, "result")

    # Helper methods
    def enter_text(self, text):
        self.driver.find_element(*self.text_input_locator).send_keys(text)

    def get_result_text(self):
        return self.driver.find_element(*self.result_text_locator).text
    