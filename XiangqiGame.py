# Author: Jillian Crowley
# Date: 03/04/2020
# Description: From Wikipedia:
# The Xiangqi game (Chinese chess) represents a battle between two 16-piece armies, with
# the object of the game being to capture the enemy's general (king).
# Notable features this game include the cannon, which must jump to capture;
# a rule prohibiting the generals from facing each other directly;
# areas on the board called the river and palace, which
# restrict the movement of some pieces (but enhance that of others);
# and placement of the pieces on the intersections of the board lines, rather than within the squares.


class XiangqiGame:
    """
    Represents a XiangqiGame with _the_board data member.
    """

    def __init__(self):
        """
        Returns a XiangqiGame object with initialized board.
        Locations on the board are specified using "algebraic notation",
        with columns labeled a-i and rows labeled 1-10, with row 1 being the Red side and row 10 the Black side
        """
        # initializes board with red and black game pieces and labeled rows/ranks and columns/files
        self._the_board = \
            [[Chariot("red"), Horse("red"), Elephant("red"),
              Advisor("red"), General("red"), Advisor("red"),
              Elephant("red"), Horse("red"), Chariot("red"), "1"],
             ["", "", "", "", "", "", "", "", "", "2"],
             ["", Cannon("red"), "", "", "", "", "", Cannon("red"), "", "3"],
             [Soldier("red"), "", Soldier("red"), "", Soldier("red"),
              "", Soldier("red"), "", Soldier("red"), "4"],
             ["", "", "", "", "", "", "", "", "", "5"],
             ["", "", "", "", "", "", "", "", "", "6"],
             [Soldier("red"), "", Soldier("red"), "", Soldier("red"),
              "", Soldier("red"), "", Soldier("red"), "7"],
             ["", Cannon("black"), "", "", "", "", "", Cannon("black"), "", "8"],
             ["", "", "", "", "", "", "", "", "", "9"],
             [Chariot("black"), Horse("black"), Elephant("black"),
              Advisor("black"), General("black"), Advisor("black"),
              Elephant("black"), Horse("black"), Chariot("black"), "10"],
             ["a", "b", "c", "d", "e", "f", "g", "h", "i"]]

        # initializes game state
        self._game_state = "UNFINISHED"

        # initializes player's turn
        self._player_turn = "red"

        # initializes red General's location and check status
        self._red_general_location = "e1"
        self._red_in_check = False

        # initializes black General's location and check status
        self._black_general_location = "e10"
        self._black_in_check = False

    def get_the_board(self):
        """
        Returns the board.
        """
        return self._the_board

    def print_the_board(self):
        """
        Returns the printed board with a newline for each rank.
        """
        return print("\n".join(str(rank) for rank in self._the_board))

    def get_game_state(self):
        """
        Returns the game state, either 'UNFINISHED', 'RED_WON' or 'BLACK_WON'.
        """
        return self._game_state

    def get_player_turn(self):
        """
        Returns the player's turn, either "red" or "black"
        """
        return self._player_turn

    def is_in_check(self, player):
        """
        Takes as a parameter either 'red' or 'black' and
        returns True if that player is in check, but returns False otherwise
        """
        if player == "red":
            return self._red_in_check

        if player == "black":
            return self._black_in_check

    def make_move(self, from_square, to_square):
        """
        Takes two parameters - strings that represent the square moved from and
        the square moved to. For example, make_move('b3', 'b10').
        Otherwise it should make the indicated move, remove any captured piece,
        update the game state if necessary, update whose turn it is, and return True

        If the general's player can make no move to prevent the general's capture, the situation is called "checkmate"
        Unlike in chess, in which stalemate is a draw, in xiangqi, it is a loss for the stalemated player.
        """

        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

        # return False where move cannot be made if:
        # not player's turn
        # to_square is occupied by a piece of the same color as from_square
        # move is not legally available for piece based on class definition
        # game state is finished; either RED_WON or BLACK_WON
        if self._the_board[file.index(from_square[0])][int(from_square[1:])].get_color() != self._player_turn or \
                self._the_board[file.index(to_square[0])][int(to_square[1:])].get_color() == self._player_turn or \
                self._the_board[file.index(from_square[0])][int(from_square[1:])]. \
                        get_legal_move(from_square, to_square) or \
                self._game_state != "UNFINISHED":
            return False

        # check for illegal moves in relation to other pieces and return False

        # return False if illegal move by General
        # return False when Generals cannot face each other along the same file with no intervening pieces
        if isinstance(self._the_board[file.index(from_square[0])][int(from_square[1:])], General):
            if self._the_board[file.index(from_square[0])][int(from_square[1:])].get_color() == "red":
                if (isinstance(self._the_board[9][int(to_square[1:])], General) and
                        self._the_board[8][int(to_square[1:])] == "" and self._the_board[7][
                            int(to_square[1:])] == "" and
                        self._the_board[6][int(to_square[1:])] == "" and self._the_board[5][
                            int(to_square[1:])] == "" and
                        self._the_board[4][int(to_square[1:])] == "" and self._the_board[3][
                            int(to_square[1:])] == "" and
                        self._the_board[2][int(to_square[1:])] == "" and self._the_board[1][int(to_square[1:])] == "" or
                        (isinstance(self._the_board[8][int(to_square[1:])], General) and
                         self._the_board[7][int(to_square[1:])] == "" and self._the_board[6][
                             int(to_square[1:])] == "" and
                         self._the_board[5][int(to_square[1:])] == "" and self._the_board[4][
                             int(to_square[1:])] == "" and
                         self._the_board[3][int(to_square[1:])] == "" and self._the_board[2][
                             int(to_square[1:])] == "" and
                         self._the_board[1][int(to_square[1:])] == "") or
                        (isinstance(self._the_board[7][int(to_square[1:])], General) and
                         self._the_board[6][int(to_square[1:])] == "" and self._the_board[5][
                             int(to_square[1:])] == "" and
                         self._the_board[4][int(to_square[1:])] == "" and self._the_board[3][
                             int(to_square[1:])] == "" and
                         self._the_board[2][int(to_square[1:])] == "" and self._the_board[1][
                             int(to_square[1:])] == "")):
                    return False

            if self._the_board[file.index(from_square[0])][int(from_square[1:])].get_color() == "black":
                if (isinstance(self._the_board[0][int(to_square[1:])], General) and
                        self._the_board[1][int(to_square[1:])] == "" and self._the_board[2][
                            int(to_square[1:])] == "" and
                        self._the_board[3][int(to_square[1:])] == "" and self._the_board[4][
                            int(to_square[1:])] == "" and
                        self._the_board[5][int(to_square[1:])] == "" and self._the_board[6][
                            int(to_square[1:])] == "" and
                        self._the_board[7][int(to_square[1:])] == "" and self._the_board[8][int(to_square[1:])] == "" or
                        (isinstance(self._the_board[8][int(to_square[1:])], General) and
                         self._the_board[2][int(to_square[1:])] == "" and self._the_board[3][
                             int(to_square[1:])] == "" and
                         self._the_board[4][int(to_square[1:])] == "" and self._the_board[5][
                             int(to_square[1:])] == "" and
                         self._the_board[6][int(to_square[1:])] == "" and self._the_board[7][
                             int(to_square[1:])] == "" and
                         self._the_board[8][int(to_square[1:])] == "") or
                        (isinstance(self._the_board[7][int(to_square[1:])], General) and
                         self._the_board[3][int(to_square[1:])] == "" and self._the_board[4][
                             int(to_square[1:])] == "" and
                         self._the_board[5][int(to_square[1:])] == "" and self._the_board[6][
                             int(to_square[1:])] == "" and
                         self._the_board[7][int(to_square[1:])] == "" and self._the_board[8][
                             int(to_square[1:])] == "")):
                    return False

        # return False if illegal move by Advisor
        if isinstance(self._the_board[file.index(from_square[0])][int(from_square[1:])], Advisor):
            self._the_board[file.index(from_square[0])][int(from_square[1:])].get_legal_move(from_square, to_square)

        # return False if illegal move by Elephant
        if isinstance(self._the_board[file.index(from_square[0])][int(from_square[1:])], Elephant):

            # Elephants cannot jump so return False if there is a piece blocking its first diagonal move
            if ((self._the_board[file.index(from_square[0]) + 1][int(from_square[1:]) + 1] == "" and
                 self._the_board[file.index(from_square[0]) + 2][int(from_square[1:]) + 2] ==
                 self._the_board[file.index(to_square[0])][int(to_square[1:])]) or
                    (self._the_board[file.index(from_square[0]) - 1][int(from_square[1:]) - 1] == "" and
                     self._the_board[file.index(from_square[0]) - 2][int(from_square[1:]) - 2] ==
                     self._the_board[file.index(to_square[0])][int(to_square[1:])]) or
                    (self._the_board[file.index(from_square[0]) + 1][int(from_square[1:]) - 1] == "" and
                     self._the_board[file.index(from_square[0]) + 2][int(from_square[1:]) - 2] ==
                     self._the_board[file.index(to_square[0])][int(to_square[1:])]) or
                    (self._the_board[file.index(from_square[0]) - 1][int(from_square[1:]) + 1] == "" and
                     self._the_board[file.index(from_square[0]) - 2][int(from_square[1:]) + 2] ==
                     self._the_board[file.index(to_square[0])][int(to_square[1:])])):
                return False

        # return False if illegal move by Horse
        if isinstance(self._the_board[file.index(from_square[0])][int(from_square[1:])], Horse):

            # Horses cannot jump so return False if there is a piece blocking its first orthogonal move
            if ((file.index(from_square[0]) - 2 == file.index(to_square[0]) and
                 int(from_square[1:]) - 1 == int(to_square[1:]) and
                 self._the_board[file.index(from_square[0]) - 1][int(from_square[1:])] != "") or
                    (file.index(from_square[0]) - 2 == file.index(to_square[0]) and
                     int(from_square[1:]) + 1 == int(to_square[1:]) and
                     self._the_board[file.index(from_square[0]) - 1][from_square[1:]] != "") or
                    (file.index(from_square[0]) - 1 == file.index(to_square[0]) and
                     int(from_square[1:]) + 2 == int(to_square[1:]) and
                     self._the_board[file.index(from_square[0])][from_square[1:] + 1] != "") or
                    (file.index(from_square[0]) + 1 == file.index(to_square[0]) and
                     int(from_square[1:]) + 2 == int(to_square[1:]) and
                     self._the_board[file.index(from_square[0])][from_square[1:] + 1] != "") or
                    (file.index(from_square[0]) + 2 == file.index(to_square[0]) and
                     int(from_square[1:]) + 1 == int(to_square[1:]) and
                     self._the_board[file.index(from_square[0]) + 1][from_square[1:]] != "") or
                    (file.index(from_square[0]) + 2 == file.index(to_square[0]) and
                     int(from_square[1:]) - 1 == int(to_square[1:]) and
                     self._the_board[file.index(from_square[0]) + 1][from_square[1:]] != "") or
                    (file.index(from_square[0]) + 1 == file.index(to_square[0]) and
                     int(from_square[1:]) - 2 == int(to_square[1:]) and
                     self._the_board[file.index(from_square[0])][from_square[1:] - 1] != "") or
                    (file.index(from_square[0]) - 1 == file.index(to_square[0]) and
                     int(from_square[1:]) - 2 == int(to_square[1:])) and
                    self._the_board[file.index(from_square[0])][int(from_square[1:]) - 1] != ""):
                return False

        # return False if illegal move by Chariot
        if isinstance(self._the_board[file.index(from_square[0])][int(from_square[1:])], Chariot):

            # Chariots cannot jump so return False if there is a piece in its orthogonal path
            from_square_path = from_square
            to_square_path = to_square
            i = 1
            while file.index(from_square_path[0]) != file.index(to_square_path[0]):
                if self._the_board[file.index(from_square_path[0])] == self._the_board[file.index(to_square_path[0])] \
                        and (self._the_board[file.index(from_square_path[0]) + i][int(from_square_path[1:])] != "" or
                             self._the_board[file.index(from_square_path[0]) - i][int(from_square_path[1:])] != ""):
                    return False

                if self._the_board[int(from_square_path[1:])] != self._the_board[int(to_square_path[1:])] and \
                        (self._the_board[file.index(from_square_path[0])][int(from_square_path[1:]) + i] != "" or
                         self._the_board[file.index(from_square_path[0])][int(from_square_path[1:]) - i] != ""):
                    return False
                i += 1

        # return False if illegal move by Cannon
        if isinstance(self._the_board[file.index(from_square[0])][int(from_square[1:])], Cannon):
            # Cannons move any distance orthogonally without jumping
            # if there is ONLY ONE piece in the path between square_from and square_to, then
            # the Cannon can capture and return True, otherwise return False
            from_square_path = from_square
            to_square_path = to_square
            i = 1
            count = 0
            while file.index(from_square_path[0]) != file.index(to_square_path[0]):
                if self._the_board[file.index(from_square_path[0])] == self._the_board[file.index(to_square_path[0])] \
                        and (self._the_board[file.index(from_square_path[0]) + i][int(from_square_path[1:])] != "" or
                             self._the_board[file.index(from_square_path[0]) - i][int(from_square_path[1:])] != ""):
                    count += 1

                if self._the_board[int(from_square_path[1:])] != self._the_board[int(to_square_path[1:])] and \
                        (self._the_board[file.index(from_square_path[0])][int(from_square_path[1:]) + i] != "" or
                         self._the_board[file.index(from_square_path[0])][int(from_square_path[1:]) - i] != ""):
                    count += 1

                i += 1
                if count != 1:
                    return False

        # return False if illegal move by Soldier
        if isinstance(self._the_board[file.index(from_square[0])][int(from_square[1:])], Soldier):
            self._the_board[file.index(from_square[0])][int(from_square[1:])].get_legal_move(from_square, to_square)

        # otherwise, make move and remove any captured piece
        self._the_board[file.index(to_square[0])][int(to_square[1:])] = \
            self._the_board[file.index(from_square[0])][int(from_square[1:])]
        self._the_board[file.index(from_square[0])][int(from_square[1:])] = ""

        # if red or black General moved, update location
        if isinstance(self._the_board[file.index(to_square[0])][int(to_square[1:])], General) and \
                self._the_board[file.index(to_square[0])][int(to_square[1:])].get_color() == "red":
            self._red_general_location = to_square
        if isinstance(self._the_board[file.index(to_square[0])][int(to_square[1:])], General) and \
                self._the_board[file.index(to_square[0])][int(to_square[1:])].get_color() == "black":
            self._black_general_location = to_square

        # if red or black player is in check, update check status

        # check if red player's General is in check by black Advisor as a result of the move made
        if ((isinstance(self._the_board[file.index(self._red_general_location[0] + 1)]
                        [int(self._red_general_location[1:]) + 1], Advisor) and
             self._the_board[file.index(self._red_general_location[0] + 1)]
             [int(self._red_general_location[1:]) + 1].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] - 1)]
                            [int(self._red_general_location[1:]) - 1], Advisor) and
                 self._the_board[file.index(self._red_general_location[0] - 1)]
                 [int(self._red_general_location[1:]) - 1].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] + 1)]
                            [int(self._red_general_location[1:]) - 1], Advisor) and
                 self._the_board[file.index(self._red_general_location[0] + 1)]
                 [int(self._red_general_location[1:]) - 1].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] - 1)]
                            [int(self._red_general_location[1:]) + 1], Advisor) and
                 self._the_board[file.index(self._red_general_location[0] - 1)]
                 [int(self._red_general_location[1:]) + 1].get_color() == "black")):
            self._red_in_check = True
            # if it is red player's turn, undo move and return False since player cannot
            # put its own General in check
            if self._player_turn == "red":
                self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                    self._the_board[file.index(to_square[0])][int(to_square[1:])]
                self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                return False

        # check if black player's General is in check by red Advisor as a result of the move made
        if ((isinstance(self._the_board[file.index(self._black_general_location[0] + 1)]
                        [int(self._black_general_location[1:]) + 1], Advisor) and
             self._the_board[file.index(self._black_general_location[0] + 1)]
             [int(self._black_general_location[1:]) + 1].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] - 1)]
                            [int(self._black_general_location[1:]) - 1], Advisor) and
                 self._the_board[file.index(self._black_general_location[0] - 1)]
                 [int(self._black_general_location[1:]) - 1].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] + 1)]
                            [int(self._black_general_location[1:]) - 1], Advisor) and
                 self._the_board[file.index(self._black_general_location[0] + 1)]
                 [int(self._black_general_location[1:]) - 1].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] - 1)]
                            [int(self._black_general_location[1:]) + 1], Advisor) and
                 self._the_board[file.index(self._black_general_location[0] - 1)]
                 [int(self._black_general_location[1:]) + 1].get_color() == "red")):
            self._black_in_check = True
            # if it is black player's turn, undo move and return False since player cannot
            # put its own General in check
            if self._player_turn == "black":
                self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                    self._the_board[file.index(to_square[0])][int(to_square[1:])]
                self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                return False

        # check if red player's General is in check by black Elephant as a result of the move made
        if ((isinstance(self._the_board[file.index(self._red_general_location[0] + 2)]
                        [int(self._red_general_location[1:]) + 2], Elephant) and
             self._the_board[file.index(self._red_general_location[0] + 2)]
             [int(self._red_general_location[1:]) + 2].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] - 2)]
                            [int(self._red_general_location[1:]) - 2], Elephant) and
                 self._the_board[file.index(self._red_general_location[0] - 2)]
                 [int(self._red_general_location[1:]) - 2].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] + 2)]
                            [int(self._red_general_location[1:]) - 2], Elephant) and
                 self._the_board[file.index(self._red_general_location[0] + 2)]
                 [int(self._red_general_location[1:]) - 2].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] - 2)]
                            [int(self._red_general_location[1:]) + 2], Elephant) and
                 self._the_board[file.index(self._red_general_location[0] - 2)]
                 [int(self._red_general_location[1:]) + 2].get_color() == "black")):
            self._red_in_check = True
            # if it is red player's turn, undo move and return False since player cannot
            # put its own General in check
            if self._player_turn == "red":
                self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                self._the_board[file.index(to_square[0])][int(to_square[1:])]
                self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                return False

        # check if black player's General is in check by red Elephant as a result of the move made
        if ((isinstance(self._the_board[file.index(self._black_general_location[0] + 2)]
                        [int(self._black_general_location[1:]) + 2], Elephant) and
             self._the_board[file.index(self._black_general_location[0] + 2)]
             [int(self._black_general_location[1:]) + 2].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] - 2)]
                            [int(self._black_general_location[1:]) - 2], Elephant) and
                 self._the_board[file.index(self._black_general_location[0] - 2)]
                 [int(self._black_general_location[1:]) - 2].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] + 2)]
                            [int(self._black_general_location[1:]) - 2], Elephant) and
                 self._the_board[file.index(self._black_general_location[0] + 2)]
                 [int(self._black_general_location[1:]) - 2].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] - 2)]
                            [int(self._black_general_location[1:]) + 2], Elephant) and
                 self._the_board[file.index(self._black_general_location[0] - 2)]
                 [int(self._black_general_location[1:]) + 2].get_color() == "red")):
            self._black_in_check = True
            # if it is black player's turn, undo move and return False since player cannot
            # put its own General in check
            if self._player_turn == "black":
                self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                    self._the_board[file.index(to_square[0])][int(to_square[1:])]
                self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                return False

        # check if red player's General is in check by black Horse as a result of the move made
        if ((isinstance(self._the_board[file.index(self._red_general_location[0] - 2)]
                        [int(self._red_general_location[1:]) - 1], Horse) and
             self._the_board[file.index(self._red_general_location[0] - 2)]
             [int(self._red_general_location[1:]) - 1].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] - 2)]
                            [int(self._red_general_location[1:]) + 1], Horse) and
                 self._the_board[file.index(self._red_general_location[0] - 2)]
                 [int(self._red_general_location[1:]) + 1].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] + 1)]
                            [int(self._red_general_location[1:]) + 2], Horse) and
                 self._the_board[file.index(self._red_general_location[0] - 1)]
                 [int(self._red_general_location[1:]) + 2].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] + 1)]
                            [int(self._red_general_location[1:]) + 2], Horse) and
                 self._the_board[file.index(self._red_general_location[0] + 1)]
                 [int(self._red_general_location[1:]) + 2].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] + 2)]
                            [int(self._red_general_location[1:]) + 1], Horse) and
                 self._the_board[file.index(self._red_general_location[0] + 2)]
                 [int(self._red_general_location[1:]) + 1].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] + 2)]
                            [int(self._red_general_location[1:]) - 1], Horse) and
                 self._the_board[file.index(self._red_general_location[0] + 2)]
                 [int(self._red_general_location[1:]) - 1].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] + 1)]
                            [int(self._red_general_location[1:]) - 2], Horse) and
                 self._the_board[file.index(self._red_general_location[0] + 1)]
                 [int(self._red_general_location[1:]) - 2].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0] - 1)]
                            [int(self._red_general_location[1:]) - 2], Horse) and
                 self._the_board[file.index(self._red_general_location[0] - 1)]
                 [int(self._red_general_location[1:]) - 2].get_color() == "black")):
            self._red_in_check = True
            # if it is red player's turn, undo move and return False since player cannot
            # put its own General in check
            if self._player_turn == "red":
                self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                    self._the_board[file.index(to_square[0])][int(to_square[1:])]
                self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                return False

        # check if black player's General is in check by red Horse as a result of the move made
        if ((isinstance(self._the_board[file.index(self._black_general_location[0] - 2)]
                        [int(self._black_general_location[1:]) - 1], Horse) and
             self._the_board[file.index(self._black_general_location[0] - 2)]
             [int(self._black_general_location[1:]) - 1].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] - 2)]
                            [int(self._black_general_location[1:]) + 1], Horse) and
                 self._the_board[file.index(self._black_general_location[0] - 2)]
                 [int(self._black_general_location[1:]) + 1].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] + 1)]
                            [int(self._black_general_location[1:]) + 2], Horse) and
                 self._the_board[file.index(self._black_general_location[0] - 1)]
                 [int(self._black_general_location[1:]) + 2].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] + 1)]
                            [int(self._black_general_location[1:]) + 2], Horse) and
                 self._the_board[file.index(self._black_general_location[0] + 1)]
                 [int(self._black_general_location[1:]) + 2].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] + 2)]
                            [int(self._black_general_location[1:]) + 1], Horse) and
                 self._the_board[file.index(self._black_general_location[0] + 2)]
                 [int(self._black_general_location[1:]) + 1].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] + 2)]
                            [int(self._black_general_location[1:]) - 1], Horse) and
                 self._the_board[file.index(self._black_general_location[0] + 2)]
                 [int(self._black_general_location[1:]) - 1].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] + 1)]
                            [int(self._black_general_location[1:]) - 2], Horse) and
                 self._the_board[file.index(self._black_general_location[0] + 1)]
                 [int(self._black_general_location[1:]) - 2].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0] - 1)]
                            [int(self._black_general_location[1:]) - 2], Horse) and
                 self._the_board[file.index(self._black_general_location[0] - 1)]
                 [int(self._black_general_location[1:]) - 2].get_color() == "red")):
            self._black_in_check = True
            # if it is black player's turn, undo move and return False since player cannot
            # put its own General in check
            if self._player_turn == "black":
                self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                    self._the_board[file.index(to_square[0])][int(to_square[1:])]
                self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                return False

        # check if red player's General is in check by black Chariot as a result of the move made
        i = 1
        while file.index(self._red_general_location[0] + i) < 10:
            if ((isinstance(self._the_board[file.index(self._red_general_location[0] + i)]
                            [int(self._red_general_location[1:])], Chariot) and
                 self._the_board[file.index(self._red_general_location[0] + i)]
                 [int(self._red_general_location[1:])].get_color() == "black")) or \
                    (isinstance(self._the_board[file.index(self._red_general_location[0] - i)]
                                [int(self._red_general_location[1:])], Chariot) and
                     self._the_board[file.index(self._red_general_location[0] - i)]
                     [int(self._red_general_location[1:])].get_color() == "black"):
                self._red_in_check = True
                # if it is red player's turn, undo move and return False since player cannot
                # put its own General in check
                if self._player_turn == "red":
                    self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                        self._the_board[file.index(to_square[0])][int(to_square[1:])]
                    # WON'T WORK. NEED TO PUT BACK CAPTURED PIECE
                    self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                    return False
            elif self._the_board[file.index(self._red_general_location[0] + i)] == "" or \
                    self._the_board[file.index(self._red_general_location[0] - i)] == "":
                i += 1

        i = 1
        while file.index(self._red_general_location[1:] + i) < 11:
            if ((isinstance(self._the_board[file.index(self._red_general_location[0])]
                            [int(self._red_general_location[1:]) + i], Chariot) and
                 self._the_board[file.index(self._red_general_location[0])]
                 [int(self._red_general_location[1:]) + i].get_color() == "black")) or \
                    (isinstance(self._the_board[file.index(self._red_general_location[0])]
                                [int(self._red_general_location[1:]) - i], Chariot) and
                     self._the_board[file.index(self._red_general_location[0])]
                     [int(self._red_general_location[1:]) - i].get_color() == "black"):
                self._red_in_check = True
                # if it is red player's turn, undo move and return False since player cannot
                # put its own General in check
                if self._player_turn == "black":
                    self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                        self._the_board[file.index(to_square[0])][int(to_square[1:])]
                    self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                    return False
            elif self._the_board[int(self._red_general_location[1:]) + i] == "" or \
                    self._the_board[int(self._red_general_location[1:]) - i] == "":
                i += 1

        # check if black player's General is in check by red Chariot as a result of the move made
        i = 1
        while file.index(self._black_general_location[0] + i) < 10:
            if ((isinstance(self._the_board[file.index(self._black_general_location[0] + i)]
                            [int(self._black_general_location[1:])], Chariot) and
                 self._the_board[file.index(self._black_general_location[0] + i)]
                 [int(self._black_general_location[1:])].get_color() == "red")) or \
                    (isinstance(self._the_board[file.index(self._black_general_location[0] - i)]
                                [int(self._black_general_location[1:])], Chariot) and
                     self._the_board[file.index(self._black_general_location[0] - i)]
                     [int(self._black_general_location[1:])].get_color() == "red"):
                self._black_in_check = True
                # if it is red player's turn, undo move and return False since player cannot
                # put its own General in check
                if self._player_turn == "black":
                    self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                        self._the_board[file.index(to_square[0])][int(to_square[1:])]
                    self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                    return False
            elif self._the_board[file.index(self._black_general_location[0] + i)] == "" or \
                    self._the_board[file.index(self._black_general_location[0] - i)] == "":
                i += 1

        i = 1
        while file.index(int(self._black_general_location[1:]) + i) < 11:
            if ((isinstance(self._the_board[file.index(self._black_general_location[0])]
                            [int(self._black_general_location[1:]) + i], Chariot) and
                 self._the_board[file.index(self._black_general_location[0])]
                 [int(self._black_general_location[1:]) + i].get_color() == "red")) or \
                    (isinstance(self._the_board[file.index(self._black_general_location[0])]
                                [int(self._black_general_location[1:]) - i], Chariot) and
                     self._the_board[file.index(self._black_general_location[0])]
                     [int(self._black_general_location[1:]) - i].get_color() == "red"):
                self._black_in_check = True
                # if it is red player's turn, undo move and return False since player cannot
                # put its own General in check
                if self._player_turn == "black":
                    self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                        self._the_board[file.index(to_square[0])][int(to_square[1:])]
                    self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                    return False
            elif self._the_board[int(self._black_general_location[1:]) + i] == "" or \
                    self._the_board[int(self._black_general_location[1:]) - i] == "":
                i += 1

        # check if red player's General is in check by black Cannon as a result of the move made
        i = 1
        count = 0
        while file.index(self._red_general_location[0] + i) < 10:
            if ((isinstance(self._the_board[file.index(self._red_general_location[0] + i)]
                            [int(self._red_general_location[1:])], Chariot) and
                 self._the_board[file.index(self._red_general_location[0] + i)]
                 [int(self._red_general_location[1:])].get_color() == "black") is False and
                    (self._the_board[file.index(self._red_general_location[0] + i)]
                     [int(self._red_general_location[1:])] != "") or
                    (isinstance(self._the_board[file.index(self._red_general_location[0] - i)]
                                [int(self._red_general_location[1:])], Chariot) and
                     self._the_board[file.index(self._red_general_location[0] - i)]
                     [int(self._red_general_location[1:])].get_color() == "black") is False and
                    (self._the_board[file.index(self._red_general_location[0] - i)]
                     [int(self._red_general_location[1:])] != "")):
                count += 1
                i += 1

        if count == 1:
            while file.index(self._red_general_location[0] + i) < 10:
                if ((isinstance(self._the_board[file.index(self._red_general_location[0] + i)]
                                [int(self._red_general_location[1:])], Chariot) and
                     self._the_board[file.index(self._red_general_location[0] + i)]
                     [int(self._red_general_location[1:])].get_color() == "black")) or \
                        (isinstance(self._the_board[file.index(self._red_general_location[0] - i)]
                                    [int(self._red_general_location[1:])], Chariot) and
                         self._the_board[file.index(self._red_general_location[0] - i)]
                         [int(self._red_general_location[1:])].get_color() == "black"):
                    self._red_in_check = True
                    # if it is red player's turn, undo move and return False since player cannot
                    # put its own General in check
                    if self._player_turn == "red":
                        self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                            self._the_board[file.index(to_square[0])][int(to_square[1:])]
                        self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                        return False
                elif self._the_board[file.index(self._red_general_location[0] + i)] == "" or \
                        self._the_board[file.index(self._red_general_location[0] - i)] == "":
                    i += 1

        i = 1
        count = 0
        while file.index(self._red_general_location[0] + i) < 11:
            if ((isinstance(self._the_board[file.index(self._red_general_location[0])]
                            [int(self._red_general_location[1:]) + i], Chariot) and
                 self._the_board[file.index(self._red_general_location[0])]
                 [int(self._red_general_location[1:]) + i].get_color() == "black") is False and
                    (self._the_board[file.index(self._red_general_location[0])]
                     [int(self._red_general_location[1:]) + i] != "") or
                    (isinstance(self._the_board[file.index(self._red_general_location[0])]
                                [int(self._red_general_location[1:]) - i], Chariot) and
                     self._the_board[file.index(self._red_general_location[0])]
                     [int(self._red_general_location[1:]) - i].get_color() == "black") is False and
                    (self._the_board[file.index(self._red_general_location[0])]
                     [int(self._red_general_location[1:]) - i] != "")):
                count += 1
                i += 1

        if count == 1:
            while file.index(self._red_general_location[0] + i) < 11:
                if ((isinstance(self._the_board[file.index(self._red_general_location[0])]
                                [int(self._red_general_location[1:]) + i], Chariot) and
                     self._the_board[file.index(self._red_general_location[0])]
                     [int(self._red_general_location[1:]) + i].get_color() == "black")) or \
                        (isinstance(self._the_board[file.index(self._red_general_location[0])]
                                    [int(self._red_general_location[1:]) - i], Chariot) and
                         self._the_board[file.index(self._red_general_location[0])]
                         [int(self._red_general_location[1:]) - i].get_color() == "black"):
                    self._red_in_check = True
                    # if it is red player's turn, undo move and return False since player cannot
                    # put its own General in check
                    if self._player_turn == "red":
                        self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                            self._the_board[file.index(to_square[0])][int(to_square[1:])]
                        self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                        return False
                elif self._the_board[file.index(self._red_general_location[0] + i)] == "" or \
                        self._the_board[file.index(self._red_general_location[0] - i)] == "":
                    i += 1

        # check if black player's General is in check by red Cannon as a result of the move made
        i = 1
        count = 0
        while file.index(self._black_general_location[0] + i) < 10:
            if ((isinstance(self._the_board[file.index(self._black_general_location[0] + i)]
                            [int(self._black_general_location[1:])], Chariot) and
                 self._the_board[file.index(self._black_general_location[0] + i)]
                 [int(self._black_general_location[1:])].get_color() == "red") is False and
                    (self._the_board[file.index(self._black_general_location[0] + i)]
                     [int(self._black_general_location[1:])] != "") or
                    (isinstance(self._the_board[file.index(self._black_general_location[0] - i)]
                                [int(self._black_general_location[1:])], Chariot) and
                     self._the_board[file.index(self._black_general_location[0] - i)]
                     [int(self._black_general_location[1:])].get_color() == "red") is False and
                    (self._the_board[file.index(self._black_general_location[0] - i)]
                     [int(self._black_general_location[1:])] != "")):
                count += 1
                i += 1

        if count == 1:
            while file.index(self._black_general_location[0] + i) < 10:
                if ((isinstance(self._the_board[file.index(self._black_general_location[0] + i)]
                                [int(self._black_general_location[1:])], Chariot) and
                     self._the_board[file.index(self._black_general_location[0] + i)]
                     [int(self._black_general_location[1:])].get_color() == "black")) or \
                        (isinstance(self._the_board[file.index(self._black_general_location[0] - i)]
                                    [int(self._black_general_location[1:])], Chariot) and
                         self._the_board[file.index(self._black_general_location[0] - i)]
                         [int(self._black_general_location[1:])].get_color() == "black"):
                    self._black_in_check = True
                    # if it is red player's turn, undo move and return False since player cannot
                    # put its own General in check
                    if self._player_turn == "black":
                        self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                            self._the_board[file.index(to_square[0])][int(to_square[1:])]
                        self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                        return False
                elif self._the_board[file.index(self._black_general_location[0] + i)] == "" or \
                        self._the_board[file.index(self._black_general_location[0] - i)] == "":
                    i += 1

        i = 1
        count = 0
        while file.index(self._black_general_location[0] + i) < 11:
            if ((isinstance(self._the_board[file.index(self._black_general_location[0])]
                            [int(self._black_general_location[1:]) + i], Chariot) and
                 self._the_board[file.index(self._black_general_location[0])]
                 [int(self._black_general_location[1:]) + i].get_color() == "red") is False and
                    (self._the_board[file.index(self._black_general_location[0])]
                     [int(self._black_general_location[1:]) + i] != "") or
                    (isinstance(self._the_board[file.index(self._black_general_location[0])]
                                [int(self._black_general_location[1:]) - i], Chariot) and
                     self._the_board[file.index(self._black_general_location[0])]
                     [int(self._black_general_location[1:]) - i].get_color() == "red") is False and
                    (self._the_board[file.index(self._black_general_location[0])]
                     [int(self._black_general_location[1:]) - i] != "")):
                count += 1
                i += 1

        if count == 1:
            while file.index(self._black_general_location[0] + i) < 11:
                if ((isinstance(self._the_board[file.index(self._black_general_location[0])]
                                [int(self._black_general_location[1:]) + i], Chariot) and
                     self._the_board[file.index(self._black_general_location[0])]
                     [int(self._black_general_location[1:]) + i].get_color() == "red")) or \
                        (isinstance(self._the_board[file.index(self._black_general_location[0])]
                                    [int(self._black_general_location[1:]) - i], Chariot) and
                         self._the_board[file.index(self._black_general_location[0])]
                         [int(self._black_general_location[1:]) - i].get_color() == "red"):
                    self._black_in_check = True
                    # if it is red player's turn, undo move and return False since player cannot
                    # put its own General in check
                    if self._player_turn == "black":
                        self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                            self._the_board[file.index(to_square[0])][int(to_square[1:])]
                        self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                        return False
                elif self._the_board[file.index(self._black_general_location[0] + i)] == "" or \
                        self._the_board[file.index(self._black_general_location[0] - i)] == "":
                    i += 1

        # check if red player's General is in check by black Soldier as a result of the move made
        if ((isinstance(self._the_board[file.index(self._red_general_location[0] - 1)]
                        [int(self._red_general_location[1:])], Soldier) and
             self._the_board[file.index(self._red_general_location[0] - 1)]
             [int(self._red_general_location[1:])].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0])]
                            [int(self._red_general_location[1:]) - 1], Soldier) and
                 self._the_board[file.index(self._red_general_location[0])]
                 [int(self._red_general_location[1:]) - 1].get_color() == "black") or
                (isinstance(self._the_board[file.index(self._red_general_location[0])]
                            [int(self._red_general_location[1:]) + 1], Soldier) and
                 self._the_board[file.index(self._red_general_location[0])]
                 [int(self._red_general_location[1:]) + 1].get_color() == "black")):
            self._red_in_check = True
            # if it is red player's turn, undo move and return False since player cannot
            # put its own General in check
            if self._player_turn == "red":
                self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                    self._the_board[file.index(to_square[0])][int(to_square[1:])]
                self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                return False

        # check if black player's General is in check by red Soldier as a result of the move made
        if ((isinstance(self._the_board[file.index(self._black_general_location[0] - 1)]
                        [int(self._black_general_location[1:])], Soldier) and
             self._the_board[file.index(self._black_general_location[0] - 1)]
             [int(self._black_general_location[1:])].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0])]
                            [int(self._black_general_location[1:]) - 1], Soldier) and
                 self._the_board[file.index(self._black_general_location[0])]
                 [int(self._black_general_location[1:]) - 1].get_color() == "red") or
                (isinstance(self._the_board[file.index(self._black_general_location[0])]
                            [int(self._black_general_location[1:]) + 1], Soldier) and
                 self._the_board[file.index(self._black_general_location[0])]
                 [int(self._black_general_location[1:]) + 1].get_color() == "red")):
            self._black_in_check = True
            # if it is black player's turn, undo move and return False since player cannot
            # put its own General in check
            if self._player_turn == "black":
                self._the_board[file.index(from_square[0])][int(from_square[1:])] = \
                    self._the_board[file.index(to_square[0])][int(to_square[1:])]
                self._the_board[file.index(to_square[0])][int(to_square[1:])] = ""
                return False

        # # if red General is in checkmate or red player is in stalemate, update _game_state to "BLACK WON"
        # # if red player no legal moves):
        # if self._player_turn == "red":
        #     self._game_state = "BLACK_WON"
        #
        # # if black General is in checkmate or black player is in stalemate, update _game_state to "RED WON"
        # # if black player has no legal moves):
        # if self._player_turn == "black":
        #     self._game_state = "RED_WON"

        # update _player_turn
        if self._player_turn == "red":
            self._player_turn = "black"

        if self._player_turn == "black":
            self._player_turn = "red"

        return True


