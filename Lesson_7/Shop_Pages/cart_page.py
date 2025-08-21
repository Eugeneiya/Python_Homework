from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def checkout_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "[id='checkout']").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Eva")
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Adams")
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("223221")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def total_price(self):
        self.driver.implicitly_wait(4)
        total_price = self.driver.find_element(
            By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label").text
        total_price_value = float(total_price.split("$")[1])
        print(total_price)
        assert total_price_value == 58.29

    def close_driver(self):
        self.driver.quit()
