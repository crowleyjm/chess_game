# Author: Jillian Crowley
# Date: 01/15/2020
# Description:  Writes six unit tests for Store.py using five different assert functions.

import unittest
from XiangqiGame import General, Advisor, Elephant, Horse, Chariot, Cannon, Soldier


class TestStore(unittest.TestCase, General, Advisor, Elephant, Horse, Chariot, Cannon, Soldier):
    """
    Contains unit tests for the functions in XiangqiGame
    """
    def test_general_is_legal_move(self):
        general = General("red")
        color = general.get_color()
        result_1 = general.is_legal_move("e1", "d1")
        result_2 = general.is_legal_move("e1", "f1")
        result_3 = general.is_legal_move("e1", "e2")
        result_4 = general.is_legal_move("e1", "d2")
        result_5 = general.is_legal_move("e1", "f2")
        result_6 = general.is_legal_move("f1", "g1")
        final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, ("red", True, True, True, False, False, False))



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStore)
    unittest.TextTestRunner(verbosity=2).run(suite)