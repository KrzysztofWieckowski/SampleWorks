# dictionaries.

class Dictionaries:
    """A class for dictionaries. All input and output data necessary for performing test cases should come here."""

    # Output data for test_01_check_page_loading.
    test_01 = {"title": "Bus travel through Europe | FlixBus"}

    # Input and output data for test_03_sample_search_test.
    test_03 = {"departure": "Warsaw",
               "arrival": "Berlin",
               "date": "May 2022",
               "assert_text": "No trips on: Thu, 5 May",
               "assert_departure": "Berlin",
               "assert_arrival": "Warsaw",
               "assert_date1": "Thu 5 May",
               "assert_date2": "Fri 6 May",
               "assert_passengers": "2 Adults, 1 Child, 0 Bike Slots",
               "locator for Thu 5 May": "[aria-label='Thursday, 5 May 2022']",
               "locator for Fri 6 May": "[aria-label='Friday, 6 May 2022']"}

    # Input and output data for test_04_sample_search_test_with_fail.
    test_04 = {"departure": "Munich",
               "arrival": "Berlin",
               "date": "May 2022",
               "assert_text": "Outbound trip",
               "assert_departure": "Munich",
               "assert_arrival": "Berlin",
               "assert_date1": "Thu 5 May",
               "assert_date2": "Fri 6 May",
               "assert_passengers": "1 Adult, 1 Bike Slot",
               "locator for Thu 5 May": "[aria-label='Thursday, 5 May 2022']",
               "locator for Fri 6 May": "[aria-label='Friday, 6 May 2022']"}
