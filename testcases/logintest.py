import time
import unittest

from selenium.webdriver.common.by import By
from pages.loginPage import LoginPage
from locators.browseropen import BrowserOpen


class MyTestCase(unittest.TestCase):

    def setUp(self):

        self.browser = BrowserOpen()

        self.driver = self.browser.chrome_browser()
        self.lp = LoginPage(self.driver)

    def test_login(self):
        # Perform login
        self.lp.login("testmorning", "test123")

        time.sleep(5)

        expected_result = "Welcome testmorning"

        actual_result = self.driver.find_element( By.ID,"nameofuser").text

        self.assertEqual(
            expected_result,
            actual_result,
            msg="Login Failed"
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()