import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com")

    def test_login(self):
        driver = self.driver

        nav_login = driver.find_element(By.ID, "login2")
        nav_login.click()
        driver.implicitly_wait(10)
        login_username = driver.find_element(By.ID, "loginusername")
        login_password = driver.find_element(By.ID, "loginpassword")
        login_username.send_keys("testmorning")
        login_password.send_keys("test123")
        login_button = driver.find_element("xpath", '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        login_button.click()
        time.sleep(5)
        expected_result = "Welcome testmorning"
        actual_result = driver.find_element(By.ID, "nameofuser").text
        self.assertEqual(expected_result, actual_result, "Login failed: Expected and actual results do not match.")


    def tearDown(self):
        self.driver.quit()







if __name__ == '__main__':
    unittest.main()
