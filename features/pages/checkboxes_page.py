from selenium.webdriver.common.by import By

class CheckBoxesPage:
    def __init__(self, driver):
        self.driver = driver
        self.path = "checkboxes"

    # Locators
    checkbox_1_locator = (By.XPATH, "//input[@type='checkbox'][1]")
    checkbox_2_locator = (By.XPATH, "//input[@type='checkbox'][2]")
    checkbox_1_label_locator = (By.XPATH, "//input[@type='checkbox'][1]/following-sibling::label")
    checkbox_2_label_locator = (By.XPATH, "//input[@type='checkbox'][2]/following-sibling::label")

    # Helper methods
    def open(self, base_url):
        url = f"{base_url}{self.path}"
        self.driver.get(url)

    def click_checkbox_1(self):
        self.driver.find_element(*self.checkbox_1_locator).click()

    def click_checkbox_2(self):
        self.driver.find_element(*self.checkbox_2_locator).click()
    
    def get_checkbox_1_status(self):
        return self.driver.find_element(*self.checkbox_1_locator).is_selected()
    
    def get_checkbox_2_status(self):
        return self.driver.find_element(*self.checkbox_2_locator).is_selected()
