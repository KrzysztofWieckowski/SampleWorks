# Udemy_Test
# An UNIT TEST MODULE which performs 3 test cases on udemy.com


import unittest
from selenium import webdriver
import page
import time

class UdemySearch(unittest.TestCase):
    """A test class to show how few page elements works"""

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.udemy.com/")

    def test_search_udemy(self):
        """Test#1 Checks if the sentence "Udemy" is in title"""
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        """Test#2 Tests udemy.org search feature. Searches for the word "selenium", then verified that some results show up."""
        mainPage.search_text_element = "selenium"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
        """Test#3 Checks transition to page 'Zaloguj się'"""
        self.driver.implicitly_wait(5)
        search_result_page.click_button_2()
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

