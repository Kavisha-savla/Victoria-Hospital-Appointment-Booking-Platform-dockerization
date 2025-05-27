from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime, timedelta

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
    driver.find_element(By.ID, "name").send_keys("Test User")
    driver.find_element(By.ID, "age").send_keys("25")
    driver.find_element(By.ID, "phone").send_keys("9876543210")
    driver.find_element(By.ID, "gender").send_keys("Female")
    driver.find_element(By.ID, "department").send_keys("Cardiology")
    driver.find_element(By.ID, "service").send_keys("Consultation")
    tomorrow = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    driver.find_element(By.ID, "date").send_keys(tomorrow)
    driver.find_element(By.ID, "time").send_keys("11:00 AM")
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(1)

    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"✔ Alert text: {alert.text}")
        alert.accept()
        print("✔ Alert accepted.")
    except TimeoutException:
        print("✖ No alert was detected.")

    time.sleep(1)

    if "dashboard.html" in driver.current_url:
        print("✔ Booking test passed!")
    else:
        print("✖ Booking test failed.")

finally:
    time.sleep(2)
    driver.quit()
