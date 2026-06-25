import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.demoblaze.com")
nav_login = driver.find_element(By.ID, "login2")
nav_login.click()
wait = WebDriverWait(driver, 10)

login_username = wait.until(EC.element_to_be_clickable((By.ID, "loginusername")))
login_password = driver.find_element(By.ID, "loginpassword")
login_username.send_keys("testmorning")
login_password.send_keys("test123")
login_button = driver.find_element("xpath" , '//*[@id="logInModal"]/div/div/div[3]/button[2]')
login_button.click()
time.sleep(5)