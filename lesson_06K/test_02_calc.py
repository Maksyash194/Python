from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_L6K():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    input_delay = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    input_delay.send_keys("45")
    submit_button_7 = driver.find_element(By.XPATH, "//span[text()='7']")  

    driver.quit()