# Sample_project_POM_TEST_flixbus.com
# This demo project delivers a framework for website test automation.
# It's a Sample Page Object Model test with www.flixbus.com. as an example.


from selenium import webdriver
import unittest
from searchPage import SearchPage
from resultPage import ResultPage
from staticMethods import StaticMethods
import HtmlTestRunner


class FlixbusTest(unittest.TestCase):
    """A test class to check how selected page elements works"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        driver = cls.driver
        driver.get("https://www.flixbus.com/")
        cls.driver.find_element_by_id("cookie-consent-accept-all-button").click()

    def test_01_check_page_loading(self):
        """Test_01 Checks page loading by the page title."""
        driver = self.driver
        expected_title = "Bus travel through Europe | FlixBus"
        self.assertEqual(driver.title, expected_title, "Wrong page title")

    def test_02_check_page_elements_availability(self):
        """Test_02 Checks page elements availability before starting the proper tests."""
        driver = self.driver
        check = SearchPage(driver)

        with self.subTest("Checking two ways flight button"):
            self.assertTrue(check.check_two_ways_flight_button())
        with self.subTest("Checking departure searchbox"):
            self.assertTrue(check.check_departure_searchbox())
        with self.subTest("Checking arrival searchbox"):
            self.assertTrue(check.check_arrival_searchbox())
        with self.subTest("Checking replace_button"):
            self.assertTrue(check.check_replace_button())
        with self.subTest("Checking insert date1 searchbox"):
            self.assertTrue(check.check_insert_date1_searchbox())
        with self.subTest("Checking insert date2 searchbox"):
            self.assertTrue(check.check_insert_date2_searchbox())
        with self.subTest("Checking month and year heading"):
            self.assertTrue(check.check_month_and_year_heading())
        with self.subTest("Checking passengers searchbox"):
            self.assertTrue(check.check_passengers_searchbox())
        with self.subTest("Checking adults button"):
            self.assertTrue(check.check_adults_button())
        with self.subTest("Checking children button"):
            self.assertTrue(check.check_children_button())
        with self.subTest("Checking bikes button"):
            self.assertTrue(check.check_children_button())
        with self.subTest("Checking search button"):
            self.assertTrue(check.check_search_button())

    def test_03_sample_search_test(self):
        """Test_03 Runs and checks a sample test case."""
        driver = self.driver
        search = SearchPage(driver)

        # Performing user steps:
        search.select_two_ways_flight()
        search.insert_departure("Warsaw")
        search.insert_arrival("Berlin")
        search.replace_destinations()
        search.insert_dates("May 2022")
        search.set_adults_amount()
        search.set_children_amount()
        search.search_button()

        # Checking results:
        result = ResultPage(driver)
        with self.subTest("Checking if main message is equal to expected"):
            self.assertTrue(result.result_assertion_by_text("No trips on: Thu, 5 May"))
        with self.subTest("Checking if departure place is equal to expected"):
            self.assertTrue(result.departure_assertion("Berlin"))
        with self.subTest("Checking if arrival place is equal to expected"):
            self.assertTrue(result.arrival_assertion("Warsaw"))
        with self.subTest("Checking if departure date is equal to expected"):
            self.assertTrue(result.date1_assertion("Thu 5 May"))
        with self.subTest("Checking if arrival date is equal to expected"):
            self.assertTrue(result.date2_assertion("Fri 6 May"))
        with self.subTest("Checking if adults, children, bikes amount is equal to expected"):
            self.assertTrue(result.passengers_assertion("2 Adults, 1 Child, 0 Bike Slots"))

    def test_04_sample_search_test_fail(self):
        driver = self.driver
        driver.get("https://www.flixbus.com/")
        search = SearchPage(driver)

        # Performing user steps:
        search.select_two_ways_flight()
        search.insert_departure("Warsaw")
        search.insert_arrival("Berlin")
        search.replace_destinations()
        search.insert_dates("May 2022")
        search.set_adults_amount()
        search.set_children_amount()
        search.search_button()

        # Checking results:
        result = ResultPage(driver)
        with self.subTest("Checking if main result page message is equal to expected"):
            # Expected message ("Outbound trip") is intentionally wrong and causes one subtest to fail.
            self.assertTrue(result.result_assertion_by_text("Outbound trip"))
        with self.subTest("Checking if departure place is equal to expected"):
            self.assertTrue(result.departure_assertion("Berlin"))
        with self.subTest("Checking if arrival place is equal to expected"):
            self.assertTrue(result.arrival_assertion("Warsaw"))
        with self.subTest("Checking if departure date is equal to expected"):
            self.assertTrue(result.date1_assertion("Thu 5 May"))
        with self.subTest("Checking if arrival date is equal to expected"):
            self.assertTrue(result.date2_assertion("Fri 6 May"))
        with self.subTest("Checking if adults, children, bikes amount is equal to expected"):
            self.assertTrue(result.passengers_assertion("2 Adults, 1 Child, 0 Bike Slots"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    folder = StaticMethods.report_folder()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output=folder), verbosity=2)
