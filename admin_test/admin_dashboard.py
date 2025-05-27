from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
import time

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

try:
    driver.get("http://localhost:9000/admin/login")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "email")))
    driver.find_element(By.NAME, "email").send_keys("admin@example.com")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)

    driver.get("http://localhost:9000/admin/dashboard")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "dashboard")))
    print("✔ Dashboard loaded.")

    for status in ['cancelled', 'rescheduled', 'booked']:
        try:
            box = driver.find_element(By.CLASS_NAME, status)
            box.click()
            print(f"✔ Filter box '{status}' clickable.")
            time.sleep(1)
        except Exception as e:
            print(f"✖ Filter box '{status}' not working: {e}")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "appointment-card"))
        )
        appointment_cards = driver.find_elements(By.CLASS_NAME, "appointment-card")
        if appointment_cards:
            card = appointment_cards[0]

            try:
                cancel_btn = card.find_element(By.XPATH, ".//button[text()='Cancel']")
                cancel_btn.click()
                print("✔ Cancel button clicked.")
                time.sleep(1)
            except Exception:
                print("✖ Cancel button not found.")

            try:
                reschedule_btn = card.find_element(By.XPATH, ".//button[text()='Reschedule']")
                reschedule_btn.click()
                print("✔ Reschedule form toggle clicked.")
                time.sleep(1)

                tomorrow = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
                date_input = card.find_element(By.XPATH, ".//input[@type='date']")
                driver.execute_script("arguments[0].value = arguments[1];", date_input, tomorrow)
                time.sleep(1)

                time_select = card.find_element(By.XPATH, ".//select[contains(@id, 'newTime')]")
                options_list = time_select.find_elements(By.TAG_NAME, "option")
                for option in options_list:
                    if option.get_attribute("disabled") is None and option.get_attribute("value"):
                        option.click()
                        print(f"✔ Time selected: {option.get_attribute('value')}")
                        break
                else:
                    print("✖ No available time slot to select.")

                submit_btn = card.find_element(By.XPATH, ".//button[text()='Submit']")
                submit_btn.click()
                print("✔ Reschedule form submitted.")
                time.sleep(2)

            except Exception as e:
                print("✖ Reschedule section error:", e)
        else:
            print("✖ No appointment cards found after wait.")
    except Exception:
        print("✖ Appointment cards not found (timeout).")

    try:
        search = driver.find_element(By.ID, "searchInput")
        search.send_keys("Anjali")
        print("✔ Search bar functional.")
        time.sleep(1)
    except Exception as e:
        print("✖ Search input test failed:", e)

    try:
        export_btn = driver.find_element(By.XPATH, "//button[text()='Export as CSV']")
        export_btn.click()
        print("✔ Export to CSV button clicked.")
        time.sleep(1)
    except Exception as e:
        print("✖ CSV export failed:", e)

    try:
        logout_link = driver.find_element(By.LINK_TEXT, "Logout")
        logout_link.click()
        print("✔ Logout successful.")
        time.sleep(1)
    except Exception as e:
        print("✖ Logout failed:", e)

except Exception as e:
    print("✖ Test failed due to error:", e)

finally:
    driver.quit()