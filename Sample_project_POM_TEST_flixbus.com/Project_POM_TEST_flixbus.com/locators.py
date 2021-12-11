# locators.

class Locators:
    """A class for locators. All search page and result page locators should come here."""

    select_one_way_flight_css = "[for='search-mask-trip-mode-oneway-toggle']"
    select_two_ways_flight_css = "[for='search-mask-trip-mode-roundtrip-toggle']"
    insert_departure_xpath = "//*[.='From']//input"
    departure_list_first_xpath = "//div[@class='HHHZr styles.responsivePopuplarge']//li[2]//button"
    insert_arrival_xpath = "//*[.='To']//input"
    arrival_list_first_xpath = "//div[@class='HHHZr styles.responsivePopuplarge']//li[2]//button"
    replace_destinations_xpath = "//*[@alt='icon-switch']/.."
    insert_date1_css = "[data-e2e='departure-date-input-field']"
    insert_date2_css = "[data-e2e='arrival-date-input-field']"
    next_month_button_css = ".flix-icon-arrow-right"
    month_and_year_heading_css = ".DayPicker-Month:nth-child(1) > .DayPicker-Caption > div"
    insert_passengers_css = "[placeholder='Please add passengers...']"
    add_adult_css = ".\_1f35C:nth-child(1) .flix-icon-plus"
    add_child_css = ".\_1f35C:nth-child(2) .flix-icon-plus"
    add_bike_css = ".\_1f35C:nth-child(3) .flix-icon-plus"
    search_button_css = "[data-e2e='search-button']"
    search_result_assertion_css = "h2[class='flix-h2 Message__messageTitle___2SiYU']"
