from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestSectionDesigner:
    def test_section_designer_sauses(self, driver):
        driver.find_element(*TestLocators.BUTTON_SAUCES).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SAUCES_SECTION_NAME))
        assert driver.find_element(*TestLocators.SAUCES_SECTION_NAME).is_displayed()

    def test_section_designer_fillings(self, driver):

        driver.find_element(*TestLocators.BUTTON_FILLINGS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.FILLINGS_SECTION_NAME))
        assert driver.find_element(*TestLocators.FILLINGS_SECTION_NAME).is_displayed()

    def test_section_designer_buns(self, driver):
        driver.find_element(*TestLocators.BUTTON_FILLINGS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.FILLINGS_SECTION_NAME))
        driver.find_element(*TestLocators.BUTTON_BUNS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUNS_SECTION_NAME))
        assert driver.find_element(*TestLocators.BUNS_SECTION_NAME).is_displayed()
