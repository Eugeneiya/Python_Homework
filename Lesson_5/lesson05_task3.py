from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/inputs")

sleep(3)

input_field = driver.find_element(By.CSS_SELECTOR, "input")

input_field.send_keys("sky")

sleep(3)

input_field.clear()

input_field.send_keys("Pro")

sleep(3)
driver.quit()
