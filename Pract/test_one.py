
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# Create a new instance of the Chrome driver

driver = webdriver.Chrome()


# Navigate to a website
driver.get("https://google.com")
assert driver.title == "Google"
driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys('website for product' )
driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(Keys.ENTER)
time.sleep(3)
