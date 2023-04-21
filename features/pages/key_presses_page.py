from selenium.webdriver.common.by import By

class KeyPressesPage:
    def __init__(self, driver):
        self.driver = driver
        self.path = "key_presses"

    # Locators
    text_input_locator = (By.ID, "target")
    result_text_locator = (By.ID, "result")

    # Helper methods
    def open(self, base_url):
        url = f"{base_url}{self.path}"
        self.driver.get(url)

    def enter_text(self, text):
        self.driver.find_element(*self.text_input_locator).send_keys(text)

    def get_result_text(self):
        return self.driver.find_element(*self.result_text_locator).text
