from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AddRemoveElementsPage(BasePage):
    # TODO - doc string here

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.path = "add_remove_elements/"

    # Locators
    add_element_button_locator = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    delete_element_button_locator = (By.CSS_SELECTOR, "button[onclick='deleteElement()']")

    # Helper methods
    def click_add_element_button(self):
        self.driver.find_element(*self.add_element_button_locator).click()

    def click_delete_element_button(self):
        self.driver.find_element(*self.delete_element_button_locator).click()
    
    def get_delete_element_button_count(self):
        return len(self.driver.find_elements(*self.delete_element_button_locator))
    