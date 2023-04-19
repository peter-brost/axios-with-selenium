from base_test import BaseTest

class ExampleTest(BaseTest):
    def test_example(self):
        # Load a webpage and check its title
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)
