from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class Cart:
    def __init__(self, driver):
        """Конструктор класса Cart"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие корзины, заполнение формы заказа")
    def checkout_form(self):
        """Открывает корзину, заполняет форму заказа"""
        self.driver.find_element(By.CSS_SELECTOR, "[id='checkout']").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Eva")
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Adams")
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("223221")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Проверка общей стоимости заказа")
    def total_price(self):
        """Проверяет общую сумму заказа"""
        self.driver.implicitly_wait(4)
        total_price = self.driver.find_element(
            By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label").text
        total_price_value = float(total_price.split("$")[1])
        print(total_price)
        assert total_price_value == 58.29

    @allure.step("Закрытие сайта магазина одежды")
    def close_driver(self):
        """Закрывает сайт магазина одежды"""
        self.driver.quit()
