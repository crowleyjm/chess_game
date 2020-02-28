# Author: Jillian Crowley
# Date: 02/28/2020
# Description:


class XiangqiGame:
    """
    Represents a XiangqiGame with id_code and title data members.
    """

    def __init__(self):
        """
        Returns a XiangqiGame object with initialized board.
        Locations on the board will be specified using "algebraic notation",
        with columns labeled a-i and rows labeled 1-10, with row 1 being the Red side and row 10 the Black side
        """
        # _the_board
        self._the_board = [["1", "a", "b", "c", "d", "e", "f", "g", "h", "i"],
                           ["2", "", "", "", "", "", "", "", "", ""],
                           ["3", "", "", "", "", "", "", "", "", ""],
                           ["4", "", "", "", "", "", "", "", "", ""],
                           ["5", "", "", "", "", "", "", "", "", ""],
                           ["6", "", "", "", "", "", "", "", "", ""],
                           ["7", "", "", "", "", "", "", "", "", ""],
                           ["8", "", "", "", "", "", "", "", "", ""],
                           ["9", "", "", "", "", "", "", "", "", ""],
                           ["10", "", "", "", "", "", "", "", "", ""]]
        self._game_state = ""

    def get_the_board(self):
        """Returns the board."""
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

