from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru")
    cookie_user1 ={
        "name": "SESSION",
        "value": "N2U4YjRjZDEtMzgwNy00ZGQ0LTk0MTMtZTIwMjVjZjk0Nzk5",
        "domain": "gitflic.ru"
    }
    cookie_user2 ={
        "name": "SESSION",
        "value": "OWMzZmQ5ZjYtOTg3ZC00MjM2LWI2MTctYWY4MjEzMmJkYWRk",
        "domain": "gitflic.ru"
    }
    driver.add_cookie(cookie_user1)
    driver.refresh()
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[text()='Мои проекты']"))
        )
    driver.get("https://gitflic.ru/profile")
    WebDriverWait(driver, 10).until(EC.url_contains("/user/"))
    url_user1 = driver.current_url
    print(f"URL пользователя 1: {url_user1}")

    driver.delete_all_cookies()
    driver.refresh()

    driver.add_cookie(cookie_user2)
    driver.refresh()
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[text()='Мои проекты']"))
    )
    driver.get("https://gitflic.ru/profile")
    WebDriverWait(driver, 10).until(EC.url_contains("/user/"))
    url_user2 = driver.current_url
    print(f"URL пользователя 2: {url_user2}")

    assert url_user1 != url_user2, f"URL профилей одинаковые: {url_user1}"
    print("Тест пройден, URL различаются.")
    driver.quit()
    
