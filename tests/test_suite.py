from tests.base_test import BaseTest
import time


class TheInternetTests(BaseTest):
    # TODO - doc string here

    def test_login_page(self):
        # TODO - doc string here
        self.login_page.open(path=self.login_page.path)
        self.login_page.login(username="tomsmith", password="SuperSecretPassword!")
        self.assertIn(self.secure_page.path, self.driver.current_url)
        self.assertTrue(self.driver.find_element(*self.secure_page.logout_button_locator).is_displayed())

