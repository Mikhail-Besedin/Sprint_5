from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators


class TestAccountToDesignerTransition:
    def test_account_to_designer_transition_via_logo(self,driver):
        driver.find_element(*TestLocators.LOG_IN_TO_YOUR_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        driver.find_element(*TestLocators.STELLAR_BURGERS_LOGO).click()
        assert driver.find_element(*TestLocators.TITLE_IN_THE_CONSTRUCTOR).text == "Соберите бургер"

    def test_account_to_designer_transition_via_button_constructor(self,driver):
        driver.find_element(*TestLocators.LOG_IN_TO_YOUR_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        assert driver.find_element(*TestLocators.TITLE_IN_THE_CONSTRUCTOR).text == "Соберите бургер"