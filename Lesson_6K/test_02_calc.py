from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


def test_calc():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    text_input = driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    text_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    text_input.send_keys("45")
    driver.find_element(By.XPATH, "//*[@id='calculator']/div[2]/span[1]").click()
    driver.find_element(By.XPATH, "//*[@id='calculator']/div[2]/span[4]").click()
    driver.find_element(By.XPATH, "//*[@id='calculator']/div[2]/span[2]").click()
    driver.find_element(By.XPATH, "//*[@id='calculator']/div[2]/span[15]").click()
    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.XPATH, "//*[@id='calculator']/div[1]/div"), "15"))
    res = driver.find_element(By.XPATH, "//*[@id='calculator']/div[1]/div").text
    assert res == "15"
    driver.quit()
