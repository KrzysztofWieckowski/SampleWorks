# SearchPage_02
# All page actions methods come here.

from tests_locators.Tests_Locators import *
from tests_data.Tests_Data import TestData
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# Global variables for product name assertions:
product_name_1 = ""
product_name_2 = ""


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Main Page actions methods come here"""

    def is_title_matches(self):
        return TestData.test_data_02["page_title"] in self.driver.title

    def input_text(self):
        text = TestData.test_data_02["search_text"]
        self.driver.find_element(*Locators.SEARCH_BOX).clear()
        self.driver.find_element(*Locators.SEARCH_BOX).send_keys(text)

    def press_search(self):
        self.driver.find_element(*Locators.SEARCH_BUTTON).click()

    def select_product(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, Locators.SELECT_PRODUCT_xpath)))

        product = self.driver.find_element(*Locators.SELECT_PRODUCT)
        add_to_cart = self.driver.find_element(*Locators.ADD_TO_CART)

        # Putting a string into the global variable 'product_name_1' (useful later on for a product name assertion).
        product_name = self.driver.find_element(*Locators.SELECT_PRODUCT).get_attribute("data-product-name")
        global product_name_1
        product_name_1 = product_name

        self.driver.execute_script("window.scrollBy(0, 500)", "")
        hover = ActionChains(self.driver).move_to_element(product).move_to_element(add_to_cart)
        hover.click().perform()

        self.driver.find_element(*Locators.CART_BUTTON).click()


class CartPage(BasePage):
    """Cart Page actions methods come here"""

    def enter_cart(self):
        self.driver.execute_script("window.scrollBy(0, 100)", "")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, Locators.PRODUCT_NAME_xpath)))
        product_name = element.get_attribute("alt")

        # Putting a string into the global variable 'product_name_2' (useful later on for a product name assertion).
        global product_name_2
        product_name_2 = product_name

    def is_cart_not_empty(self):
        return "Twój koszyk jest pusty" not in self.driver.page_source

    @staticmethod
    def assert_product_name():
        global product_name_1, product_name_2
        return product_name_1 == product_name_2

    def delete_product(self):
        self.driver.find_element(*Locators.DELETE_BUTTON).click()

    def is_cart_empty(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.CART_MESSAGE_css)))
        return "Twój koszyk jest pusty" in self.driver.page_source
