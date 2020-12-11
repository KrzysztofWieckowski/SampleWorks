from Lenght_Modifier_By_Number import NewList

# test_Length Modifier_by_Number.
# Tests the Length_Modifier_By_Number.

# Runs all possible tests for selected arguments:
# test_list = ([], ["k"], ["k", "l", "m", "n"]), test_numbers = (-1, 0, 1, 10).

# You can also attach any list in test_list or/and number in test_numbers.
# Please remember that the given number of elements (in test_numbers) must be > 0.

test_list = ([], ["k"], ["k", "l", "m", "n"])
test_numbers = (-1, 0, 1, 10)

q = 1
for item in test_list:
    for element in test_numbers:
        print("\nTEST NUMBER:", q, "\nArguments:", item, ",", element)
        test = NewList(item, element)
        result = test.creating_new_list()
        q += 1


