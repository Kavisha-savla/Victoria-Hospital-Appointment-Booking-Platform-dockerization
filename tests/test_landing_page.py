from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("http://localhost:9000")
time.sleep(1)
print("Page title is:", driver.title)

assert "Victoria Multi Speciality Hospital" in driver.title
print("✔ Title is correct")

assert driver.find_element(By.LINK_TEXT, "Login").get_attribute("href").endswith("/login.html")
assert driver.find_element(By.LINK_TEXT, "Register").get_attribute("href").endswith("/register.html")
print("✔ Navbar links found")

assert "Book Appointments Easily" in driver.page_source
assert "Your health is our highest priority." in driver.page_source
print("✔ Hero content verified")

book_btn = driver.find_element(By.CLASS_NAME, "btn")
assert book_btn.get_attribute("href").endswith("/login.html")
print("✔ Book Appointment button is functional")

testimonials = driver.find_elements(By.CLASS_NAME, "testimonial")
assert len(testimonials) == 3
print("✔ 3 testimonials found")

assert "support@victoriahospital.com" in driver.page_source
assert "+61 1800 000 911" in driver.page_source
print("✔ Footer contact details verified")

driver.quit()
print("✔ Landing page test passed!")
