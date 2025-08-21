import pytest
from selenium import webdriver
from Calc_Classes.calculator_page import Calculator


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
    calculator_page = Calculator(driver)
    calculator_page.open()
    calculator_page.waiting_time()
    calculator_page.calculation()
    calculator_page.result()
    calculator_page.close_driver()
