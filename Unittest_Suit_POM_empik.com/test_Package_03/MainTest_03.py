# MainTest
# Sample_POM_TEST_empik.com

# A PAGE OBJECT MODEL which performs sample end-to-end test on empik.com:
# User chooses a product, adds it to the cart, deletes it from the cart.

import unittest
from selenium import webdriver
from test_Package_03 import SearchPages_03


class EmpikSearch03(unittest.TestCase):
    """A test class to show how selected test cases works"""

    def setUp(self):
        # Here you can select your web browser and a path to its driver:
        self.driver = webdriver.Chrome("C:/Program Files (x86)/chromedriver.exe")
        self.driver.get("https://www.empik.com/")
        self.driver.maximize_window()

    @unittest.SkipTest           # Decorator to skip the page title test which will be done in MainTest_02
    def test_01_page_title(self):
        """Checking if the search page title matches"""
        search_page = SearchPages_03.MainPage(self.driver)
        assert search_page.is_title_matches()

    def test_02(self):
        """Performs searching and adding selected product to the cart"""
        search_page = SearchPages_03.MainPage(self.driver)
        search_page.input_text()
        search_page.press_search()
        search_page.select_product()

        cart_page = SearchPages_03.CartPage(self.driver)
        cart_page.enter_cart()
        assert cart_page.is_cart_not_empty()
        assert cart_page.assert_product_name()

        cart_page.delete_product()
        assert cart_page.is_cart_empty()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()