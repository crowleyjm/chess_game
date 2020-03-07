# Author: Jillian Crowley
# Date: 03/07/2020
# Description:  Writes unit tests for XiangqiGame.py.

import unittest
from XiangqiGame import XiangqiGame, General, Advisor, Elephant, Horse, Chariot, Cannon, Soldier


class TestXiangqiGame(unittest.TestCase, XiangqiGame, General, Advisor, Elephant, Horse, Chariot, Cannon, Soldier):
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

    def test_is_valid_move_general(self):
        game = XiangqiGame()
        result_1 = game.is_valid_move_general("e1", "e2")
        result_2 = game.is_valid_move_general("e1", "d1")
        result_3 = game.is_valid_move_general("e1", "f1")
        final_result = (result_1, result_2, result_3)
        self.assertEqual(final_result, (True, True, True))
    #
    # def test_advisor_is_legal_move(self):
    #     advisor = Advisor("red")
    #     color = advisor.get_color()
    #     result_1 = advisor.is_legal_move("d1", "e2")
    #     result_2 = advisor.is_legal_move("f1", "e2")
    #     result_3 = advisor.is_legal_move("e2", "d3")
    #     result_4 = advisor.is_legal_move("d1", "d2")
    #     result_5 = advisor.is_legal_move("f1", "e1")
    #     result_6 = advisor.is_legal_move("f1", "g2")
    #     final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
    #     self.assertEqual(final_result, ("red", True, True, True, False, False, False))
    #
    # def test_elephant_is_legal_move(self):
    #     elephant = Elephant("red")
    #     color = elephant.get_color()
    #     result_1 = elephant.is_legal_move("c1", "a3")
    #     result_2 = elephant.is_legal_move("a3", "c5")
    #     result_3 = elephant.is_legal_move("g1", "e3")
    #     result_4 = elephant.is_legal_move("c5", "d7")
    #     result_5 = elephant.is_legal_move("c1", "d2")
    #     result_6 = elephant.is_legal_move("g1", "g2")
    #     final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
    #     self.assertEqual(final_result, ("red", True, True, True, False, False, False))
    #
    # def test_is_valid_move_elephant(self):
    #     game = XiangqiGame()
    #     result_1 = game.is_valid_move_elephant("e1", "d1")
    #     result_2 = game.is_valid_move_elephant("e1", "f1")
    #     result_3 = game.is_valid_move_elephant("e1", "e2")
    #     result_4 = game.is_valid_move_elephant("e1", "d2")
    #     result_5 = game.is_valid_move_elephant("e1", "f2")
    #     result_6 = game.is_valid_move_elephant("f1", "g1")
    #     final_result = (result_1, result_2, result_3, result_4, result_5, result_6)
    #     self.assertEqual(final_result, (True, True, True, False, False, False))
    #
    # def test_horse_is_legal_move(self):
    #     horse = Horse("red")
    #     color = horse.get_color()
    #     result_1 = horse.is_legal_move("b1", "c3")
    #     result_2 = horse.is_legal_move("h1", "g3")
    #     result_3 = horse.is_legal_move("b1", "a3")
    #     result_4 = horse.is_legal_move("b1", "b3")
    #     result_5 = horse.is_legal_move("c3", "e3")
    #     result_6 = horse.is_legal_move("h1", "e1")
    #     final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
    #     self.assertEqual(final_result, ("red", True, True, True, False, False, False))
    #
    # def test_is_valid_move_horse(self):
    #     game = XiangqiGame()
    #     result_1 = game.is_valid_move_horse("e1", "d1")
    #     result_2 = game.is_valid_move_horse("e1", "f1")
    #     result_3 = game.is_valid_move_horse("e1", "e2")
    #     result_4 = game.is_valid_move_horse("e1", "d2")
    #     result_5 = game.is_valid_move_horse("e1", "f2")
    #     result_6 = game.is_valid_move_horse("f1", "g1")
    #     final_result = (result_1, result_2, result_3, result_4, result_5, result_6)
    #     self.assertEqual(final_result, (True, True, True, False, False, False))
    #
    # def test_chariot_is_legal_move(self):
    #     chariot = Chariot("red")
    #     color = chariot .get_color()
    #     result_1 = chariot.is_legal_move("a1", "a2")
    #     result_2 = chariot.is_legal_move("a1", "a3")
    #     result_3 = chariot.is_legal_move("i1", "a1")
    #     result_4 = chariot.is_legal_move("a1", "b2")
    #     result_5 = chariot.is_legal_move("a1", "c3")
    #     result_6 = chariot.is_legal_move("i1", "h3")
    #     final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
    #     self.assertEqual(final_result, ("red", True, True, True, False, False, False))
    #
    # def test_is_valid_move_chariot(self):
    #     game = XiangqiGame()
    #     result_1 = game.is_valid_move_chariot("e1", "d1")
    #     result_2 = game.is_valid_move_chariot("e1", "f1")
    #     result_3 = game.is_valid_move_chariot("e1", "e2")
    #     result_4 = game.is_valid_move_chariot("e1", "d2")
    #     result_5 = game.is_valid_move_chariot("e1", "f2")
    #     result_6 = game.is_valid_move_chariot("f1", "g1")
    #     final_result = (result_1, result_2, result_3, result_4, result_5, result_6)
    #     self.assertEqual(final_result, (True, True, True, False, False, False))
    #
    # def test_cannon_is_legal_move(self):
    #     cannon = Cannon("red")
    #     color = cannon.get_color()
    #     result_1 = cannon.is_legal_move("a1", "a5")
    #     result_2 = cannon.is_legal_move("a1", "a9")
    #     result_3 = cannon.is_legal_move("i1", "a1")
    #     result_4 = cannon.is_legal_move("a1", "b3")
    #     result_5 = cannon.is_legal_move("a1", "c4")
    #     result_6 = cannon.is_legal_move("i1", "g2")
    #     final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
    #     self.assertEqual(final_result, ("red", True, True, True, False, False, False))
    #
    # def test_is_valid_move_cannon(self):
    #     game = XiangqiGame()
    #     result_1 = game.is_valid_move_cannon("e1", "d1")
    #     result_2 = game.is_valid_move_cannon("e1", "f1")
    #     result_3 = game.is_valid_move_cannon("e1", "e2")
    #     result_4 = game.is_valid_move_cannon("e1", "d2")
    #     result_5 = game.is_valid_move_cannon("e1", "f2")
    #     result_6 = game.is_valid_move_cannon("f1", "g1")
    #     final_result = (result_1, result_2, result_3, result_4, result_5, result_6)
    #     self.assertEqual(final_result, (True, True, True, False, False, False))
    #
    # def test_soldier_is_legal_move(self):
    #     soldier = Soldier("red")
    #     color = soldier.get_color()
    #     result_1 = soldier.is_legal_move("a4", "a5")
    #     result_2 = soldier.is_legal_move("c4", "c5")
    #     result_3 = soldier.is_legal_move("a6", "b6")
    #     result_4 = soldier.is_legal_move("a4", "b4")
    #     result_5 = soldier.is_legal_move("c4", "d4")
    #     result_6 = soldier.is_legal_move("e7", "f8")
    #     final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
    #     self.assertEqual(final_result, ("red", True, True, True, False, False, False))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestXiangqiGame)
    unittest.TextTestRunner(verbosity=2).run(suite)
