# Length Modifier by Number.
# Modifies the length of the list by the given number.

# Below, in the MAIN part, to the object 'new_list' add:
# - any list (currently there is an example_list: ["k", "l", "m", "n"]);
# - any number of elements (currently an example_number is: 8)
#   (but please remember that the given number of elements must be > 0 and integer).

class LengthModifier(object):

    def __init__(self, old_list, number):
        self.old_list = old_list
        self.number = number

    def creating_new_list(self):
        if len(self.old_list) == 0 and self.number <= 0:
            print("The given list is empty! We can't divide by zero.")
            print("Please create a list with at least 1 element.")
            print("The given number is not correct!")
            print("Please write number > 0.")
        elif len(self.old_list) == 0:
            print("The given list is empty! We can't divide by zero.")
            print("Please create a list with at least 1 element.")
        elif self.number <= 0:
            print("The given number is not correct!")
            print("Please write number > 0.")
        else:
            x = len(self.old_list)
            y = self.number
            if x > y:
                elements_to_subtract = x - y
                elements_that_remains = x - elements_to_subtract
                new__list = self.old_list[:elements_that_remains]
                print("New List: ", new__list)
            if x == y:
                print("New List: ", self.old_list)
            if x < y:
                quotient = int(y/x + 1)
                assistant_list = self.old_list * quotient
                elements_to_add = y - x
                list_to_add = assistant_list[:elements_to_add]
                for i in range(elements_to_add):
                        z = list_to_add[i]
                        self.old_list.append(z)
                print("New List: ", self.old_list)


# MAIN
example_list = ["k", "l", "m", "n"]
example_number = 8
new_list = LengthModifier(example_list, example_number)
new_list.creating_new_list()
