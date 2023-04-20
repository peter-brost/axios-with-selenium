from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from pages.key_presses_page import KeyPressesPage


class BaseTest(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver instance
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.key_presses_page = KeyPressesPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.secure_page = SecurePage(self.driver)

    def tearDown(self):
        # Quit the WebDriver instance
        self.driver.quit()
