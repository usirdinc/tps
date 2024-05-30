from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
 
emails = []

password = ""

for email in emails:
    success = False
    while not success:
        try:
            service = Service(executable_path="chromedriver.exe")
            driver = webdriver.Chrome(service=service)

            driver.get("https://myaccount.uscis.gov/")

            # Wait until the email input field is present
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "user[email]")))
            input_element = driver.find_element(By.NAME, "user[email]")
            input_element.send_keys(email + Keys.TAB + password + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)

            # # Define the Google Sheet URL and the email to search for
            google_sheet_url = 'https://docs.google.com/spreadsheets/d/1FxOusbdVAqqh76If-KQ5Xpf1_3rn3CD4cOwp2RzYBwg/edit?usp=sharing'

            # # Open the Google Sheet in a new tab
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(google_sheet_url)

            # # Wait until the Google Sheet is loaded
            # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "docs-title-inner")))
            time.sleep(90)
            # # Perform Ctrl + F to open the search box and search for the email
            search_box = driver.switch_to.active_element
            search_box.send_keys(Keys.CONTROL , 'f')

            search_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "docs-findinput-input")))
            search_box.send_keys(email + Keys.ENTER)
            time.sleep(1)
            search_box.send_keys(Keys.ESCAPE, Keys.TAB, Keys.CONTROL, 'c')
            time.sleep(5)

            # # Switch back to the USCIS tab and paste the copied content
            driver.switch_to.window(driver.window_handles[0])

            # # Wait until the code input field is present
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "code")))
            vcode = driver.find_element(By.NAME, "code")
            vcode.send_keys(Keys.CONTROL + 'v' + Keys.TAB + Keys.ENTER)

            # # Switch to the dashboard tab and click on the button
            driver.switch_to.window(driver.window_handles[2])
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "myuscis-dashboard")))
            clickbtn = driver.find_element(By.CLASS_NAME, "myuscis-dashboard")
            clickbtn.click()
            time.sleep(5)

            # # Wait until the case status is present and get the text
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "panel-title")))
            casestatus = driver.find_element(By.CLASS_NAME, "panel-title")
            time.sleep(3)
            casestatusnotes = casestatus.text

            # # Switch back to the Google Sheet tab and fill in the case status notes
            driver.switch_to.window(driver.window_handles[1])
            fillbox = driver.switch_to.active_element
            fillbox.send_keys(Keys.CONTROL + 'f')

            fillbox = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "docs-findinput-input")))
            fillbox.send_keys(email + Keys.ENTER)
            time.sleep(5)
            fillbox.send_keys(Keys.ESCAPE, Keys.TAB, Keys.TAB, Keys.TAB, casestatusnotes, Keys.ENTER)
            time.sleep(10)

            driver.quit()
            success = True
        except Exception as e:
            print(f"An error occurred: {e}")
            driver.quit()
            time.sleep(5)
