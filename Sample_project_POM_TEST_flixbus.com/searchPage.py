from locators import Locators
import time


class SearchPage:
    """All search page methods come here."""

    def __init__(self, driver):
        self.driver = driver

        # Variables for locators
        self.select_one_way_flight_xpath = Locators.select_one_way_flight_xpath
        self.select_two_ways_flight_xpath = Locators.select_two_ways_flight_xpath
        self.insert_departure_xpath = Locators.insert_departure_xpath
        self.insert_departure_list_first_xpath = Locators.insert_departure_list_first_xpath
        self.insert_arrival_xpath = Locators.insert_arrival_xpath
        self.insert_arrival_list_first_xpath = Locators.insert_arrival_list_first_xpath
        self.replace_destinations_xpath = Locators.replace_destinations_xpath
        self.insert_date1_xpath = Locators.insert_date1_xpath
        self.insert_date2_xpath = Locators.insert_date2_xpath
        self.next_month_button_xpath = Locators.next_month_button_xpath
        self.month_and_year_heading_xpath = Locators.month_and_year_heading_xpath
        self.new_date1_xpath = Locators.new_date1_xpath
        self.new_date2_xpath = Locators.new_date2_xpath
        self.insert_passengers_class = Locators.insert_passengers
        self.add_adult_xpath = Locators.add_adult_xpath
        self.add_child_xpath = Locators.add_child_xpath
        self.add_bike_xpath = Locators.add_bike_xpath
        self.search_button_xpath = Locators.search_button_xpath

    """Methods for testing 
    the bus connections browser."""

    def select_one_way_flight(self):
        self.driver.find_element_by_xpath(self.select_one_way_flight_xpath).click()

    def select_two_ways_flight(self):
        self.driver.find_element_by_xpath(self.select_two_ways_flight_xpath).click()

    def insert_departure(self, departure):
        self.driver.find_element_by_xpath(self.insert_departure_xpath).send_keys(departure)
        self.driver.find_element_by_xpath(self.insert_departure_list_first_xpath).click()

    def insert_arrival(self, arrival):
        self.driver.find_element_by_xpath(self.insert_arrival_xpath).send_keys(arrival)
        time.sleep(1) #
        self.driver.find_element_by_xpath(self.insert_arrival_list_first_xpath).click()

    def replace_destinations (self):
        self.driver.find_element_by_xpath(self.replace_destinations_xpath).click()

    def insert_dates (self, new_date):

        self.driver.find_element_by_xpath(self.insert_date1_xpath).click()
        month_and_year_heading = self.driver.find_element_by_xpath(self.month_and_year_heading_xpath).text
        while month_and_year_heading != new_date:
            self.driver.find_element_by_xpath(self.next_month_button_xpath).click()
            month_and_year_heading = self.driver.find_element_by_xpath(self.month_and_year_heading_xpath).text
        else:
            self.driver.find_element_by_xpath(self.new_date1_xpath).click()

        self.driver.find_element_by_xpath(self.insert_date2_xpath).click()
        while month_and_year_heading != new_date:
            self.driver.find_element_by_xpath(self.next_month_button_xpath).click()
            month_and_year_heading = self.driver.find_element_by_xpath(self.month_and_year_heading_xpath).text
        else:
            self.driver.find_element_by_xpath(self.new_date2_xpath).click()

    def set_adults_amount(self):
        self.driver.find_element_by_xpath(self.insert_passengers_class).click()
        self.driver.find_element_by_xpath(self.add_adult_xpath).click()

    def set_children_amount(self):
        self.driver.find_element_by_xpath(self.insert_passengers_class).click()
        self.driver.find_element_by_xpath(self.add_child_xpath).click()

    def set_bikes_amount(self):
        self.driver.find_element_by_xpath(self.insert_passengers_class).click()
        self.driver.find_element_by_xpath(self.add_bike_xpath).click()

    def search_button(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

    """Methods for checking 
    search page elements availability."""

    def check_two_ways_flight_button(self):
        self.driver.find_element_by_xpath(self.select_two_ways_flight_xpath).click()
        return self.driver.find_element_by_xpath(self.select_two_ways_flight_xpath).is_enabled()

    def check_departure_searchbox(self):
        return self.driver.find_element_by_xpath(self.insert_departure_xpath).is_enabled()

    def check_arrival_searchbox(self):
        return self.driver.find_element_by_xpath(self.insert_arrival_xpath).is_enabled()

    def check_replace_button(self):
        return self.driver.find_element_by_xpath(self.replace_destinations_xpath).is_enabled()

    def check_insert_date1_searchbox(self):
        return self.driver.find_element_by_xpath(self.insert_date1_xpath).is_enabled()

    def check_insert_date2_searchbox(self):
        return self.driver.find_element_by_xpath(self.insert_date2_xpath).is_enabled()

    def check_month_and_year_heading(self):
        self.driver.find_element_by_xpath(self.insert_date1_xpath).click()
        return self.driver.find_element_by_xpath(self.month_and_year_heading_xpath).is_displayed()

    def check_passengers_searchbox(self):
        return self.driver.find_element_by_xpath(self.insert_passengers_class).is_enabled()

    def check_adults_button(self):
        self.driver.find_element_by_xpath(self.insert_passengers_class).click()
        return self.driver.find_element_by_xpath(self.add_adult_xpath).is_enabled()

    def check_children_button(self):
        self.driver.find_element_by_xpath(self.insert_passengers_class).click()
        return self.driver.find_element_by_xpath(self.add_child_xpath).is_enabled()

    def check_bikes_button(self):
        self.driver.find_element_by_xpath(self.insert_passengers_class).click()
        return self.driver.find_element_by_xpath(self.add_bike_xpath).is_enabled()

    def check_search_button(self):
        return self.driver.find_element_by_xpath(self.search_button_xpath).is_enabled()