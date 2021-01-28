from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import time


class ResultPage:
    """All result page methods come here."""

    def __init__(self, driver):
        self.driver = driver

        # Variables for locators:
        self.search_departure_assertion_xpath = Locators.insert_departure_xpath
        self.search_arrival_assertion_xpath = Locators.insert_arrival_xpath
        self.search_date1_assertion_css = Locators.insert_date1_css
        self.search_date2_assertion_css = Locators.insert_date2_css
        self.search_passengers_assertion_css = Locators.insert_passengers_css
        self.search_result_assertion_css = Locators.search_result_assertion_css

    """Methods for checking 
        expected results."""

    def assertion_by_text(self, expected_text):
        time.sleep(10)

        result_text = self.driver.find_element_by_css_selector(self.search_result_assertion_css).text
        if expected_text == result_text:
            return True

    def departure_assertion(self, expected_text):
        result_text = self.driver.find_element_by_xpath(self.search_departure_assertion_xpath).get_attribute("value")
        if expected_text == result_text:
            return True

    def arrival_assertion(self, expected_text):
        result_text = self.driver.find_element_by_xpath(self.search_arrival_assertion_xpath).get_attribute("value")
        if expected_text == result_text:
            return True

    def date1_assertion(self, expected_text):
        result_text = self.driver.find_element_by_css_selector(self.search_date1_assertion_css).get_attribute("value")
        if expected_text == result_text:
            return True

    def date2_assertion(self, expected_text):
        result_text = self.driver.find_element_by_css_selector(self.search_date2_assertion_css).get_attribute("value")
        if expected_text == result_text:
            return True

    def passengers_assertion(self, expected_text):
        result_text = self.driver.find_element_by_css_selector(self.search_passengers_assertion_css).get_attribute("value")
        if expected_text == result_text:
            return True
