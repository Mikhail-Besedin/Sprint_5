from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestAuthorization:
    def test_authorization_button_go_to_personal_account(self,driver):
        driver.find_element(*TestLocators.LOG_IN_TO_YOUR_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_ENTRY_FIELD).send_keys(TestLocators.TEST_LOGIN)
        driver.find_element(*TestLocators.PASSWORD_ENTRY_FIELD).send_keys(TestLocators.TEST_PAS)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until_not (expected_conditions.visibility_of_element_located (TestLocators.LOGIN_BUTTON))
        assert driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text == "Оформить заказ"

    def test_authorization_button_go_to_account(self, driver):
        driver.find_element(*TestLocators.BUTTON_GO_TO_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_ENTRY_FIELD).send_keys(TestLocators.TEST_LOGIN)
        driver.find_element(*TestLocators.PASSWORD_ENTRY_FIELD).send_keys(TestLocators.TEST_PAS)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        assert driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text == "Оформить заказ"

    def test_authorization_button_registration(self,driver):
        driver.find_element(*TestLocators.LOG_IN_TO_YOUR_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_THE_REGISTRATION_FORM).click()
        driver.find_element(*TestLocators.EMAIL_ENTRY_FIELD).send_keys(TestLocators.TEST_LOGIN)
        driver.find_element(*TestLocators.PASSWORD_ENTRY_FIELD).send_keys(TestLocators.TEST_PAS)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        assert driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text == "Оформить заказ"

    def test_authorization_button_restore_password(self, driver):
        driver.find_element(*TestLocators.LOG_IN_TO_YOUR_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.RESTORE_PASSWORD_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_THE_RESTORE_PASSWORD_FORM).click()
        driver.find_element(*TestLocators.EMAIL_ENTRY_FIELD).send_keys(TestLocators.TEST_LOGIN)
        driver.find_element(*TestLocators.PASSWORD_ENTRY_FIELD).send_keys(TestLocators.TEST_PAS)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until_not(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        assert driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text == "Оформить заказ"

