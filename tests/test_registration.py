from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import random

class TestRegistration:
    def test_registration(self, driver):
        driver.find_element(*TestLocators.LOG_IN_TO_YOUR_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        driver.find_element(*TestLocators.NAME_ENTRY_FIELD).send_keys(f'Mikhail{random.randint(1,100)}')
        driver.find_element(*TestLocators.EMAIL_ENTRY_FIELD).send_keys(f'mikhailbesedin6{random.randint(100,999)}@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_ENTRY_FIELD).send_keys(f'besedin{random.randint(100000,999999)}')
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        assert driver.find_element(*TestLocators.TAG_ENTER).text == 'Вход'


    def test_registration_fail(self, driver):
        driver.find_element(*TestLocators.LOG_IN_TO_YOUR_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        driver.find_element(*TestLocators.NAME_ENTRY_FIELD).send_keys(f'Mikhail{random.randint(1, 100)}')
        driver.find_element(*TestLocators.EMAIL_ENTRY_FIELD).send_keys(f'mikhailbesedin6{random.randint(100, 999)}@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_ENTRY_FIELD).send_keys(f'1{random.randint(1, 99)}')
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        assert driver.find_element(*TestLocators.ERROR_PASSWORD).text == 'Некорректный пароль'