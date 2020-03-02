# Author: Jillian Crowley
# Date: 02/28/2020
# Description:


class XiangqiGame:
    """
    Represents a XiangqiGame with _the_board data member.
    """

    def __init__(self):
        """
        Returns a XiangqiGame object with initialized board.
        Locations on the board will be specified using "algebraic notation",
        with columns labeled a-i and rows labeled 1-10, with row 1 being the Red side and row 10 the Black side
        """
        # _the_board
        self._the_board_test = [["r", "a1", "r", "b1", "r", "c1", "r", "d1", "r", "e1", "r", "f1", "r", "g1", "h1", "i1"],
                           ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2"],
                           ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3"],
                           ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4"],
                           ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "i5"],
                           ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "i6"],
                           ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "i7"],
                           ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "i8"],
                           ["a9", "b9", "c9", "d9", "e9", "f9", "g9", "h9", "i9"],
                           ["a10", "b10", "c10", "d10", "e10", "f10", "g10", "h10", "i10"]]

        self._the_board = \
            [["red_chariot_1", "red_horse_1", "red_elephant_1", "red_advisor_1", "red_general", "red_advisor_2", "red_elephant_2", "red_horse_2"", "red_chariot_2"],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["black_chariot_1", "black_horse_1", "black_elephant_1", "black_advisor_1", "black_general", "black_advisor_2", "black_elephant_2", "black_horse_2", "black_chariot_2"]]

        self._game_state = "UNFINISHED"

    def get_the_board(self):
        """Returns the board."""
        column_labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        return self._the_board

    def get_game_state(self):
        """Returns the game state, either 'UNFINISHED', 'RED_WON' or 'BLACK_WON'."""
        return self._game_state

    def is_in_check(self, player):
        """
        Takes as a parameter either 'red' or 'black' and
        returns True if that player is in check, but returns False otherwise
        """

    def make_move(self):
        """takes two parameters - strings that represent the square moved from and
        the square moved to. For example, make_move('b3', 'b10').
        If the square being moved from does not contain a piece belonging to
        the player whose turn it is, or if the indicated move is not legal, or
        if the game has already been won, then it should just return False.
        Otherwise it should make the indicated move, remove any captured piece,
        update the game state if necessary, update whose turn it is, and return True"""

