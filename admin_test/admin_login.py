from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

URL = "http://localhost:9000/admin/login"  
VALID_EMAIL = "admin@example.com"             
VALID_PASSWORD = "admin123"
INVALID_EMAIL = "notanemail"
INVALID_PASSWORD = "wrongpass"

def wait(seconds=1):
    time.sleep(seconds)

def reset_and_open():
    driver.get(URL)
    wait()

def print_result(condition, description):
    print(f"✔ {description}" if condition else f" {description} FAILED")

reset_and_open()
print_result("Victoria Multi Speciality Hospital" in driver.page_source, "Page loaded and title visible")

email_input_exists = False
try:
    driver.find_element(By.ID, "email")
    email_input_exists = True
except NoSuchElementException:
    pass
print_result(email_input_exists, "Email input field is present")

password_input_exists = False
try:
    driver.find_element(By.ID, "password")
    password_input_exists = True
except NoSuchElementException:
    pass
print_result(password_input_exists, "Password input field is present")

login_button_exists = False
try:
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button_exists = True
except NoSuchElementException:
    pass
print_result(login_button_exists, "Login button is present")

reset_and_open()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
wait()
print_result(URL in driver.current_url, "Form not submitted with empty fields (client-side validation)")

reset_and_open()
driver.find_element(By.ID, "email").send_keys(INVALID_EMAIL)
driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
wait()
print_result(URL in driver.current_url, "Form not submitted with invalid email format (client-side validation)")

reset_and_open()
driver.find_element(By.ID, "email").send_keys("wrong@example.com")
driver.find_element(By.ID, "password").send_keys(INVALID_PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
wait(2)
print_result("Invalid" in driver.page_source or URL in driver.current_url, "Login failed with wrong credentials")

reset_and_open()
driver.find_element(By.ID, "email").send_keys(VALID_EMAIL)
driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
wait(2)
print_result("Admin Dashboard" in driver.page_source or "admin/dashboard" in driver.current_url, "Login successful with correct credentials")

driver.quit()
print("✔ All admin login tests completed.")