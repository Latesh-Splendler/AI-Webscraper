from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def scrape_website(website):
    print("Launching Chrome browser...")

    # Set up Chrome options
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode
    options.add_argument("--no-sandbox")  # Bypasses OS security model
    options.add_argument("--disable-dev-shm-usage")  # Helps with low-memory issues

    # Automatically get the correct ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(website)
        print("Page loaded...")

        # Wait until the page is fully loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        html = driver.page_source
        return html

    finally:
        driver.quit()
