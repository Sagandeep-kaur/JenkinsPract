import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
#from MyListner import MyListner
#from conf import Credential
#from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def set_up(request, browser_type):
    #print("Running on browser : "+browser_type)

    if browser_type == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome()
    elif browser_type == 'firefox':
        driver = webdriver.Firefox()
    elif browser_type == 'edge':
        driver = webdriver.Edge()
    #driver.get('www.google.com')
    else:
        raise ValueError(f"Unsupported browser: {browser_type}")
    driver.implicitly_wait(10)
    #driver = EventFiringWebDriver(driver, MyListner())
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome')


@pytest.fixture(scope="class", autouse=True)
def browser_type(request):
    return request.config.getoption("--browser")






