from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

sleep(2)

blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
blue_button.click

sleep(5)
driver.quit()