class General:
    """
    Represents a General with data members: color, rank, and file.
    The general starts the game at the midpoint of the back edge, within the palace.
    The general may move and capture one point orthogonally and may not leave the palace, with the following exception.
    The two generals may not face each other along the same file with no intervening pieces.
    If that happens, the "flying general" move may be executed, in which the general to
    move may cross the board to capture the enemy general.
    In practice, this rule means that creating this situation in the first place means
    moving into check, and is therefore not allowed
    """

    def __init__(self, color):
        self._color = color

    def get_color(self):
        """
        Returns piece color
        """
        return self._color

    def is_legal_move(self, from_square, to_square):
        """
        Returns True if legal move and False if illegal move
        Only considers space itself and move style (one space orthogonally)
        """
        # list of files to associate index values
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

        if self._color == "red" and \
                file.index(from_square[0]) < 3 and 6 > int(from_square[1:]) > 2 and \
                ((file.index(to_square[0]) + 1 == file.index(from_square[0]) or
                  (file.index(to_square[0]) - 1 == file.index(from_square[0])) and
                  int(to_square[1:]) - int(from_square[1:]) == 0)) or \
                (file.index(to_square[0]) - file.index(from_square[0]) == 0 and
                 (int(to_square[1:]) + 1 == int(from_square[1:]) or int(to_square[1:]) - 1 == int(from_square[1:]))):
            return True

        if self._color == "black" and \
                file.index(from_square[0]) > 6 and 6 > int(from_square[1:]) > 2 and \
                ((file.index(to_square[0]) + 1 == file.index(from_square[0]) or
                  (file.index(to_square[0]) - 1 == file.index(from_square[0])) and
                  int(to_square[1:]) - int(from_square[1:]) == 0)) or \
                (file.index(to_square[0]) - file.index(from_square[0]) == 0 and
                 (int(to_square[1:]) + 1 == int(from_square[1:]) or int(to_square[1:]) - 1 == int(from_square[1:]))):
            return True
        return False


