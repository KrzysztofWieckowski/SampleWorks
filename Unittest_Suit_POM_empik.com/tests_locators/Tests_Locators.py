# Tests_Locators.

from selenium.webdriver.common.by import By


class Locators(object):
    """A class for locators. All pages locators should come here"""

    SEARCH_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    SEARCH_BOX = (By.ID, "bq")
    SEARCH_BOX_id = "bq"
    SELECT_PRODUCT = (By.CSS_SELECTOR, "[data-product-position='1']")
    SELECT_PRODUCT_xpath = "/html/body/main/div[2]/div/div/div/div[2]/div/div[3]/div[1]"
    ADD_TO_CART = (By.XPATH, "//div[2]/div/div/button")
    CART_BUTTON = (By.XPATH, "//a[@id='simple-dropdown4']/span/div")

    PRODUCT_NAME_xpath = "/html/body/main/div/section/div[1]/div/div/div[2]/div/div[1]/a/img"
    DELETE_BUTTON = (By.XPATH, "//div[5]/a")
    CART_MESSAGE_css = "div[class='css-1ruotq7-emptyCart']"
