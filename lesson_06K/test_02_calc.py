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
    submit_button_1 = driver.find_element(By.XPATH, "//span[text()='7']")  
    submit_button_1.click()
    submit_button_2 = driver.find_element(By.XPATH, "//span[text()='+']")  
    submit_button_2.click()
    submit_button_3 = driver.find_element(By.XPATH, "//span[text()='8']")  
    submit_button_3.click()
    submit_button_4 = driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning']")  
    submit_button_4.click()
    window_field = WebDriverWait(driver, 45).until( 
    EC.presence_of_element_located((By.XPATH, "//input[@id='delay']"))), "Результат 15 через 45 секунд"
    driver.quit()