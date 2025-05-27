from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

try:
    driver.get("http://localhost:9000/login.html")
    time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys("user@example.com")
    driver.find_element(By.NAME, "password").send_keys("user123")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)

    driver.get("http://localhost:9000/book.html")
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(2)
    if "book.html" in driver.current_url:
        print("✔ Negative test 1 passed: Empty form was blocked.")
    else:
        print("Negative test 1 failed: Empty form was submitted.")

    driver.refresh()
    time.sleep(1)
    driver.find_element(By.ID, "name").send_keys("Test User")
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(2)
    if "book.html" in driver.current_url:
        print("✔ Negative test 2 passed: Incomplete form was blocked.")
    else:
        print("Negative test 2 failed: Incomplete form was submitted.")

finally:
    driver.quit()
