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

    driver.get("http://localhost:9000/dashboard.html")
    time.sleep(2)

    appointments = driver.find_elements(By.CLASS_NAME, "appointment-card")
    initial_count = len(appointments)

    if initial_count == 0:
        print("No appointments to cancel.")
    else:
        cancel_button = appointments[0].find_element(By.XPATH, ".//button[text()='Cancel']")
        cancel_button.click()
        print("Canceling appointment...")
        time.sleep(3)

        driver.refresh()
        time.sleep(2)
        new_appointments = driver.find_elements(By.CLASS_NAME, "appointment-card")

        if len(new_appointments) < initial_count:
            print("✔ Cancel test passed: Appointment removed from dashboard.")
        else:
            print("Cancel test failed: Appointment still present.")

finally:
    driver.quit()
