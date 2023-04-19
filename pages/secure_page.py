from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SecurePage(BasePage):
    # TODO - doc string here

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.path = "secure"

    # Locators
    logout_button_locator = (By.XPATH, "//i[text()=' Logout']")

    # Helper methods
    def click_logout_button(self):
        self.driver.find_element(*self.logout_button_locator).click()
