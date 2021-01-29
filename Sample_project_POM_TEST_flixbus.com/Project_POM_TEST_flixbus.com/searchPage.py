from locators import Locators
from dictionaries import Dictionaries


class SearchPage:
    """All search page methods come here."""

    def __init__(self, driver):
        self.driver = driver

        # Variables for locators:
        self.select_one_way_flight_css = Locators.select_one_way_flight_css
        self.select_two_ways_flight_css = Locators.select_two_ways_flight_css
        self.insert_departure_xpath = Locators.insert_departure_xpath
        self.departure_list_first_xpath = Locators.departure_list_first_xpath
        self.insert_arrival_xpath = Locators.insert_arrival_xpath
        self.arrival_list_first_xpath = Locators.arrival_list_first_xpath
        self.replace_destinations_xpath = Locators.replace_destinations_xpath
        self.insert_date1_css = Locators.insert_date1_css
        self.insert_date2_css = Locators.insert_date2_css
        self.next_month_button_css = Locators.next_month_button_css
        self.month_and_year_heading_css = Locators.month_and_year_heading_css
        self.insert_passengers_css = Locators.insert_passengers_css
        self.add_adult_css = Locators.add_adult_css
        self.add_child_css = Locators.add_child_css
        self.add_bike_css = Locators.add_bike_css
        self.search_button_css = Locators.search_button_css

    """Methods for testing 
    the bus connections browser."""

    def select_one_way_flight(self):
        self.driver.find_element_by_css_selector(self.select_one_way_flight_css).click()

    def select_two_ways_flight(self):
        self.driver.find_element_by_css_selector(self.select_two_ways_flight_css).click()

    def insert_departure(self, departure):
        self.driver.find_element_by_xpath(self.insert_departure_xpath).send_keys(departure)
        self.driver.find_element_by_xpath(self.departure_list_first_xpath).click()

    def insert_arrival(self, arrival):
        self.driver.find_element_by_xpath(self.insert_arrival_xpath).send_keys(arrival)
        self.driver.find_element_by_xpath(self.arrival_list_first_xpath).click()

    def replace_destinations(self):
        self.driver.find_element_by_xpath(self.replace_destinations_xpath).click()

    def insert_dates(self, new_date):
        self.driver.find_element_by_css_selector(self.insert_date1_css).click()
        month_and_year_heading = self.driver.find_element_by_css_selector(self.month_and_year_heading_css).text
        while month_and_year_heading != new_date:
            self.driver.find_element_by_css_selector(self.next_month_button_css).click()
            month_and_year_heading = self.driver.find_element_by_css_selector(self.month_and_year_heading_css).text
        else:
            self.driver.find_element_by_css_selector(Dictionaries.test_03.get("locator for Thu 5 May")).click()

        self.driver.find_element_by_css_selector(self.insert_date2_css).click()
        while month_and_year_heading != new_date:
            self.driver.find_element_by_css_selector(self.next_month_button_css).click()
            month_and_year_heading = self.driver.find_element_by_css_selector(self.month_and_year_heading_css).text
        else:
            self.driver.find_element_by_css_selector(Dictionaries.test_03.get("locator for Fri 6 May")).click()

    def set_adults_amount(self):
        self.driver.find_element_by_css_selector(self.insert_passengers_css).click()
        self.driver.find_element_by_css_selector(self.add_adult_css).click()

    def set_children_amount(self):
        self.driver.find_element_by_css_selector(self.insert_passengers_css).click()
        self.driver.find_element_by_css_selector(self.add_child_css).click()

    def set_bikes_amount(self):
        self.driver.find_element_by_css_selector(self.insert_passengers_css).click()
        self.driver.find_element_by_css_selector(self.add_bike_css).click()

    def search_button(self):
        self.driver.find_element_by_css_selector(self.search_button_css).click()

    """Methods for checking 
    search page elements availability."""

    def check_one_way_flight_button(self):
        return self.driver.find_element_by_css_selector(self.select_one_way_flight_css).is_enabled()

    def check_two_ways_flight_button(self):
        self.driver.find_element_by_css_selector(self.select_two_ways_flight_css).click()
        return self.driver.find_element_by_css_selector(self.select_two_ways_flight_css).is_enabled()

    def check_departure_searchbox(self):
        return self.driver.find_element_by_xpath(self.insert_departure_xpath).is_enabled()

    def check_arrival_searchbox(self):
        return self.driver.find_element_by_xpath(self.insert_arrival_xpath).is_enabled()

    def check_replace_button(self):
        return self.driver.find_element_by_xpath(self.replace_destinations_xpath).is_enabled()

    def check_insert_date1_searchbox(self):
        return self.driver.find_element_by_css_selector(self.insert_date1_css).is_enabled()

    def check_insert_date2_searchbox(self):
        return self.driver.find_element_by_css_selector(self.insert_date2_css).is_enabled()

    def check_month_and_year_heading(self):
        self.driver.find_element_by_css_selector(self.insert_date1_css).click()
        return self.driver.find_element_by_css_selector(self.month_and_year_heading_css).is_displayed()

    def check_passengers_searchbox(self):
        return self.driver.find_element_by_css_selector(self.insert_passengers_css).is_enabled()

    def check_adults_button(self):
        self.driver.find_element_by_css_selector(self.insert_passengers_css).click()
        return self.driver.find_element_by_css_selector(self.add_adult_css).is_enabled()

    def check_children_button(self):
        self.driver.find_element_by_css_selector(self.insert_passengers_css).click()
        return self.driver.find_element_by_css_selector(self.add_child_css).is_enabled()

    def check_bikes_button(self):
        self.driver.find_element_by_css_selector(self.insert_passengers_css).click()
        return self.driver.find_element_by_css_selector(self.add_bike_css).is_enabled()

    def check_search_button(self):
        return self.driver.find_element_by_css_selector(self.search_button_css).is_enabled()
