# Author: Jillian Crowley
# Date: 03/12/2020
# Description: From Wikipedia:
# The Xiangqi game (Chinese chess) represents a battle between two 16-piece armies, with
# the object of the game being to capture the enemy's general (king).
# Notable features this game include the cannon, which must jump to capture;
# a rule prohibiting the generals from facing each other directly;
# areas on the board called the river and palace, which
# restrict the movement of some pieces (but enhance that of others);
# and placement of the pieces on the intersections of the board lines, rather
# than within the squares.
# Writes classes XiangqiGame, General, Advisor, Elephant, Horse, Chariot, Cannon, Soldier and
# methods within these classes to play Xiangqi


class XiangqiGame:
    """
    Represents a XiangqiGame with _the_board, _game_state, _player_turn, _red_general_location,
    _red_in_check, _black_general_location, and _black_in_check data members.
    """

    def __init__(self):
        """
        Returns a XiangqiGame object with initialized _the_board, _game_state, _player_turn, _red_general_location,
        _red_in_check, _black_general_location, and _black_in_check
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
             [Soldier("black"), "", Soldier("black"), "", Soldier("black"),
              "", Soldier("black"), "", Soldier("black"), "7"],
             ["", Cannon("black"), "", "", "", "", "", Cannon("black"), "", "8"],
             ["", "", "", "", "", "", "", "", "", "9"],
             [Chariot("black"), Horse("black"), Elephant("black"),
              Advisor("black"), General("black"), Advisor("black"),
              Elephant("black"), Horse("black"), Chariot("black"), "10"],
             ["a", "b", "c", "d", "e", "f", "g", "h", "i"]]

        # initializes _game_state
        self._game_state = "UNFINISHED"

        # initializes _player_turn
        self._player_turn = "red"

        # initializes _red_general_location and _red_in_check
        self._red_general_location = "e1"
        self._red_in_check = False

        # initializes _black_general_location and _black_in_check
        self._black_general_location = "e10"
        self._black_in_check = False

    def get_the_board(self):
        """
        Returns _the_board.
        """
        return self._the_board

    def print_the_board(self):
        """
        Returns printed _the_board with a newline for each rank.
        """
        return print("\n".join(str(rank) for rank in self._the_board))

    def get_game_state(self):
        """
        Returns the _game_state; either 'UNFINISHED', 'RED_WON' or 'BLACK_WON'.
        """
        return self._game_state

    def get_player_turn(self):
        """
        Returns _player_turn; either "red" or "black"
        """
        return self._player_turn

    def is_in_check(self, player):
        """
        Takes as a parameter either 'red' or 'black' and
        returns True if that player is in check, but returns False otherwise
        """
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

        # define board indices if player is red
        player_general_row = int(self._red_general_location[1:]) - 1
        player_general_column = file.index(self._red_general_location[0])
        other_player = "black"
        if player == "red":
            self._red_in_check = False

        # define board indices if player is black
        if player == "black":
            player_general_row = int(self._black_general_location[1:]) - 1
            player_general_column = file.index(self._black_general_location[0])
            other_player = "red"
            self._black_in_check = False

        # see if player's General is in check by other player's Horse
        if player_general_row - 2 >= 0 and player_general_column - 1 >= 0:
            if (isinstance(self._the_board[player_general_row - 2][player_general_column - 1], Horse) and
                    self._the_board[player_general_row - 2][player_general_column - 1].get_color() == other_player):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True

        if player_general_row - 2 >= 0 and player_general_column + 1 <= 8:
            if (isinstance(self._the_board[player_general_row - 2][player_general_column + 1], Horse) and
                    self._the_board[player_general_row - 2][player_general_column + 1].get_color() == other_player):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True

        if player_general_row - 1 >= 0 and player_general_column + 2 <= 8:
            if (isinstance(self._the_board[player_general_row - 1][player_general_column + 2], Horse) and
                    self._the_board[player_general_row - 1][player_general_column + 2].get_color() == other_player):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True

        if player_general_row + 1 <= 9 and player_general_column + 2 <= 8:
            if (isinstance(self._the_board[player_general_row + 1][player_general_column + 2], Horse) and
                    self._the_board[player_general_row + 1][player_general_column + 2].get_color() == other_player):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True

        if player_general_row + 2 <= 9 and player_general_column + 1 <= 8:
            if (isinstance(self._the_board[player_general_row + 2][player_general_column + 1], Horse) and
                    self._the_board[player_general_row + 2][player_general_column + 1].get_color() == other_player):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True

        if player_general_row + 2 <= 9 and player_general_column - 1 >= 0:
            if (isinstance(self._the_board[player_general_row + 2][player_general_column - 1], Horse) and
                    self._the_board[player_general_row + 2][player_general_column - 1].get_color() == other_player):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True

        if player_general_row + 1 <= 9 and player_general_column - 2 >= 0:
            if (isinstance(self._the_board[player_general_row + 1][player_general_column - 2], Horse) and
                    self._the_board[player_general_row + 1][player_general_column - 2].get_color() == other_player):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True

        if player_general_row - 1 >= 0 and player_general_column - 2 >= 0:
            if (isinstance(self._the_board[player_general_row - 1][player_general_column - 2], Horse) and
                    self._the_board[player_general_row - 1][player_general_column - 2].get_color() == other_player):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True

        # see if player's General is in check by other player's Chariot
        i = 1
        while player_general_row + i <= 9:
            if ((isinstance(self._the_board[player_general_row + i][player_general_column], Chariot) and
                 self._the_board[player_general_row + i][player_general_column].get_color() == other_player)):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True
            if self._the_board[player_general_row + i][player_general_column] == "":
                i += 1
            else:
                break

        i = 1
        while player_general_row - i >= 0:
            if ((isinstance(self._the_board[player_general_row - i][player_general_column], Chariot) and
                 self._the_board[player_general_row - i][player_general_column].get_color() == other_player)):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True
            if self._the_board[player_general_row - i][player_general_column] == "":
                i += 1
            else:
                break

        i = 1
        while player_general_column + i <= 8:
            if ((isinstance(self._the_board[player_general_row][player_general_column + i], Chariot) and
                 self._the_board[player_general_row][player_general_column + i].get_color() == other_player)):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True
            if self._the_board[player_general_row][player_general_column + i] == "":
                i += 1
            else:
                break

        i = 1
        while player_general_column - i >= 0:
            if ((isinstance(self._the_board[player_general_row][player_general_column - i], Chariot) and
                 self._the_board[player_general_row][player_general_column - i].get_color() == other_player)):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True
            if self._the_board[player_general_row][player_general_column - i] == "":
                i += 1
            else:
                break

        # see if player's General is in check by other player's Cannon
        i = 1
        count_i = 0
        count_j = 0

        while player_general_row + i <= 9:
            if ((isinstance(self._the_board[player_general_row + i][player_general_column], Cannon) and
                 self._the_board[player_general_row + i][player_general_column].get_color() == other_player)):
                break
            i += 1

        if player_general_row + i < 9:
            j = i + 1
            while player_general_row + j <= 9:
                if ((isinstance(self._the_board[player_general_row + j][player_general_column], Cannon) and
                     self._the_board[player_general_row + j][player_general_column].get_color() == other_player)):
                    break
                j += 1

            if (isinstance(self._the_board[player_general_row + j][player_general_column], Cannon) and
                    self._the_board[player_general_row + j][player_general_column].get_color() == other_player):
                j -= 1
                while player_general_row + j > player_general_row:
                    if self._the_board[player_general_row + j][player_general_column] != "":
                        count_j += 1
                    j -= 1

        if (isinstance(self._the_board[player_general_row + i][player_general_column], Cannon) and
                self._the_board[player_general_row + i][player_general_column].get_color() == other_player):
            i -= 1
            while player_general_row + i > player_general_row:
                if self._the_board[player_general_row + i][player_general_column] != "":
                    count_i += 1
                i -= 1

        if count_i == 1 or count_j == 1:
            if player == "red":
                self._red_in_check = True
            if player == "black":
                self._black_in_check = True

        i = 1
        count_i = 0
        count_j = 0
        while player_general_row - i >= 0:
            if ((isinstance(self._the_board[player_general_row - i][player_general_column], Cannon) and
                 self._the_board[player_general_row - i][player_general_column].get_color() == other_player)):
                break
            i += 1

        if player_general_row - i > 0:
            j = i + 1
            while player_general_row - j >= 0:
                if ((isinstance(self._the_board[player_general_row - j][player_general_column], Cannon) and
                     self._the_board[player_general_row - j][player_general_column].get_color() == other_player)):
                    break
                j += 1

            if (isinstance(self._the_board[player_general_row - j][player_general_column], Cannon) and
                    self._the_board[player_general_row - j][player_general_column].get_color() == other_player):
                j -= 1
                while player_general_row - j < player_general_row:
                    if self._the_board[player_general_row - j][player_general_column] != "":
                        count_j += 1
                    j -= 1

        if (isinstance(self._the_board[player_general_row - i][player_general_column], Cannon) and
                self._the_board[player_general_row - i][player_general_column].get_color() == other_player):
            i -= 1
            while player_general_row - i < player_general_row:
                if self._the_board[player_general_row - i][player_general_column] != "":
                    count_i += 1
                i -= 1

        if count_i == 1 or count_j == 1:
            if player == "red":
                self._red_in_check = True
            if player == "black":
                self._black_in_check = True

        i = 1
        count_i = 0
        count_j = 0
        while player_general_column + i <= 8:
            if ((isinstance(self._the_board[player_general_row][player_general_column + i], Cannon) and
                 self._the_board[player_general_row][player_general_column + i].get_color() == other_player)):
                break
            i += 1

        if player_general_column + i < 8:
            j = i + 1
            while player_general_column + j <= 8:
                if ((isinstance(self._the_board[player_general_row][player_general_column + j], Cannon) and
                     self._the_board[player_general_row][player_general_column + j].get_color() == other_player)):
                    break
                j += 1

            if (isinstance(self._the_board[player_general_row][player_general_column + j], Cannon) and
                    self._the_board[player_general_row][player_general_column + j].get_color() == other_player):
                j -= 1
                while player_general_column + j > player_general_column:
                    if self._the_board[player_general_row][player_general_column + j] != "":
                        count_j += 1
                    j -= 1

        if (isinstance(self._the_board[player_general_row][player_general_column + i], Cannon) and
                self._the_board[player_general_row][player_general_column + i].get_color() == other_player):
            i -= 1
            while player_general_column + i > player_general_column:
                if self._the_board[player_general_row][player_general_column + i] != "":
                    count_i += 1
                i -= 1

        if count_i == 1 or count_j == 1:
            if player == "red":
                self._red_in_check = True
            if player == "black":
                self._black_in_check = True

        i = 1
        count_i = 0
        count_j = 0
        while player_general_column - i >= 0:
            if ((isinstance(self._the_board[player_general_row][player_general_column - i], Cannon) and
                 self._the_board[player_general_row][player_general_column - i].get_color() == other_player)):
                break
            i += 1

        if player_general_column - i > 0:
            j = i + 1
            while player_general_column - j >= 0:
                if ((isinstance(self._the_board[player_general_row][player_general_column - j], Cannon) and
                     self._the_board[player_general_row][player_general_column - j].get_color() == other_player)):
                    break
                j += 1

            if (isinstance(self._the_board[player_general_row][player_general_column - j], Cannon) and
                    self._the_board[player_general_row][player_general_column - j].get_color() == other_player):
                j -= 1
                while player_general_column - j < player_general_column:
                    if self._the_board[player_general_row][player_general_column - j] != "":
                        count_j += 1
                    j -= 1

        if (isinstance(self._the_board[player_general_row][player_general_column - i], Cannon) and
                self._the_board[player_general_row][player_general_column - i].get_color() == other_player):
            i -= 1
            while player_general_column - i < player_general_column:
                if self._the_board[player_general_row][player_general_column - i] != "":
                    count_i += 1
                i -= 1

        if count_i == 1 or count_j == 1:
            if player == "red":
                self._red_in_check = True
            if player == "black":
                self._black_in_check = True

        # see if player's General is in check by other player's Soldier
        if player_general_row - 1 >= 0 and player == "black":
            if (isinstance(self._the_board[player_general_row - 1][player_general_column], Soldier) and
                    self._the_board[player_general_row - 1][player_general_column].get_color() == other_player):
                self._black_in_check = True

        if player_general_row + 1 <= 9 and player == "red":
            if (isinstance(self._the_board[player_general_row + 1][player_general_column], Soldier) and
                    self._the_board[player_general_row + 1][player_general_column].get_color() == other_player):
                self._red_in_check = True

        if player_general_column - 1 >= 0:
            if (isinstance(self._the_board[player_general_row][player_general_column - 1], Soldier) and
                    self._the_board[player_general_row][player_general_column - 1].get_color() == other_player):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True

        if player_general_column + 1 <= 8:
            if (isinstance(self._the_board[player_general_row][player_general_column + 1], Soldier) and
                    self._the_board[player_general_row][player_general_column + 1].get_color() == other_player):
                if player == "red":
                    self._red_in_check = True
                if player == "black":
                    self._black_in_check = True

        if player == "red":
            return self._red_in_check

        if player == "black":
            return self._black_in_check

    def make_move(self, from_square, to_square):
        """
        Takes two parameters - strings that represent the square moved from and
        the square moved to. For example, make_move('b3', 'b10').
        Checks for illegal/invalid moves, but otherwise makes the indicated move, removes any captured piece,
        updates the game state if necessary, updates whose turn it is, and returns True

        If the general's player can make no move to prevent the general's capture, the situation is called "checkmate"
        and the other player wins. If a player has no legal/valid moves, the other player wins by stalemate.
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        # move cannot be made if no piece exists at from_square
        if self._the_board[from_row][from_column] == "":
            return False

        # move cannot be made if player's piece exists at to_square
        if self._the_board[to_row][to_column] != "":
            if self._the_board[to_row][to_column].get_color() == self._player_turn:
                return False

        # move cannot be made if: not player's turn, move is not legally available for piece based on class definition,
        # or game state is finished; either "RED_WON" or "BLACK_WON"
        if self._the_board[from_row][from_column].get_color() != self._player_turn or \
                self._the_board[from_row][from_column].is_legal_move(from_square, to_square) is False or \
                self._game_state != "UNFINISHED":
            return False

        # move cannot be made if it is not valid in relation to other pieces on the board:
        # if piece trying to move is a General
        if isinstance(self._the_board[from_row][from_column], General):
            if self.is_valid_move_general(from_square, to_square) is False:
                return False

            # if red or black General moved, update location
            if self._the_board[from_row][from_column].get_color() == "red":
                self._red_general_location = to_square
            if self._the_board[from_row][from_column].get_color() == "black":
                self._black_general_location = to_square

        # if piece trying to move is an Elephant
        if isinstance(self._the_board[from_row][from_column], Elephant):
            if self.is_valid_move_elephant(from_square, to_square) is False:
                return False

        # if piece trying to move is a Horse
        if isinstance(self._the_board[from_row][from_column], Horse):
            if self.is_valid_move_horse(from_square, to_square) is False:
                return False

        # if piece trying to move is a Chariot
        if isinstance(self._the_board[from_row][from_column], Chariot):
            if self.is_valid_move_chariot(from_square, to_square) is False:
                return False

        # if piece trying to move is a Cannon
        if isinstance(self._the_board[from_row][from_column], Cannon):
            if self.is_valid_move_cannon(from_square, to_square) is False:
                return False

        # otherwise, make move and remove any captured piece
        temp = self._the_board[to_row][to_column]
        self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
        self._the_board[from_row][from_column] = ""

        # if it is player's turn and player is in check, undo move and return False
        # since player cannot put its own General in check
        if self.is_in_check(self._player_turn):
            self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
            self._the_board[to_row][to_column] = temp

            # if red or black General move is being undone, revert location
            if self._the_board[from_row][from_column].get_color() == "red":
                self._red_general_location = from_square
            if self._the_board[from_row][from_column].get_color() == "black":
                self._black_general_location = from_square
            return False

        # if red General is in checkmate or red player is in stalemate, update _game_state to "BLACK_WON"
        from_spaces = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1",
                       "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2",
                       "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3",
                       "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4",
                       "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "i5",
                       "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "i6",
                       "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "i7",
                       "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "i8",
                       "a9", "b9", "c9", "d9", "e9", "f9", "g9", "h9", "i9",
                       "a10", "b10", "c10", "d10", "e10", "f10", "g10", "h10", "i10"]
        to_spaces = from_spaces
        count = 0

        for i in from_spaces:
            if count > 0:
                break

            for j in to_spaces:
                # define board indices
                file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
                from_row = int(i[1:]) - 1
                from_column = file.index(i[0])
                to_row = int(j[1:]) - 1
                to_column = file.index(j[0])

                # piece must exist at from_square
                if self._the_board[from_row][from_column] != "":

                    # player's piece cannot exist at to_square
                    if ((self._the_board[to_row][to_column] == "") or
                            (self._the_board[to_row][to_column] != "" and
                             self._the_board[to_row][to_column].get_color() != "red")):

                        # must be player's piece at from_square, move must be legal
                        if self._the_board[from_row][from_column].get_color() == "red" and \
                                self._the_board[from_row][from_column].is_legal_move(i, j):

                            # if piece considered is a General
                            if (isinstance(self._the_board[from_row][from_column], General) and
                                    self._the_board[from_row][from_column].get_color() == "red" and
                                    self.is_valid_move_general(i, j) is True):

                                # make move temporarily to see if it puts player in check; update General location
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""
                                self._red_general_location = j

                                # if there is a legal/valid move here, add one to counter
                                if self.is_in_check("red") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                                # if General move is being undone, revert location
                                self._red_general_location = i

                            # if piece considered is an Advisor
                            if (isinstance(self._the_board[from_row][from_column], Advisor) and
                                    self._the_board[from_row][from_column].get_color() == "red"):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if there is a legal/valid move here, add one to counter
                                if self.is_in_check("red") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                            # if piece considered is an Elephant
                            if (isinstance(self._the_board[from_row][from_column], Elephant) and
                                    self._the_board[from_row][from_column].get_color() == "red" and
                                    self.is_valid_move_elephant(i, j) is True):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if there is a legal/valid move here, add one to counter
                                if self.is_in_check("red") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                            # if piece considered is a Horse
                            if (isinstance(self._the_board[from_row][from_column], Horse) and
                                    self._the_board[from_row][from_column].get_color() == "red" and
                                    self.is_valid_move_horse(i, j) is True):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if there is a legal/valid move here, add one to counter
                                if self.is_in_check("red") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                            # if piece considered is a Chariot
                            if (isinstance(self._the_board[from_row][from_column], Chariot) and
                                    self._the_board[from_row][from_column].get_color() == "red" and
                                    self.is_valid_move_chariot(i, j) is True):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if there is a legal/valid move here, add one to counter
                                if self.is_in_check("red") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                            # if piece considered is a Cannon
                            if (isinstance(self._the_board[from_row][from_column], Cannon) and
                                    self._the_board[from_row][from_column].get_color() == "red" and
                                    self.is_valid_move_cannon(i, j) is True):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if there is a legal/valid move here, add one to counter
                                if self.is_in_check("red") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                            # if piece considered is a Soldier
                            if (isinstance(self._the_board[from_row][from_column], Soldier) and
                                    self._the_board[from_row][from_column].get_color() == "red"):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if there is a legal/valid move here, add one to counter
                                if self.is_in_check("red") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

        # if red has no legal moves, black wins
        if count == 0:
            self._game_state = "BLACK_WON"

        # if black General is in checkmate or black player is in stalemate, update _game_state to "RED_WON"
        count = 0

        for i in from_spaces:
            if count > 0:
                break

            for j in to_spaces:
                # define board indices
                file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
                from_row = int(i[1:]) - 1
                from_column = file.index(i[0])
                to_row = int(j[1:]) - 1
                to_column = file.index(j[0])

                # piece must exist at from_square
                if self._the_board[from_row][from_column] != "":

                    # player's piece cannot exist at to_square
                    if ((self._the_board[to_row][to_column] == "") or
                            (self._the_board[to_row][to_column] != "" and
                             self._the_board[to_row][to_column].get_color() != "black")):

                        # must be player's piece at from_square, move must be legal
                        if self._the_board[from_row][from_column].get_color() == "black" and \
                                self._the_board[from_row][from_column].is_legal_move(i, j):

                            # if piece considered is a General
                            if (isinstance(self._the_board[from_row][from_column], General) and
                                    self._the_board[from_row][from_column].get_color() == "black" and
                                    self.is_valid_move_general(i, j) is True):

                                # make move temporarily to see if it puts player in check; update General location
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""
                                self._black_general_location = j

                                # if if there is a legal/valid move here, add one to counter
                                if self.is_in_check("black") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                                # if General move is being undone, revert location
                                self._black_general_location = i

                            # if piece considered is an Advisor
                            if (isinstance(self._the_board[from_row][from_column], Advisor) and
                                    self._the_board[from_row][from_column].get_color() == "black"):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if if there is a legal/valid move here, add one to counter
                                if self.is_in_check("black") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                            # if piece considered is an Elephant
                            if (isinstance(self._the_board[from_row][from_column], Elephant) and
                                    self._the_board[from_row][from_column].get_color() == "black" and
                                    self.is_valid_move_elephant(i, j) is True):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if if there is a legal/valid move here, add one to counter
                                if self.is_in_check("black") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                            # if piece considered is a Horse
                            if (isinstance(self._the_board[from_row][from_column], Horse) and
                                    self._the_board[from_row][from_column].get_color() == "black" and
                                    self.is_valid_move_horse(i, j) is True):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if if there is a legal/valid move here, add one to counter
                                if self.is_in_check("black") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                            # if piece considered is a Chariot
                            if (isinstance(self._the_board[from_row][from_column], Chariot) and
                                    self._the_board[from_row][from_column].get_color() == "black" and
                                    self.is_valid_move_chariot(i, j) is True):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if if there is a legal/valid move here, add one to counter
                                if self.is_in_check("black") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                            # if piece considered is a Cannon
                            if (isinstance(self._the_board[from_row][from_column], Cannon) and
                                    self._the_board[from_row][from_column].get_color() == "black" and
                                    self.is_valid_move_cannon(i, j) is True):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if if there is a legal/valid move here, add one to counter
                                if self.is_in_check("black") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

                            # if piece considered is a Soldier
                            if (isinstance(self._the_board[from_row][from_column], Soldier) and
                                    self._the_board[from_row][from_column].get_color() == "black"):

                                # make move temporarily to see if it puts player in check
                                temp = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = self._the_board[from_row][from_column]
                                self._the_board[from_row][from_column] = ""

                                # if if there is a legal/valid move here, add one to counter
                                if self.is_in_check("black") is False:
                                    count += 1

                                # Undo move
                                self._the_board[from_row][from_column] = self._the_board[to_row][to_column]
                                self._the_board[to_row][to_column] = temp

        # if black has no legal moves, red wins
        if count == 0:
            self._game_state = "RED_WON"

        # update _player_turn
        if self._player_turn == "red":
            self._player_turn = "black"
            return True

        # update _player_turn
        if self._player_turn == "black":
            self._player_turn = "red"
            return True

    def is_valid_move_general(self, from_square, to_square):
        """
        Returns True if valid move and False if invalid move
        Considers move within the context of current board
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        # return False when Generals cannot face each other along the same file with no intervening pieces
        if self._the_board[from_row][from_column].get_color() == "red":
            if isinstance(self._the_board[9][to_column], General):
                rank = 9
                while to_row < rank:
                    if self._the_board[rank - 1][to_column] != "":
                        return True
                    rank -= 1
                return False

            if isinstance(self._the_board[8][to_column], General):
                rank = 8
                while to_row < rank:
                    if self._the_board[rank - 1][to_column] != "":
                        return True
                    rank -= 1
                return False

            if isinstance(self._the_board[7][to_column], General):
                rank = 7
                while to_row < rank:
                    if self._the_board[rank - 1][to_column] != "":
                        return True
                    rank -= 1
                return False
            return True

        if self._the_board[from_row][from_column].get_color() == "black":
            if isinstance(self._the_board[0][to_column], General):
                rank = 0
                while to_row > rank:
                    if self._the_board[rank + 1][to_column] != "":
                        return True
                    rank += 1
                return False

            if isinstance(self._the_board[1][to_column], General):
                rank = 1
                while to_row > rank:
                    if self._the_board[rank + 1][to_column] != "":
                        return True
                    rank += 1
                return False

            if isinstance(self._the_board[2][to_column], General):
                rank = 2
                while to_row > rank:
                    if self._the_board[rank + 1][to_column] != "":
                        return True
                    rank += 1
                return False
            return True

    def is_valid_move_elephant(self, from_square, to_square):
        """
        Returns True if valid move and False if invalid move
        Considers move within the context of current board
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        # Elephants cannot jump so return False if there is a piece blocking its first diagonal move
        if to_row == from_row + 2 and to_column == from_column + 2:
            if self._the_board[from_row + 1][from_column + 1] != "":
                return False

        if to_row == from_row - 2 and to_column == from_column - 2:
            if self._the_board[from_row - 1][from_column - 1] != "":
                return False

        if to_row == from_row + 2 and to_column == from_column - 2:
            if self._the_board[from_row + 1][from_column - 1] != "":
                return False

        if to_row == from_row - 2 and to_column == from_column + 2:
            if self._the_board[from_row - 1][from_column + 1] != "":
                return False
        return True

    def is_valid_move_horse(self, from_square, to_square):
        """
        Returns True if valid move and False if invalid move
        Considers move within the context of current board
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        # Horses cannot jump so return False if there is a piece blocking its first orthogonal move
        if ((to_row == from_row - 2 and to_column == from_column - 1) or
                (to_row == from_row - 2 and to_column == from_column + 1)):
            if self._the_board[from_row - 1][from_column] != "":
                return False

        if ((to_row == from_row - 1 and to_column == from_column + 2) or
                (to_row == from_row + 1 and to_column == from_column + 2)):
            if self._the_board[from_row][from_column + 1] != "":
                return False

        if ((to_row == from_row + 2 and to_column == from_column + 1) or
                (to_row == from_row + 2 and to_column == from_column - 1)):
            if self._the_board[from_row + 1][from_column] != "":
                return False

        if ((to_row == from_row + 1 and to_column == from_column - 2) or
                (to_row == from_row - 1 and to_column == from_column - 2)):
            if self._the_board[from_row][from_column - 1] != "":
                return False
        return True

    def is_valid_move_chariot(self, from_square, to_square):
        """
        Returns True if valid move and False if invalid move
        Considers move within the context of current board
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        # Chariots cannot jump so return False if there is a piece in its orthogonal path
        i = 1
        while from_row + i < to_row:
            if from_column == to_column and self._the_board[from_row + i][from_column] != "":
                return False
            i += 1

        i = 1
        while from_row - i > to_row:
            if from_column == to_column and self._the_board[from_row - i][from_column] != "":
                return False
            i += 1

        i = 1
        while from_column + i < to_column:
            if from_row == to_row and self._the_board[from_row][from_column + i] != "":
                return False
            i += 1

        i = 1
        while from_column - i > to_column:
            if from_row == to_row and self._the_board[from_row][from_column - i] != "":
                return False
            i += 1
        return True

    def is_valid_move_cannon(self, from_square, to_square):
        """
        Returns True if valid move and False if invalid move
        Only considers move within the context of current board
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        # Cannons can move any distance orthogonally without jumping
        # if there is only ONE piece in the path between square_from and square_to, then
        # Cannons can capture and return True

        i = 1
        count = 0
        while from_row + i < to_row:
            if from_column == to_column and self._the_board[from_row + i][from_column] != "":
                count += 1
            i += 1

        i = 1
        while from_row - i > to_row:
            if from_column == to_column and self._the_board[from_row - i][from_column] != "":
                count += 1
            i += 1

        i = 1
        while from_column + i < to_column:
            if from_row == to_row and self._the_board[from_row][from_column + i] != "":
                count += 1
            i += 1

        i = 1
        while from_column - i > to_column:
            if from_row == to_row and self._the_board[from_row][from_column - i] != "":
                count += 1
            i += 1

        if (count > 1 or (count == 0 and self._the_board[to_row][to_column] != "") or
                (count == 1 and self._the_board[to_row][to_column] == "")):
            return False
        return True


class General:
    """
    Represents a General with data member _color
    The general starts the game at the midpoint of the back edge, within the palace.
    The general may move and capture one point orthogonally and may not leave the palace.
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
        Considers spaces themselves and move style (one space orthogonally and cannot leave palace)
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        if (self._color == "red" and from_row < 3 and to_row < 3 and 6 > from_column > 2 and 6 > to_column > 2 and
                ((from_row + 1 == to_row or from_row - 1 == to_row) and from_column == to_column) or
                ((from_column + 1 == to_column or from_column - 1 == to_column) and from_row == to_row)):
            return True

        if (self._color == "black" and from_row > 6 and to_row < 6 and 6 > from_column > 2 and 6 > to_column > 2 and
                ((from_row + 1 == to_row or from_row - 1 == to_row) and from_column == to_column) or
                ((from_column + 1 == to_column or from_column - 1 == to_column) and from_row == to_row)):
            return True
        return False


