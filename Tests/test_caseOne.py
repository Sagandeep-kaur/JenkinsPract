import pytest
from base_test  import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class Test_Selenium_Demo(BaseTest):


    def test_one(self):
        self.driver.get("https://google.com")
        assert self.driver.title == "Google"
        self.driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys('website for product' )
        self.driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(Keys.ENTER)
        time.sleep(3)



    def test_second(self):
        self.driver.get("https://facebook.com/")

        element = self.driver.find_element(By.ID, "email")
        element.clear()
        element.send_keys("Testing@gmail.com")

        element = self.driver.find_element(By.ID, "pass")
        element.clear()
        element.send_keys("Password")

        element = self.driver.find_element(By.NAME, "login")
        element.click()