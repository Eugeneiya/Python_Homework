from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()
driver.get("https://www.saucedemo.com")

user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
user_name.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys("secret_sauce")

driver.find_element(By.CSS_SELECTOR, "#login-button").click()
             
backpack = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
backpack = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
backpack.click()

shirt = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")))
shirt = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
shirt.click()

onesie = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")))
onesie = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
onesie.click()

basket = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#shopping_cart_container > a > span")))
basket = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span")
basket.click()

checkout = driver.find_element(By.CSS_SELECTOR, "#checkout")
checkout.click()

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.send_keys("Eva")

last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.send_keys("Adams")

postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
postal_code.send_keys("223221")

contin = driver.find_element(By.CSS_SELECTOR, "#continue")
contin.click()

total_price = driver.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label").text
total_price_value = float(total_price.split("$")[1])
print(total_price)

assert total_price_value == 58.29
driver.quit()
