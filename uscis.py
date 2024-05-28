from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
# "kyawsuhein.usird.client@gmail.com", aye aye paing, nandar shun let moe
 
emails = ['ayeayepaing.usird.client@gmail.com','ayechanmoe.usird.client@gmail.com','ayemyapwintphyu.usird.client@gmail.com','ayemyatmyataung.usird.client@gmail.com','ayenandarhtun.usird.client@gmail.com','ayethidawin.usird.client@gmail.com','eichomaung.usird.client@gmail.com','eithinzarkyaw.usird.client@gmail.com','estherparthasinmawi.usird.client@gmail.com','heinhtet.usird.client@gmail.com','hmweyuparlwin@usird.org','hsushoonmyat.usird.client@gmail.com','kapkhankhual.usird.client@gmail.com','khaingmyenaung.usird.client@gmail.com','khinekhinemon.usird.client@gmail.com','kyawsoelwin.usird.client@gmail.com','kyawsuhein.usird.client@gmail.com','kyawzaw.usird.client@gmail.com','kyileiyeeoo.usird.client@gmail.com','laihninaye.usird@gmail.com','linlettlaminn.usird.client@gmail.com','lwinmyohtun.usird.client@gmail.com','maymyatnoeeain.usird.client@gmail.com','maythucho.usird.client@gmail.com','minheinkyaw.usird.client@gmail.com','minniookyaw.usird.client@gmail.com','minsithumaung.usird.client@gmail.com','minthetkyaw.usird.client@gmail.com','minthutahtun.usird.client@gmail.com','moenar.usird.client@gmail.com','myatnoethirimaung.usird.client@gmail.com','myothihakyaw.usird.client@gmail.com','nandarshunletmoe.usird.client@gmail.com','naychi.usird.client@gmail.com','nilartun.usird.client@gmail.com','nuwahthein.usird.client@gmail.com','nyanminhtet.usird.client@gmail.com','oaksoekhant.usird.client@gmail.com','phyothida.usird.client@gmail.com','phyothinzaraung.usird.client@gmail.com','ryanwin720@gmail.com','sawhanthazaw.usird.client@gmail.com','shunlaethu.usird.client@gmail.com','shwechizarwin.usird@gmail.com','shweyeeoo.usird.client@gmail.com','sithuaung.usird.client@gmail.com','soethadarbo.usird.client@gmail.com','sumyatsan.usird.client@gmail.com','susuhlaing.usird.client@gmail.com','suthirisan.usird.client@gmail.com','swesinayemyanyo.usird.client@gmail.com','theinhtikezaw.usird.client@gmail.com','thethtartinzar.usird.client@gmail.com','thetkhaingoo.usird.client@gmail.com','thinzaraung.usird.client@gmail.com','thirimyatnoe.usird.client@gmail.com','tintinthein.usird.client@gmail.com','waiyanlinmaung.usird.client@gmail.com','wunna.usird.client@gmail.com','yairyinthtun.usird.client@gmail.com','yaminthawthawhtut.usird.client@gmail.com','yeeyeekhin.usird.client@gmail.com','zarzarmoe.usird.client@gmail.com','zayarlinnhtet.usird.client@gmail.com']

password = "AsylumGranted2023$"

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
