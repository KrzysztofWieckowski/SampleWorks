# Sample_project_POM_TEST_flixbus.com
# This demo project delivers a framework for website test automation.
# It's a Sample Page Object Model test with www.flixbus.com. as an example.

from selenium import webdriver
import unittest
import HtmlTestRunner
from staticMethods import StaticMethods
from searchPage import SearchPage
from resultPage import ResultPage
from dictionaries import Dictionaries


class FlixbusTest(unittest.TestCase):
    """A test class to check how selected page elements works"""

    @classmethod
    def setUpClass(cls):
        # Here you can select your web browser and path to its driver:
        cls.driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        driver = cls.driver
        driver.get("https://www.flixbus.com/")
        # Accepting cookies:
        driver.find_element_by_id("cookie-consent-accept-all-button").click()

    def test_01_check_page_loading(self):
        """Test_01 Checks page loading by the page title."""
        driver = self.driver
        expected_title = Dictionaries.test_01.get("title")
        self.assertEqual(driver.title, expected_title, "Wrong page title")

    def test_02_check_page_elements_availability(self):
        """Test_02 Checks page elements availability before starting the proper tests."""
        driver = self.driver
        check = SearchPage(driver)

        with self.subTest("Checking one way flight button"):
            self.assertTrue(check.check_one_way_flight_button())
        with self.subTest("Checking two ways flight button"):
            self.assertTrue(check.check_two_ways_flight_button())
        with self.subTest("Checking departure searchbox"):
            self.assertTrue(check.check_departure_searchbox())
        with self.subTest("Checking arrival searchbox"):
            self.assertTrue(check.check_arrival_searchbox())
        with self.subTest("Checking replace button"):
            self.assertTrue(check.check_replace_button())
        with self.subTest("Checking insert date1 picker"):
            self.assertTrue(check.check_insert_date1_searchbox())
        with self.subTest("Checking insert date2 picker"):
            self.assertTrue(check.check_insert_date2_searchbox())
        with self.subTest("Checking month and year heading"):
            self.assertTrue(check.check_month_and_year_heading())
        with self.subTest("Checking passengers searchbox"):
            self.assertTrue(check.check_passengers_searchbox())
        with self.subTest("Checking add adults button"):
            self.assertTrue(check.check_adults_button())
        with self.subTest("Checking add children button"):
            self.assertTrue(check.check_children_button())
        with self.subTest("Checking add bikes button"):
            self.assertTrue(check.check_children_button())
        with self.subTest("Checking search button"):
            self.assertTrue(check.check_search_button())

    def test_03_sample_search_test(self):
        """Test_03 Runs and checks a sample test case.
        Uses test_03 dictionary from dictionaries module."""
        driver = self.driver
        search = SearchPage(driver)

        # Performing user steps:
        search.select_two_ways_flight()
        search.insert_departure(Dictionaries.test_03.get("departure"))
        search.insert_arrival(Dictionaries.test_03.get("arrival"))
        search.replace_destinations()
        search.insert_dates(Dictionaries.test_03.get("date"))
        search.set_adults_amount()
        search.set_children_amount()
        search.search_button()

        # Checking results:
        result = ResultPage(driver)
        with self.subTest("Checking if main message is equal to expected"):
            self.assertTrue(result.assertion_by_text(Dictionaries.test_03.get("assert_text")))
        with self.subTest("Checking if departure place is equal to expected"):
            self.assertTrue(result.departure_assertion(Dictionaries.test_03.get("assert_departure")))
        with self.subTest("Checking if arrival place is equal to expected"):
            self.assertTrue(result.arrival_assertion(Dictionaries.test_03.get("assert_arrival")))
        with self.subTest("Checking if departure date is equal to expected"):
            self.assertTrue(result.date1_assertion(Dictionaries.test_03.get("assert_date1")))
        with self.subTest("Checking if arrival date is equal to expected"):
            self.assertTrue(result.date2_assertion(Dictionaries.test_03.get("assert_date2")))
        with self.subTest("Checking if adults, children, bikes amount is equal to expected"):
            self.assertTrue(result.passengers_assertion(Dictionaries.test_03.get("assert_passengers")))

    def test_04_sample_search_test_with_fail(self):
        """Test_03 Runs and checks a sample test case. One subtest is intentionally failed.
        Uses test_04 dictionary from dictionaries module."""
        driver = self.driver
        driver.get("https://www.flixbus.com/")
        search = SearchPage(driver)

        # Performing user steps:
        search.select_two_ways_flight()
        search.insert_departure(Dictionaries.test_04.get("departure"))
        search.insert_arrival(Dictionaries.test_04.get("arrival"))
        search.insert_dates(Dictionaries.test_04.get("date"))
        search.set_bikes_amount()
        search.search_button()

        # Checking results:
        result = ResultPage(driver)
        with self.subTest("Checking if main result page message is equal to expected"):
            # Expected text ("Outbound trip") is intentionally wrong and causes one subtest to fail:
            self.assertTrue(result.assertion_by_text(Dictionaries.test_04.get("assert_text")))
        with self.subTest("Checking if departure place is equal to expected"):
            self.assertTrue(result.departure_assertion(Dictionaries.test_04.get("assert_departure")))
        with self.subTest("Checking if arrival place is equal to expected"):
            self.assertTrue(result.arrival_assertion(Dictionaries.test_04.get("assert_arrival")))
        with self.subTest("Checking if departure date is equal to expected"):
            self.assertTrue(result.date1_assertion(Dictionaries.test_04.get("assert_date1")))
        with self.subTest("Checking if arrival date is equal to expected"):
            self.assertTrue(result.date2_assertion(Dictionaries.test_04.get("assert_date2")))
        with self.subTest("Checking if adults, children, bikes amount is equal to expected"):
            self.assertTrue(result.passengers_assertion(Dictionaries.test_04.get("assert_passengers")))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    folder = StaticMethods.reports_folder()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output=folder), verbosity=2)