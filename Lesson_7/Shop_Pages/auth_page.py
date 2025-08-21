from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Authorization:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
    
    def open(self):
        self.driver.get("https://www.saucedemo.com")

    def login_form(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(
            By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
