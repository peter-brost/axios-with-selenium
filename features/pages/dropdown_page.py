from selenium.webdriver.common.by import By

class DropdownPage:
    def __init__(self, driver):
        self.driver = driver
        self.path = "dropdown"

    # Locators
    dropdown_locator = (By.ID, "dropdown")
    option_1_locator = (By.XPATH, "//option[@value='1']")
    option_2_locator = (By.XPATH, "//option[@value='2']")
    selected_option = (By.XPATH, "//option[@selected='selected']")

    # Helper methods

    def open(self, base_url):
        url = f"{base_url}{self.path}"
        self.driver.get(url)

    def select_option_1(self):
        self.driver.find_element(*self.dropdown_locator).click()
        self.driver.find_element(*self.option_1_locator).click()

    def select_option_2(self):
        self.driver.find_element(*self.dropdown_locator).click()
        self.driver.find_element(*self.option_2_locator).click()

    def get_selected_option_text(self):
        return self.driver.find_element(*self.selected_option).text
