from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class ResultPage:
    """All result page methods come here."""
    def __init__(self, driver):
        self.driver = driver

        # Variables for locators.
        self.search_departure_assertion_xpath = Locators.search_departure_assertion_xpath
        self.search_arrival_assertion_xpath = Locators.search_arrival_assertion_xpath
        self.search_date1_assertion_xpath = Locators.search_date1_assertion_xpath
        self.search_date2_assertion_xpath = Locators.search_date2_assertion_xpath
        self.search_passengers_assertion_xpath = Locators.search_passengers_xpath
        self.search_result_assertion_xpath = Locators.search_result_assertion_xpath

    """Methods for checking 
        expected results."""

    def assertion_by_text(self, assertion):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.search_result_assertion_xpath))
        )
        expected_result_text = assertion
        result_text = self.driver.find_element_by_xpath(self.search_result_assertion_xpath).text
        if expected_result_text == result_text:
            return True

    def departure_assertion(self, assertion):
        expected_result_text = assertion
        result_text = self.driver.find_element_by_xpath(self.search_departure_assertion_xpath).get_attribute("value")
        if expected_result_text == result_text:
            return True

    def arrival_assertion(self, assertion):
        expected_result_text = assertion
        result_text = self.driver.find_element_by_xpath(self.search_arrival_assertion_xpath).get_attribute("value")
        if expected_result_text == result_text:
            return True

    def date1_assertion(self, assertion):
        expected_result_text = assertion
        result_text = self.driver.find_element_by_xpath(self.search_date1_assertion_xpath).get_attribute("value")
        if expected_result_text == result_text:
            return True

    def date2_assertion(self, assertion):
        expected_result_text = assertion
        result_text = self.driver.find_element_by_xpath(self.search_date2_assertion_xpath).get_attribute("value")
        if expected_result_text == result_text:
            return True

    def passengers_assertion(self, assertion):
        expected_result_text = assertion
        result_text = self.driver.find_element_by_xpath(self.search_passengers_assertion_xpath).get_attribute("value")
        if expected_result_text == result_text:
            return True