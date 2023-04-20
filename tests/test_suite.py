from tests.base_test import BaseTest
import random
import string
import time


class TheInternetTests(BaseTest):
    # TODO - doc string here

    def test_login_page(self):
        # TODO - doc string here
        self.login_page.open(path=self.login_page.path)
        self.login_page.login(username="tomsmith", password="SuperSecretPassword!")
        self.assertIn(self.secure_page.path, self.driver.current_url)
        self.assertTrue(self.driver.find_element(*self.secure_page.logout_button_locator).is_displayed())

    def test_key_presses_page(self):
        # TODO - doc string here
        self.key_presses_page.open(path=self.key_presses_page.path)
        character = random.choice(string.ascii_uppercase)
        self.key_presses_page.enter_text(character)
        self.assertEqual(self.key_presses_page.get_result_text(), f"You entered: {character}")

    def test_add_remove_elements_page(self):
        # TODO - doc string here
        self.add_remove_elements_page.open(path=self.add_remove_elements_page.path)
        number = random.randint(1, 5)
        for i in range(number):
            self.add_remove_elements_page.click_add_element_button()
            time.sleep(.25)
        element_count = self.add_remove_elements_page.get_delete_element_button_count()
        self.assertEqual(element_count, number)

    def test_checkboxes_page(self):
        # TODO - doc string here
        self.checkboxes_page.open(path=self.checkboxes_page.path)
        self.checkboxes_page.click_checkbox_1()
        self.checkboxes_page.click_checkbox_2()
        self.assertTrue(self.checkboxes_page.get_checkbox_1_status())
        self.assertFalse(self.checkboxes_page.get_checkbox_2_status())
