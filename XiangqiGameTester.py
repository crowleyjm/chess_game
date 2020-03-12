# Author: Jillian Crowley
# Date: 03/11/2020
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
        result_6 = general.is_legal_move("e10", "f9")
        final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, ("red", True, True, True, False, False, False))

    def test_advisor_is_legal_move(self):
        advisor = Advisor("red")
        color = advisor.get_color()
        result_1 = advisor.is_legal_move("d1", "e2")
        result_2 = advisor.is_legal_move("f1", "e2")
        result_3 = advisor.is_legal_move("e2", "d3")
        result_4 = advisor.is_legal_move("d1", "d2")
        result_5 = advisor.is_legal_move("f1", "e1")
        result_6 = advisor.is_legal_move("f1", "g2")
        final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, ("red", True, True, True, False, False, False))

    def test_elephant_is_legal_move(self):
        elephant = Elephant("red")
        color = elephant.get_color()
        result_1 = elephant.is_legal_move("c1", "a3")
        result_2 = elephant.is_legal_move("a3", "c5")
        result_3 = elephant.is_legal_move("g1", "e3")
        result_4 = elephant.is_legal_move("c5", "d7")
        result_5 = elephant.is_legal_move("c1", "d2")
        result_6 = elephant.is_legal_move("g1", "g2")
        final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, ("red", True, True, True, False, False, False))

    def test_horse_is_legal_move(self):
        horse = Horse("red")
        color = horse.get_color()
        result_1 = horse.is_legal_move("b1", "c3")
        result_2 = horse.is_legal_move("h1", "g3")
        result_3 = horse.is_legal_move("b1", "a3")
        result_4 = horse.is_legal_move("b1", "b3")
        result_5 = horse.is_legal_move("c3", "e3")
        result_6 = horse.is_legal_move("h1", "e1")
        final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, ("red", True, True, True, False, False, False))

    def test_chariot_is_legal_move(self):
        chariot = Chariot("red")
        color = chariot .get_color()
        result_1 = chariot.is_legal_move("a1", "a2")
        result_2 = chariot.is_legal_move("a1", "a3")
        result_3 = chariot.is_legal_move("i1", "a1")
        result_4 = chariot.is_legal_move("a1", "b2")
        result_5 = chariot.is_legal_move("a1", "c3")
        result_6 = chariot.is_legal_move("i1", "h3")
        final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, ("red", True, True, True, False, False, False))

    def test_cannon_is_legal_move(self):
        cannon = Cannon("red")
        color = cannon.get_color()
        result_1 = cannon.is_legal_move("a1", "a5")
        result_2 = cannon.is_legal_move("a1", "a9")
        result_3 = cannon.is_legal_move("i1", "a1")
        result_4 = cannon.is_legal_move("a1", "b3")
        result_5 = cannon.is_legal_move("a1", "c4")
        result_6 = cannon.is_legal_move("i1", "g2")
        final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, ("red", True, True, True, False, False, False))

    def test_soldier_is_legal_move(self):
        soldier = Soldier("red")
        color = soldier.get_color()
        result_1 = soldier.is_legal_move("a4", "a5")
        result_2 = soldier.is_legal_move("c4", "c5")
        result_3 = soldier.is_legal_move("a6", "b6")
        result_4 = soldier.is_legal_move("a4", "b4")
        result_5 = soldier.is_legal_move("c4", "d4")
        result_6 = soldier.is_legal_move("e7", "f8")
        final_result = (color, result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, ("red", True, True, True, False, False, False))

    def test_is_valid_move_general(self):
        game = XiangqiGame()
        result_1 = game.is_valid_move_general("e1", "e2")
        result_2 = game.is_valid_move_general("e1", "d1")
        result_3 = game.is_valid_move_general("e1", "f1")
        result_4 = game.is_valid_move_general("e10", "e9")
        result_5 = game.is_valid_move_general("e10", "d10")
        result_6 = game.is_valid_move_general("e10", "f10")
        final_result = (result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, (True, True, True, True, True, True))

    def test_is_valid_move_elephant(self):
        game = XiangqiGame()
        result_1 = game.is_valid_move_elephant("c1", "a3")
        result_2 = game.is_valid_move_elephant("c1", "e3")
        result_3 = game.is_valid_move_elephant("e1", "e2")
        result_4 = game.is_valid_move_elephant("c10", "a8")
        result_5 = game.is_valid_move_elephant("g10", "e8")
        final_result = (result_1, result_2, result_3, result_4, result_5)
        self.assertEqual(final_result, (True, True, True, True, True))

    def test_is_valid_move_horse(self):
        game = XiangqiGame()
        result_1 = game.is_valid_move_horse("b1", "a3")
        result_2 = game.is_valid_move_horse("b1", "c3")
        result_3 = game.is_valid_move_horse("b10", "c8")
        result_4 = game.is_valid_move_horse("h10", "g8")
        result_5 = game.is_valid_move_horse("h10", "i8")
        result_6 = game.is_valid_move_horse("h1", "g3")
        final_result = (result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, (True, True, True, True, True, True))

    def test_is_valid_move_chariot(self):
        game = XiangqiGame()
        result_1 = game.is_valid_move_chariot("a1", "a2")
        result_2 = game.is_valid_move_chariot("a1", "a3")
        result_3 = game.is_valid_move_chariot("i1", "i2")
        result_4 = game.is_valid_move_chariot("a10", "a8")
        result_5 = game.is_valid_move_chariot("a10", "a6")
        result_6 = game.is_valid_move_chariot("i1", "i5")
        final_result = (result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, (True, True, True, True, False, False))

    def test_is_valid_move_cannon(self):
        game = XiangqiGame()
        result_1 = game.is_valid_move_cannon("b3", "b7")
        result_2 = game.is_valid_move_cannon("h3", "e3")
        result_3 = game.is_valid_move_cannon("b8", "d8")
        result_4 = game.is_valid_move_cannon("h8", "h5")
        result_5 = game.is_valid_move_cannon("h3", "a3")
        result_6 = game.is_valid_move_cannon("b8", "b3")
        final_result = (result_1, result_2, result_3, result_4, result_5, result_6)
        self.assertEqual(final_result, (True, True, True, True, False, False))

    def test_red_wins_1(self):
        game = XiangqiGame()
        result_1 = game.make_move('h3', 'e3')
        result_2 = game.make_move('h8', 'g8')
        result_3 = game.make_move('h1', 'i3')
        result_4 = game.make_move('i10', 'i9')
        result_5 = game.make_move('i1', 'h1')
        result_6 = game.make_move('h10', 'i8')
        result_7 = game.make_move('e3', 'e7')
        result_8 = game.make_move('i8', 'g9')
        result_9 = game.make_move('b3', 'e3')
        result_10 = game.make_move('g8', 'h8')
        result_11 = game.make_move('h1', 'h8')
        result_12 = game.make_move('b8', 'b6')
        result_13 = game.make_move('h8', 'e8')
        result_14 = game.is_in_check("black")
        result_15 = game.make_move('f10', 'e9')
        result_16 = game.make_move('e8', 'i8')
        result_17 = game.make_move('c10', 'e8')
        result_18 = game.make_move('i8', 'i9')
        result_19 = game.make_move('b6', 'b2')
        result_20 = game.make_move('i9', 'g9')
        result_21 = game.make_move('c7', 'c6')
        result_22 = game.make_move('g9', 'g10')
        result_23 = game.get_game_state()
        final_result = (result_1, result_2, result_3, result_4, result_5, result_6, result_7, result_8, result_9,
                        result_10, result_11, result_12, result_13, result_14, result_15, result_16, result_17,
                        result_18, result_19, result_20, result_21, result_22, result_23)
        self.assertEqual(final_result,
                         (True, True, True, True, True, True, True, True, True, True,
                          True, True, True, True, True, True, True, True, True, True,
                          True, True, "RED_WON"))

    def test_black_wins_1(self):
        game = XiangqiGame()
        result_1 = game.make_move('h3', 'f3')
        result_2 = game.make_move('b8', 'e8')
        result_3 = game.make_move('f3', 'f6')
        result_4 = game.make_move('h10', 'g8')
        result_5 = game.make_move('h1', 'g3')
        result_6 = game.make_move('i10', 'h10')
        result_7 = game.make_move('c4', 'c5')
        result_8 = game.make_move('a10', 'a9')
        result_9 = game.make_move('c5', 'c6')
        result_10 = game.make_move('a9', 'f9')
        result_11 = game.make_move('c6', 'c7')
        result_12 = game.make_move('f9', 'f6')
        result_13 = game.make_move('c7', 'd7')
        result_14 = game.make_move('f6', 'd6')
        result_15 = game.make_move('d7', 'e7')
        result_16 = game.make_move('g8', 'e7')
        result_17 = game.make_move('i1', 'h1')
        result_18 = game.make_move('d6', 'd3')
        result_19 = game.make_move('c1', 'e3')
        result_20 = game.make_move('d3', 'b3')
        result_21 = game.make_move('a1', 'a3')
        result_22 = game.make_move('b3', 'b1')
        result_23 = game.make_move('a3', 'd3')
        result_24 = game.make_move('h8', 'h2')
        result_25 = game.make_move('h1', 'h2')
        result_26 = game.make_move('h10', 'h2')
        result_27 = game.make_move('g3', 'e2')
        result_28 = game.make_move('b10', 'c8')
        result_29 = game.make_move('d3', 'c3')
        result_30 = game.make_move('e7', 'd5')
        result_31 = game.make_move('c3', 'c8')
        result_32 = game.make_move('d5', 'f4')
        result_33 = game.make_move('c8', 'e8')
        result_34 = game.is_in_check("black")
        result_35 = game.make_move('g10', 'e8')
        result_36 = game.make_move('e4', 'e5')
        result_37 = game.make_move('f4', 'd3')
        result_38 = game.get_game_state()

        final_result = (result_1, result_2, result_3, result_4, result_5, result_6, result_7, result_8, result_9,
                        result_10, result_11, result_12, result_13, result_14, result_15, result_16, result_17,
                        result_18, result_19, result_20, result_21, result_22, result_23, result_24, result_25,
                        result_26, result_27, result_28, result_29, result_30, result_31, result_32, result_33,
                        result_34, result_35, result_36, result_37, result_38)
        self.assertEqual(final_result,
                         (True, True, True, True, True, True, True, True, True, True,
                          True, True, True, True, True, True, True, True, True, True,
                          True, True, True, True, True, True, True, True, True, True,
                          True, True, True, True, True, True, True, "BLACK_WON"))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestXiangqiGame)
    unittest.TextTestRunner(verbosity=2).run(suite)
