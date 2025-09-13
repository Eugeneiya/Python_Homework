import pytest
from selenium import webdriver
from Calc_Classes.calculator_page_all import Calculator
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы калькулятора "
                    "с учетом задержки по времени отклика")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)


def test_calc(driver):
    """Тест проверяет работу калькулятора с учетом задержки"""
    with allure.step("Открытие страницы калькулятора"):
        calculator_page = Calculator(driver)
        calculator_page.open()
    with allure.step("Установка задержки калькулятора"):
        calculator_page.waiting_time()
    with allure.step("Нажатие кнопок для вычисления"):
        calculator_page.calculation()
    with allure.step("Вывод результата"):
        calculator_page.result()
    with allure.step("Закрытие страницы калькулятора"):
        calculator_page.close_driver()