class Advisor:
    """
    Represents an Advisor with data members: color, rank, and file.
    The advisors start on either side of the general. They move and capture one point diagonally and
    may not leave the palace, which confines them to five points on the board.
    The advisor is like the queen in Western chess.
    """

    def __init__(self, color):
        self._color = color

    def get_color(self):
        """
        Returns piece color
        """
        return self._color

    def is_legal_move(self, from_square, to_square):
        """
        Returns True if legal move and False if illegal move
        Only considers space itself and move style (one space diagonally)
        """
        # list of files to associate index values
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

        if self._color == "red" and \
                file.index(from_square[0]) < 3 and 6 > int(from_square[1:]) > 2 and \
                (file.index(to_square[0]) == file.index(from_square[0]) + 1 and
                 int(to_square[1:]) == int(from_square[1:]) + 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 1 and
                 int(to_square[1:]) == int(from_square[1:]) - 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) + 1 and
                 int(to_square[1:]) == int(from_square[1:]) - 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 1 and
                 int(to_square[1:]) == int(from_square[1:]) + 1):
            return True

        if self._color == "black" and \
                file.index(from_square[0]) > 6 and 6 > int(from_square[1:]) > 2 and \
                (file.index(to_square[0]) == file.index(from_square[0]) + 1 and
                 int(to_square[1:]) == int(from_square[1:]) + 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 1 and
                 int(to_square[1:]) == int(from_square[1:]) - 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) + 1 and
                 int(to_square[1:]) == int(from_square[1:]) - 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 1 and
                 int(to_square[1:]) == int(from_square[1:]) + 1):
            return True
        return False


