from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calculator:
    def __init__(self, driver):
        """Конструктор класса Calculator"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """Открывает страницу калькулятора"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка времени задержки в секундах")
    def waiting_time(self):
        """Устанавливает задержку для выполнения операций на калькуляторе."""
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    @allure.step("Нажатие кнопок калькулятора для выполнения вычисления")
    def calculation(self):
        """Нажимает на кнопки калькулятора"""
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        WebDriverWait(self.driver, 45).until(
           EC.text_to_be_present_in_element((By.XPATH, "//*[@id='calculator']/div[1]/div"), "15"))

    @allure.step("Получение и проверка результата вычисления")
    def result(self):
        """Возвращает текущий результат с экрана калькулятора"""
        res = self.driver.find_element(By.XPATH, "//*[@id='calculator']/div[1]/div").text
        return res == "15"

    @allure.step("Закрытие страницы калькулятора")
    def close_driver(self):
        """Закрывает калькулятор"""
        self.driver.quit()
