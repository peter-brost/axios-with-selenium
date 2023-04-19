from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver instance
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def tearDown(self):
        # Quit the WebDriver instance
        self.driver.quit()
