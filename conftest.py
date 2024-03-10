import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import TestLocators


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get(TestLocators.URL)
    yield driver
    driver.quit()