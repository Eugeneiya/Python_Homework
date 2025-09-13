from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Shop:
    def __init__(self, driver):
        """Конструктор класса Shop"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Добавление товаров в корзину")
    def add_goods(self):
        """Добавляет товары в корзину"""
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переход в корзину")
    def cart(self):
        """Нажимает на кнопку корзины"""
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#shopping_cart_container > a > span")))
        self.driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span").click()