class Advisor:
    """
    Represents an Advisor with data member _color
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
        Considers spaces themselves and move style (one space diagonally and cannot leave palace)
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        if self._color == "red" and from_row < 3 and 6 > from_column > 2 and 6 > to_column > 2 and \
                (((from_row + 1 == to_row) and (from_column + 1 == to_column)) or
                 ((from_row - 1 == to_row) and (from_column - 1 == to_column)) or
                 ((from_row + 1 == to_row) and (from_column - 1 == to_column)) or
                 ((from_row - 1 == to_row) and (from_column + 1 == to_column))):
            return True

        if self._color == "black" and from_row > 6 and 6 > from_column > 2 and 6 > to_column > 2 and \
                (((from_row + 1 == to_row) and (from_column + 1 == to_column)) or
                 ((from_row - 1 == to_row) and (from_column - 1 == to_column)) or
                 ((from_row + 1 == to_row) and (from_column - 1 == to_column)) or
                 ((from_row - 1 == to_row) and (from_column + 1 == to_column))):
            return True
        return False


class Elephant:
    """
    Represents an Elephant with data member _color
    These pieces move and capture exactly two points diagonally and may not jump over intervening pieces;
    If an elephant cannot move due to a diagonally adjacent piece, it is known as "blocking the elephant's eye"
    Elephants may not cross the river, and serve as defensive pieces. An elephant's movement is
    restricted to just seven board positions.
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
        Considers space themselves and move style (two spaces diagonally and cannot cross river)
        """
        # list of files to associate index values
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

        # define board indices
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        # Elephants cannot cross the river
        if self._color == "red" and \
                (((from_row == 0 and from_column == 2) or (from_row == 0 and from_column == 6) or
                  (from_row == 2 and from_column == 0) or (from_row == 2 and from_column == 4) or
                  (from_row == 2 and from_column == 8) or (from_row == 4 and from_column == 2) or
                  (from_row == 4 and from_column == 6)) and
                 ((to_row == from_row + 2 and to_column == from_column + 2) or
                  (to_row == from_row - 2 and to_column == from_column - 2) or
                  (to_row == from_row + 2 and to_column == from_column - 2) or
                  (to_row == from_row - 2 and to_column == from_column + 2))):
            return True

        if self._color == "black" and \
                (((from_row == 9 and from_column == 2) or (from_row == 9 and from_column == 6) or
                  (from_row == 7 and from_column == 0) or (from_row == 7 and from_column == 4) or
                  (from_row == 7 and from_column == 9) or (from_row == 5 and from_column == 2) or
                  (from_row == 5 and from_column == 6)) and
                 ((to_row == from_row + 2 and to_column == from_column + 2) or
                  (to_row == from_row - 2 and to_column == from_column - 2) or
                  (to_row == from_row + 2 and to_column == from_column - 2) or
                  (to_row == from_row - 2 and to_column == from_column + 2))):
            return True
        return False


class Horse:
    """
    Represents a Horse with data member _color
    Horses begin the game next to the elephants, on their outside flanks.
    A horse moves and captures one point orthogonally and then one point diagonally away from
    its former position. The horse does not jump and can be blocked by a piece located one point
    horizontally or vertically adjacent to it. Blocking a horse is called "hobbling the horse's leg".
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
        Considers spaces themselves and move style (one space orthogonal and one space diagonal)
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        if ((self._color == "red" or self._color == "black") and
                ((from_row - 2 == to_row and from_column - 1 == to_column) or
                 (from_row - 2 == to_row and from_column + 1 == to_column) or
                 (from_row - 1 == to_row and from_column + 2 == to_column) or
                 (from_row + 1 == to_row and from_column + 2 == to_column) or
                 (from_row + 2 == to_row and from_column + 1 == to_column) or
                 (from_row + 2 == to_row and from_column - 1 == to_column) or
                 (from_row + 1 == to_row and from_column - 2 == to_column) or
                 (from_row - 1 == to_row and from_column - 2 == to_column))):
            return True
        return False


