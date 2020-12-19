class Locators:

    # searchPage objects LOCATORS:

    select_one_way_flight_xpath = "//*[@for='search-mask-trip-mode-oneway-toggle']"
    select_two_ways_flight_xpath = "//*[@for='search-mask-trip-mode-roundtrip-toggle']"
    insert_departure_xpath = "//*[@id='search-mask-component']/div/div/div[2]/div[1]/div/div/div/div/input"
    insert_departure_list_first_xpath = \
        "//*[@id='search-mask-component']/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div/ul/li[2]/button"
    insert_arrival_xpath = \
        "//*[@id='search-mask-component']/div/div/div[2]/div[2]/div/div/div/input"
    insert_arrival_list_first_xpath = \
        "//*[@id='search-mask-component']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/ul/li[2]/button"
    replace_destinations_xpath = "//*[@id='search-mask-component']/div/div/div[2]/div[1]/div/button"
    insert_date1_xpath = "//*[@data-e2e='departure-date-input-field']"  # locator for: Thu 5 May 2022
    insert_date2_xpath = "//*[@data-e2e='arrival-date-input-field']"   # locator for: Thu 6 May 2022
    next_month_button_xpath = "//*[@class='DayPicker-NavButton DayPicker-NavButton--custom DayPicker-NavButton--next']"
    month_and_year_heading_xpath = \
        "//*[@id='search-mask-component']/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div"
    new_date1_xpath = "//*[@aria-label='Thursday, 5 May 2022']"
    new_date2_xpath = "//*[@aria-label='Friday, 6 May 2022']"
    insert_passengers = "//*[@placeholder='Please add passengers...']"
    add_adult_xpath = "//*[@class='Icon__icon___1nNH- Icon__iconSmall___1BFyd flix-icon flix-icon-plus']"
    add_child_xpath = \
        "//*[@id='search-mask-component']/div/div/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/button[2]/i"
    add_bike_xpath = \
        "//*[@id='search-mask-component']/div/div/div[4]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/button[2]/i"
    search_button_xpath = "//*[@data-e2e='search-button']"

    # resultPage objects LOCATORS:

    search_departure_assertion_xpath = "//*[@id='search-mask-component']/div/div/div[2]/div[1]/div/div/div/div/input"
    search_arrival_assertion_xpath = "//*[@id='search-mask-component']/div/div/div[2]/div[2]/div/div/div/input"
    search_date1_assertion_xpath = "//*[@id='search-mask-component']/div/div/div[3]/div[1]/div/div/input"
    search_date2_assertion_xpath = "//*[@id='search-mask-component']/div/div/div[3]/div[2]/div/div/input"
    search_passengers_xpath = "//*[@id='search-mask-component']/div/div/div[4]/div/div/div[1]/div/input"
    search_result_assertion_xpath = "//*[@class='flix-h2 Message__messageTitle___36oyY']"
