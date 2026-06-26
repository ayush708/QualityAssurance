from selenium.webdriver.common.by import By
from locators.locate import Locator


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.lc = Locator()

    def login(self, username, password):
        driver = self.driver
        lc = self.lc

        driver.find_element(By.ID, lc.n_l_id).click()
        driver.implicitly_wait(10)

        driver.find_element(By.ID, lc.lu_id).send_keys(username)
        driver.find_element(By.ID, lc.lp_id).send_keys(password)

        driver.find_element(By.XPATH, lc.lb_xpath).click()