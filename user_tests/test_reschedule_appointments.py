from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
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

    cards = driver.find_elements(By.CLASS_NAME, "appointment-card")
    if not cards:
        print("No appointments to reschedule.")
    else:
        card = cards[0]
        reschedule_btn = card.find_element(By.XPATH, ".//button[text()='Reschedule']")
        onclick_value = reschedule_btn.get_attribute("onclick")
        app_id = onclick_value.split("'")[1]
        reschedule_btn.click()
        time.sleep(1)

        tomorrow = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
        driver.find_element(By.ID, f"newDate-{app_id}").send_keys(tomorrow)
        time.sleep(1)

        time_select = driver.find_element(By.ID, f"newTime-{app_id}")
        options_list = time_select.find_elements(By.TAG_NAME, "option")

        booked_slots = [opt.text for opt in options_list if opt.get_attribute("disabled")]
        print("🔒 Booked (disabled) slots:", booked_slots)

        new_time = None
        for opt in options_list:
            if opt.get_attribute("value") and not opt.get_attribute("disabled"):
                new_time = opt.get_attribute("value")
                opt.click()
                break

        if not new_time:
            print("No available time to reschedule.")
            driver.quit()
            exit()

        driver.find_element(By.XPATH, f"//div[@id='reschedule-{app_id}']//button[text()='Submit']").click()
        time.sleep(2)

        try:
            Alert(driver).accept()
        except NoAlertPresentException:
            pass

        driver.refresh()
        time.sleep(2)
        updated_card = driver.find_elements(By.CLASS_NAME, "appointment-card")[0]
        updated_text = updated_card.text

        if new_time in updated_text:
            print(f"✔ Reschedule test passed: Time updated to {new_time}")
        else:
            print("Reschedule test failed: Time not updated.")

finally:
    driver.quit()
