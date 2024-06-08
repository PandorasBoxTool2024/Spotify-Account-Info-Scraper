import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from getInformations import getInformations

# Set up the WebDriver with headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")  # necessary for headless mode to work properly on Windows
chrome_options.add_argument("--window-size=1920x1080")  # Optional: Set window size for screenshots or if needed

driver = webdriver.Chrome(options=chrome_options)

try:
    # Go to the Spotify login page
    driver.get("https://accounts.spotify.com/de/login")

    # Wait until the elements are present
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.presence_of_element_located((By.ID, "login-username")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "login-password")))
    login_button = wait.until(EC.presence_of_element_located((By.ID, "login-button")))

    # Enter the email and password (replace with actual credentials)
    email_field.send_keys("Your email address here (Spotify)")
    password_field.send_keys("Your password here (Spotify)")

    # Click the login button
    login_button.click()

    # Optionally, add a delay to observe the process
    time.sleep(4)

    # Retrieve and print all cookies
    cookies = driver.get_cookies()

    # Initialize variables to store the values of sp_dc and sp_key
    sp_dc = None
    sp_key = None

    for cookie in cookies:
        if cookie['name'] == 'sp_dc':
            sp_dc = cookie['value']
        elif cookie['name'] == 'sp_key':
            sp_key = cookie['value']

    # Print the values of sp_dc and sp_key
    if sp_dc and sp_key:
        #print(f"sp_dc: {sp_dc}")
        #print(f"sp_key: {sp_key}")
        getInformations(sp_dc, sp_key)
    else:
        print("The required cookies were not found.")
finally:
    # Close the browser
    driver.quit()
