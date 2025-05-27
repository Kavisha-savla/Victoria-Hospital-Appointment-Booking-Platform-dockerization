from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("http://localhost:9000/login.html")
time.sleep(1)

driver.find_element(By.NAME, "email").send_keys("user@example.com")
driver.find_element(By.NAME, "password").send_keys("user123")
driver.find_element(By.ID, "loginButton").click()
time.sleep(2)

if "User Dashboard" in driver.page_source or "dashboard" in driver.current_url:
    print("✔ User login test passed!")
else:
    print("User login test failed!")


driver.quit()
print("✔ Test finished. Browser closed.")