from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class Authorization:
    def __init__(self, driver):
        """Конструктор класса Authorization"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы авторизации")
    def open(self):
        """Открывает страницу авторизации"""
        self.driver.get("https://www.saucedemo.com")

    @allure.step("Ввод логина и пароля, нажатие на кнопку 'Login'")
    def login_form(self):
        """Заполняет форму авторизации, нажимает на кнопку 'Login'"""
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(
            By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
