from Length_Modifier_By_Number import LengthModifier

# all_results_Length Modifier_by_Number.

# Prints all possible results for 3 boundary values (-1, 0, 1) and 2 lists ([], ["k", "l", "m", "n"]:
# example_lists = ([], ["k", "l", "m", "n"])
# example_boundary_numbers = (-1, 0, 1)
# You can also attach any list in example_lists and number in example_boundary_numbers.
# Please remember that the given numbers in example_boundary_numbers must be >0 and also must be integer.

example_lists = ([], ["k", "l", "m", "n"])
example_boundary_numbers = (-1, 0, 1)

q = 1
for item in example_lists:
    for element in example_boundary_numbers:
        print("\nRESULT NUMBER:", q, "\nArguments:", item, ",", element)
        modification = LengthModifier(item, element)
        result = modification.creating_new_list()
        q += 1