class Elephant:
    """
    Represents an Elephant with data members: color, rank, and file.
    These pieces move and capture exactly two points diagonally and may not jump over intervening pieces;
    If an elephant cannot move due to a diagonally adjacent piece, it is known as
    "blocking the elephant's eye"
    Elephants may not cross the river, and serve as defensive pieces. Because an elephant's movement is
    restricted to just seven board positions, it can be easily trapped or threatened.
    The two elephants are often used to defend each other.
    """

    def __init__(self, color):
        self._color = color

    def get_color(self):
        """
        Returns piece color
        """
        return self._color

    def is_legal_move(self, from_square, to_square):
        """
        Returns True if legal move and False if illegal move
        Only considers space itself and move style (two spaces diagonally and cannot cross river)
        """
        # list of files to associate index values
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

        # Elephants cannot cross the river
        if self._color == "red" and \
                ((file.index(from_square[0]) == 0 and int(from_square[1:]) == 2) or
                 (file.index(from_square[0]) == 0 and int(from_square[1:]) == 6) or
                 (file.index(from_square[0]) == 2 and int(from_square[1:]) == 0) or
                 (file.index(from_square[0]) == 2 and int(from_square[1:]) == 4) or
                 (file.index(from_square[0]) == 2 and int(from_square[1:]) == 9) or
                 (file.index(from_square[0]) == 4 and int(from_square[1:]) == 2) or
                 (file.index(from_square[0]) == 4 and int(from_square[1:]) == 7)) and \
                (file.index(to_square[0]) == file.index(from_square[0]) + 2 and
                 int(to_square[1:]) == int(from_square[1:]) + 2) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 2 and
                 int(to_square[1:]) == int(from_square[1:]) - 2) or \
                (file.index(to_square[0]) == file.index(from_square[0]) + 2 and
                 int(to_square[1:]) == int(from_square[1:]) - 2) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 2 and
                 int(to_square[1:]) == int(from_square[1:]) + 2):
            return True

        if self._color == "black" and \
                ((file.index(from_square[0]) == 9 and int(from_square[1:]) == 2) or
                 (file.index(from_square[0]) == 9 and int(from_square[1:]) == 6) or
                 (file.index(from_square[0]) == 7 and int(from_square[1:]) == 0) or
                 (file.index(from_square[0]) == 7 and int(from_square[1:]) == 4) or
                 (file.index(from_square[0]) == 7 and int(from_square[1:]) == 9) or
                 (file.index(from_square[0]) == 5 and int(from_square[1:]) == 2) or
                 (file.index(from_square[0]) == 5 and int(from_square[1:]) == 7)) and \
                (file.index(to_square[0]) == file.index(from_square[0]) + 2 and
                 int(to_square[1:]) == int(from_square[1:]) + 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 1 and
                 int(to_square[1:]) == int(from_square[1:]) - 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) + 2 and
                 int(to_square[1:]) == int(from_square[1:]) - 2) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 2 and
                 int(to_square[1:]) == int(from_square[1:]) + 2):
            return True
        return False


