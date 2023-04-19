from selenium.webdriver.common.by import By


class BasePage:
    base_url = "https://the-internet.herokuapp.com/"

    def __init__(self, driver):
        self.driver = driver
        

    def open(self, path=""):
        self.driver.get(self.base_url + path)
