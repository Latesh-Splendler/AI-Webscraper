from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_website(website):
    print("Launching Chrome browser...")

    # Use webdriver-manager to auto-install ChromeDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (important for cloud deployment)
    options.add_argument("--no-sandbox")  # Bypass OS security restrictions
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources issues

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(website)
        print("Page loaded....")
        html = driver.page_source
        time.sleep(5)

        return html
    finally:
        driver.quit()