class Horse:
    """
    Represents a Horse with data members: color, rank, and file.
    Horses begin the game next to the elephants, on their outside flanks.
    A horse moves and captures one point orthogonally and then one point diagonally away from
    its former position. The horse does not jump as the knight does in Western chess, and
    can be blocked by a piece located one point horizontally or vertically adjacent to it.
    Blocking a horse is called "hobbling the horse's leg".
    Since horses can be blocked, it is sometimes possible to trap the opponent's horse.
    It is possible for one player's horse to have an asymmetric attack advantage if an opponent's horse is blocked.
    """

    def __init__(self, color):
        self._color = color

    def get_color(self):
        """
        Returns piece color
        """
        return self._color

    def get_legal_move(self, from_square, to_square):
        """
        Returns True if legal move and False if illegal move
        Only considers space itself and move style (one space orthogonal and one space diagonal)
        """
        # list of files to associate index values
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

        if ((self._color == "red" or self._color == "black") and
                ((file.index(from_square[0]) - 2 == file.index(to_square[0]) and
                  int(from_square[1:] - 1 == int(to_square[1:])) or
                 (file.index(from_square[0]) - 2 == file.index(to_square[0]) and
                  int(from_square[1:] + 1 == int(to_square[1:])) or
                 (file.index(from_square[0]) - 1 == file.index(to_square[0]) and
                  int(from_square[1:] + 2 == int(to_square[1:])) or
                 (file.index(from_square[0]) + 1 == file.index(to_square[0]) and
                  int(from_square[1:] + 2 == int(to_square[1:])) or
                 (file.index(from_square[0]) + 2 == file.index(to_square[0]) and
                  int(from_square[1:] + 1 == int(to_square[1:])) or
                 (file.index(from_square[0]) + 2 == file.index(to_square[0]) and
                  int(from_square[1:] - 1 == int(to_square[1:])) or
                 (file.index(from_square[0]) + 1 == file.index(to_square[0]) and
                  int(from_square[1:] - 2 == int(to_square[1:])) or
                 (file.index(from_square[0]) - 1 == file.index(to_square[0]) and
                  int(from_square[1:] - 2 == int(to_square[1:])))):
            return True
        return False


class Chariot:
    """
    Represents a Chariot with data members: color, rank, and file.
    The chariot moves and captures any distance orthogonally, but may not jump over intervening pieces.
    The chariots begin the game on the points at the corners of the board. The chariot is often
    considered to be the strongest piece in the game due to its freedom of movement and lack of restrictions.
    The chariot is sometimes known as the rook by English-speaking players, since it is like the rook in Western chess.
    """

    def __init__(self, color):
        self._color = color

    def get_color(self):
        """
        Returns piece color
        """
        return self._color

    def get_legal_move(self, from_square, to_square):
        """
        Returns True if legal move and False if illegal move
        Only considers space itself and move style (any distance orthogonal)
        """
        # list of files to associate index values
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

        if ((self._color == "red" or self._color == "black") or
                (file.index(to_square[0]) - file.index(from_square[0]) == 0) or
                (int(to_square[1:]) - int(from_square[1:]) == 0)):
            return True
        return False


class Cannon:
    """
    Represents a Cannon with data members: color, rank, and file.
    Each player has two cannons, which start on the row behind the soldiers, two points in front of the horses.
    Cannons move like chariots, any distance orthogonally without jumping,
    but can only capture by jumping a single piece, friend or foe, along the path of attack.
    The piece over which the cannon jumps is called the "cannon platform" or "screen".
    Any number of unoccupied spaces, including none, may exist between the cannon, screen, and
    the piece to be captured. Cannons can be exchanged for horses immediately from their starting positions.
    """

    def __init__(self, color):
        self._color = color

    def get_color(self):
        """
        Returns piece color
        """
        return self._color

    def get_legal_move(self, from_square, to_square):
        """
        Returns True if legal move and False if illegal move
        Only considers space itself and move style (any distance orthogonal)
        """
        # list of files to associate index values
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

        if ((self._color == "red" or self._color == "black") or
                file.index(to_square[0]) - file.index(from_square[0] == 0) or
                int(to_square[1:]) - int(from_square[1:]) == 0):
            return True
        return False


class Soldier:
    """
    Represents a Soldier with data members: color, rank, and file.
    Each side starts with five soldiers. Soldiers begin the game located on every other point one row back
    from the edge of the river. They move and capture by advancing one point. Once they have crossed the river,
    they may also move and capture one point horizontally. Soldiers cannot move backward, and
    therefore cannot retreat; after advancing to the last rank of the board, however,
    a soldier may still move sideways at the enemy's edge.
    The soldier is sometimes called the "pawn" by English-speaking players, due to the pieces' similarities.
    """

    def __init__(self, color):
        self._color = color

    def get_color(self):
        """
        Returns piece color
        """
        return self._color

    def get_legal_move(self, from_square, to_square):
        """
        Returns True if legal move and False if illegal move
        Only considers space itself and move style
        (one space forward until the river is crossed, then one space forward or horizontal)
        """
        # list of files to associate index values
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

        if self._color == "red" and \
                file.index(from_square[0]) < file.index(to_square[0]) and \
                ((file.index(to_square[0]) + 1 == file.index(from_square[0]) or
                  (file.index(to_square[0]) - 1 == file.index(from_square[0])) and
                  int(to_square[1:]) - int(from_square[1:]) == 0)) or \
                (file.index(from_square[0]) > 4 and file.index(to_square[0]) - file.index(from_square[0]) == 0 and
                 (int(to_square[1:]) + 1 == int(from_square[1:]) or int(to_square[1:]) - 1 == int(from_square[1:]))):
            return True

        if self._color == "black" and \
                file.index(from_square[0]) > file.index(to_square[0]) and \
                ((file.index(to_square[0]) + 1 == file.index(from_square[0]) or
                  (file.index(to_square[0]) - 1 == file.index(from_square[0])) and
                  int(to_square[1:]) - int(from_square[1:]) == 0)) or \
                (file.index(from_square[0]) < 5 and file.index(to_square[0]) - file.index(from_square[0]) == 0 and
                 (int(to_square[1:]) + 1 == int(from_square[1:]) or int(to_square[1:]) - 1 == int(from_square[1:]))):
            return True
        return False
