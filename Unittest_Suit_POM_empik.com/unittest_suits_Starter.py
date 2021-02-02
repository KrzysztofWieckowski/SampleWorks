# unittest_suits_Starter.
# Runs a unittest framework suit which consist of MainTest_01, MainTest_02 and MainTest_03.

import unittest
from test_Package_01.MainTest_01 import EmpikSearch01
from test_Package_02.MainTest_02 import EmpikSearch02
from test_Package_03.MainTest_03 import EmpikSearch03

test_01_add_to_cart = unittest.TestLoader().loadTestsFromTestCase(EmpikSearch01)
test_02_delete_from_cart = unittest.TestLoader().loadTestsFromTestCase(EmpikSearch02)
test_03_delete_from_cart = unittest.TestLoader().loadTestsFromTestCase(EmpikSearch03)

Test_suit_no_1 = unittest.TestSuite([test_01_add_to_cart, test_02_delete_from_cart, test_03_delete_from_cart])

unittest.TextTestRunner(verbosity=2).run(Test_suit_no_1)
