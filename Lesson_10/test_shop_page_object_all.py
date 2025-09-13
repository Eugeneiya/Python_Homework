import pytest
from selenium import webdriver
from Shop_Pages.auth_page_all import Authorization
from Shop_Pages.shop_page_all import Shop
from Shop_Pages.cart_page_all import Cart
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


@allure.title("Тестирование сайта магазина одежды")
@allure.description("Тест проверяет корректность работы сайта, "
                    "в т.ч. формы заказа")
@allure.feature("Сайт магазина одежды")
@allure.severity(allure.severity_level.CRITICAL)

def test_shop(driver):
    """Тест проверяет авторизацию, добавление товаров
     в корзину, форму заказа"""
    with allure.step("Открытие страницы авторизации, авторизация"):
        auth_page = Authorization(driver)
        auth_page.open()
        auth_page.login_form()
    with allure.step("Добавление товаров в корзину"):
        shop_page = Shop(driver)
        shop_page.add_goods()
        shop_page.cart()
    with allure.step("Просмотр корзины, заполнение формы заказа, "
                     "проверка цены, закрытие формы"):
        cart_page = Cart(driver)
        cart_page.checkout_form()
        cart_page.total_price()
        cart_page.close_driver()
