import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

@pytest.fixture
def driver():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Recommended headless argument
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Initialize WebDriver (Selenium 4.6+ handles drivers automatically)
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    # Teardown
    driver.quit()

def test_webapp_title_and_button(driver):
    # We are now testing the local file checked out by GitHub Actions
    # It will be located in the 'webapp-demo' folder
    
    html_file_path = os.path.abspath(os.path.join(os.getcwd(), "webapp-demo", "index.html"))
    local_file_url = f"file:///{html_file_path.replace(os.sep, '/')}"
    
    print(f"Testing local file: {local_file_url}")
    driver.get(local_file_url)
    
    # Give it a second to load
    time.sleep(1)

    # Assertions
    assert "Practice Web App" in driver.title
    
    # Find the button and click it
    button = driver.find_element(By.ID, "clickMeBtn")
    assert button.is_displayed()
    button.click()
    
    # Verify the message
    message_div = driver.find_element(By.ID, "message")
    assert message_div.text == "Button Clicked Successfully!"
    print("Test passed successfully!")
