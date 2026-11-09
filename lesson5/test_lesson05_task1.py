import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    time.sleep(3)
    driver.find_element(
        By.LINK_TEXT, "HTML Form").click()
    time.sleep(3)
    assert driver.current_url == "https://httpbin.qa-territory.online/forms/post"
    driver.back()
    time.sleep(3)
    driver.quit()