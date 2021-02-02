# Tests_Locators.

from selenium.webdriver.common.by import By


class Locators(object):
    """A class for locators. All pages locators should come here"""

    SEARCH_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    SEARCH_BOX = (By.ID, "bq")

    SELECT_PRODUCT = (By.CSS_SELECTOR, "[data-product-position='1']")
    SELECT_PRODUCT_xpath = "/html/body/main/div[2]/div/div/div/div[2]/div/div[3]/div[1]"
    ADD_TO_CART = (By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div/div[2]/div/div[1]/button")

    CART_BUTTON_xpath = "/html/body/header/div/div/div[5]/nav/ul[2]/li[4]"
    CART_BUTTON = (By.CSS_SELECTOR, "[class='inlineImage--basket']")
    PRODUCT_NAME_xpath = "/html/body/main/div/section/div[1]/div/div/div[2]/div/div[1]/a/img"
    DELETE_BUTTON = (By.XPATH, "/html/body/main/div/section/div[1]/div/div/div[2]/div/div[2]/div[5]/a[1]")
    CART_MESSAGE_css = "div[class='css-1ruotq7-emptyCart']"
