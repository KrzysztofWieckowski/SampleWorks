from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    BUTTON_2 = (By.CSS_SELECTOR, "[class='udlite-btn udlite-btn-medium udlite-btn-secondary udlite-heading-sm']")
