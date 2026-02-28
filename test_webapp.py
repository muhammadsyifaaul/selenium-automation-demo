import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
BASE_URL = os.getenv("BASE_URL")


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    driver.quit()

def test_webapp_title_and_button(driver):
    
    driver.get(BASE_URL)   
    
    time.sleep(1)

    assert "Practice Web App" in driver.title

    button = driver.find_element(By.ID, "clickMeBtn")
    assert button.is_displayed()
    button.click()
    

    message_div = driver.find_element(By.ID, "message")
    assert message_div.text == "Button Clicked Successfully!"
    print("Test passed successfully!")
