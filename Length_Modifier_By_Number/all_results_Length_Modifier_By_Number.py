from Length_Modifier_By_Number import LengthModifier

# all_results_Length Modifier_by_Number.

# Prints all possible results for selected arguments:
# example_lists = ([], ["k"], ["k", "l", "m", "n"])
# example_numbers = (-1, 0, 1, 10)
# You can also attach any list in example_lists or/and number in example_numbers.
# Please remember that the given number of elements (in test_numbers) must be > 0 and must be integer.

example_lists = ([], ["k"], ["k", "l", "m", "n"])
example_numbers = (-1, 0, 1, 10)

q = 1
for item in example_lists:
    for element in example_numbers:
        print("\nRESULT NUMBER:", q, "\nArguments:", item, ",", element)
        modification = LengthModifier(item, element)
        result = modification.creating_new_list()
        q += 1
