import pytest
from base_test  import BaseTest
from selenium.webdriver.common.by import By


class Test_Selenium_Demo(BaseTest):

    def test_one(self):
        self.driver.get("https://demoqa.com/")
        assert self.driver.title == 'DEMOQA'


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