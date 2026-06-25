import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")


# Alert with OK
ok_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
ok_nav.click()
button_ok = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button')
button_ok.click()
time.sleep(3)
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)

# Alert with OK & Cancel
ok_cancel_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
ok_cancel_nav.click()
button_ok_cancel = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button')
button_ok_cancel.click()
time.sleep(3)
alert.dismiss()
time.sleep(3)

# Alert with Textbox
textbox_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
textbox_nav.click()
button_textbox = driver.find_element(By.XPATH, '//*[@id="Textbox"]/button')
button_textbox.click()
time.sleep(3)
alert.send_keys("PSBP Students")
alert.accept()
time.sleep(3)
