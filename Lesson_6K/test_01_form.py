from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By

service = EdgeService(
       executable_path="C:\\Users\\Eugenia\\Downloads\\edgedriver_win64\\msedgedriver.exe")

driver = webdriver.Edge(service=service)


def test_form():
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(10)
    first_name = driver.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")
    last_name = driver.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")
    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")
    zip_code = driver.find_element(By.NAME, "zip-code")
    zip_code.send_keys("")
    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")
    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")
    mail = driver.find_element(By.NAME, "e-mail")
    mail.send_keys("test@skypro.com")
    phone = driver.find_element(By.NAME, "phone")
    phone.send_keys("+7985899998787")
    position = driver.find_element(By.NAME, "job-position")
    position.send_keys("QA")
    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    driver.implicitly_wait(20)
    zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert zip_code == "alert py-2 alert-danger"
    other_fields = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#job-position", "#company"]
    for field in other_fields:
        field_class = driver.find_element(By.CSS_SELECTOR, field).get_attribute("class")
    assert field_class == "alert py-2 alert-success"
    driver.quit()
