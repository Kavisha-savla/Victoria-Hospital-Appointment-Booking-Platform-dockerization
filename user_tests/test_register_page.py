from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get("http://localhost:9000/register.html")
time.sleep(1)

driver.find_element(By.NAME, "name").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
driver.find_element(By.NAME, "password").send_keys("strongpassword123")

driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)

try:
    alert = Alert(driver)
    alert_text = alert.text
    print(f"✔ Alert message: {alert_text}")
    alert.accept()
    print("✔ Registration test passed (alert shown).")
except:
    current_url = driver.current_url
    if "login.html" in current_url:
        print("✔ Registration test passed (redirected to login).")
    else:
        print("Registration test failed. No alert or redirect.")

driver.quit()
