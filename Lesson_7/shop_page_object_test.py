import pytest
from selenium import webdriver
from Shop_Pages.auth_page import Authorization
from Shop_Pages.shop_page import Shop
from Shop_Pages.cart_page import Cart


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    auth_page = Authorization(driver)
    auth_page.open()
    auth_page.login_form()

    shop_page = Shop(driver)
    shop_page.add_goods()
    shop_page.cart()

    cart_page = Cart(driver)
    cart_page.checkout_form()
    cart_page.total_price()
    cart_page.close_driver()
