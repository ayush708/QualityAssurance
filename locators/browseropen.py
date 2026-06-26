from selenium import webdriver


class BrowserOpen:

    def chrome_browser(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.demoblaze.com")
        return driver

    def edge_browser(self):
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("https://www.demoblaze.com")
        return driver