import pytest
from base_test  import BaseTest
from selenium.webdriver.common.by import By


class Test_Selenium_Demo(BaseTest):

    def test_one(self):
        self.driver.get("https://www.globalsqa.com/")
        assert self.driver.title == 'Home - GlobalSQA'
        #self.driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(search)
        #self.driver.find_element(By.XPATH, '(//*[@value="Google Search"])[2]').click()
        #assert self.driver.title == expectedTitle

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