import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    driver: WebDriver = webdriver.Chrome(executable_path="C:/Users/Ольга/PycharmProjects1/33.1_RT/chromedriver.exe")
    WebDriverWait(driver, 10)
    driver.implicitly_wait(5)
    yield driver

    driver.quit()


@pytest.fixture
def web_browser(request, selenium, driver):
    browser = selenium
    browser.set_window_size(1400, 1000)
    yield browser

    driver.quit()


@pytest.mark.usefixtures("web_driver")
class Base(unittest.TestCase):
    @pytest.fixture(scope="class")
    def web_driver(self, request):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        request.cls.driver = driver
        yield
        driver.close()
