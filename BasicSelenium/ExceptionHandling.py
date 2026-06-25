import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com")
try:
    nav_login = driver.find_element(By.ID, "login2")
    nav_login.click()
    login_username = driver.find_element(By.ID, "loginusername")
    login_password = driver.find_element(By.ID, "loginpassword")
    login_username.send_keys("testmorning")
    login_password.send_keys("test123")
    login_button = driver.find_element("xpath", '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    login_button.click()
    time.sleep(5)

except ElementNotInteractableException as e:
    print(f"ElementNotInteractableException on line: ", e)
    driver.implicitly_wait(10)
    login_username = driver.find_element(By.ID, "")
    login_password = driver.find_element(By.ID, "loginpassword")
    login_username.send_keys("testmorning")
    login_password.send_keys("test123")
    login_button = driver.find_element("xpath", '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    login_button.click()
    time.sleep(5)

except Exception as e:
    print("An unexpected exception occurred: ", e)


finally:
    driver.quit()