class Chariot:
    """
    Represents a Chariot with data member _color
    The chariot moves and captures any distance orthogonally, but may not jump over intervening pieces.
    The chariots begin the game on the points at the corners of the board.
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
        Considers space itself and move style (any distance orthogonal)
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        if ((self._color == "red" or self._color == "black") and
                ((to_row == from_row) or (to_column == from_column))):
            return True
        return False


class Cannon:
    """
    Represents a Cannon with data member _color.
    Each player has two cannons, which start on the row behind the soldiers, two points in front of the horses.
    Cannons move like chariots, any distance orthogonally without jumping,
    but can only capture by jumping a single piece, friend or foe, along the path of attack.
    The piece over which the cannon jumps is called the "cannon platform" or "screen".
    Any number of unoccupied spaces, including none, may exist between the cannon, screen, and
    the piece to be captured.
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
        Considers space itself and move style (any distance orthogonal)
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        if ((self._color == "red" or self._color == "black") and
                ((to_row == from_row) or (to_column == from_column))):
            return True
        return False


class Soldier:
    """
    Represents a Soldier with data member _color
    Each side starts with five soldiers. Soldiers begin the game located on every other point one row back
    from the edge of the river. They move and capture by advancing one point. Once they have crossed the river,
    they may also move and capture one point horizontally. Soldiers cannot move backward.
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
        Considers space itself and move style
        (one space forward until the river is crossed, then one space forward or horizontal)
        """
        # define board indices
        file = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        from_row = int(from_square[1:]) - 1
        from_column = file.index(from_square[0])
        to_row = int(to_square[1:]) - 1
        to_column = file.index(to_square[0])

        if self._color == "red":
            if from_row + 1 == to_row and to_column == from_column:
                return True
            if from_row > 4:
                if ((from_column + 1 == to_column and to_row == from_row) or
                        (from_column - 1 == to_column and to_row == from_row)):
                    return True

        if self._color == "black":
            if from_row - 1 == to_row and to_column == from_column:
                return True
            if from_row < 5:
                if ((from_column + 1 == to_column and to_row == from_row) or
                        (from_column - 1 == to_column and to_row == from_row)):
                    return True
        return False


def main():
    # tests example from readme
    game = XiangqiGame()
    move_result = game.make_move('c1', 'e3')
    black_in_check = game.is_in_check('black')
    game.make_move('e7', 'e6')
    state = game.get_game_state()
    results = (move_result, black_in_check, state)

    return results


if __name__ == '__main__':
    main()
