from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    locator = "q"

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """Home page action methods come here - udemy.org"""
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Udemy" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()



class SearchResultPage(BasePage):
    """Search results page action methods come here"""
    def is_results_found(self):
        return "No results found" not in self.driver.page_source

    def click_button_2(self):
        element = self.driver.find_element(*MainPageLocators.BUTTON_2)
        element.click()