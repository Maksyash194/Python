from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_L6K():
    driver = webdriver.Edge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").clear()
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    wait = WebDriverWait(driver, 10)
    zip_code_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_code_field.get_attribute("class"), "Поле zip code должно быть красным"

    green_fields_ids = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "job-position", "company"
    ]

    for field_id in green_fields_ids:
        field = driver.find_element(By.ID, field_id)
        field_classes = field.get_attribute('class')
        assert "alert-success" in field_classes, f"Поле {field_id} должно быть зеленым, классы:{field_classes}"
    driver.quit()