from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestLogout:
    def test_logout(self,driver):
        driver.find_element(*TestLocators.LOG_IN_TO_YOUR_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_ENTRY_FIELD).send_keys(TestLocators.TEST_LOGIN)
        driver.find_element(*TestLocators.PASSWORD_ENTRY_FIELD).send_keys(TestLocators.TEST_PAS)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        driver.find_element(*TestLocators.LOG_IN_TO_YOUR_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.EXIT_BUTTON))
        driver.find_element(*TestLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        assert driver.find_element(*TestLocators.TAG_ENTER).text == 'Вход'