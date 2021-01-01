class Dictionaries:
    """A class for dictionaries. All input and output data necessary for performing test cases should come here."""

    # Input and output data for test_01_check_page_loading.
    test_1 = {"title": "Bus travel through Europe | FlixBus"}

    # Input and output data for test_03_sample_search_test.
    test_3 = {"departure": "Warsaw",
              "arrival": "Berlin",
              "date": "May 2022",
              "assert_text": "No trips on: Thu, 5 May",
              "assert_departure": "Berlin",
              "assert_arrival": "Warsaw",
              "assert_date1": "Thu 5 May",
              "assert_date2": "Fri 6 May",
              "assert_passengers": "2 Adults, 1 Child, 0 Bike Slots"}

    # Input and output data for test_04_sample_search_test_with_fail.
    test_4 = {"departure": "Munich",
              "arrival": "Berlin",
              "date": "May 2022",
              "assert_text": "Outbound trip",
              "assert_departure": "Munich",
              "assert_arrival": "Berlin",
              "assert_date1": "Thu 5 May",
              "assert_date2": "Fri 6 May",
              "assert_passengers": "1 Adult, 1 Bike Slot"}
