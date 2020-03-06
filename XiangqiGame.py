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

        # initializes red General's rank and file
        self._red_general_rank = 0
        self._red_general_file = 4

        # initializes black General's rank and file
        self._black_general_rank = 9
        self._black_general_file = 4

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
        # pseudocode written here until code is written for ways the Generals can
        # be threatened by pieces of the opposite color

        # if player == "red" and \
        #         ((isinstance(self._the_board[0][3], General) and General is threatened by a black piece) or
        #         (isinstance(self._the_board[0][4], General) and General is threatened by a black piece) or
        #         (isinstance(self._the_board[0][5], General) and General is threatened by a black piece) or
        #         (isinstance(self._the_board[1][3], General) and General is threatened by a black piece) or
        #         (isinstance(self._the_board[1][4], General) and General is threatened by a black piece) or
        #         (isinstance(self._the_board[1][5], General) and General is threatened by a black piece) or
        #         (isinstance(self._the_board[2][3], General) and General is threatened by a black piece) or
        #         (isinstance(self._the_board[2][4], General) and General is threatened by a black piece) or
        #         (isinstance(self._the_board[2][5], General) and General is threatened by a black piece)):
        #     return True
        #
        # elif player == "black" and \
        #         ((isinstance(self._the_board[0][3], General) and General is threatened by a red piece) or
        #         (isinstance(self._the_board[0][4], General) and General is threatened by a red piece) or
        #         (isinstance(self._the_board[0][5], General) and General is threatened by a red piece) or
        #         (isinstance(self._the_board[1][3], General) and General is threatened by a red piece) or
        #         (isinstance(self._the_board[1][4], General) and General is threatened by a red piece) or
        #         (isinstance(self._the_board[1][5], General) and General is threatened by a red piece) or
        #         (isinstance(self._the_board[2][3], General) and General is threatened by a red piece) or
        #         (isinstance(self._the_board[2][4], General) and General is threatened by a red piece) or
        #         (isinstance(self._the_board[2][5], General) and General is threatened by a red piece)):
        #     return True
        # return False

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

        # return False where move cannot be made if no piece exists at from_square:
        if self._the_board[file.index(from_square[0])][from_square[1:]] == "":
            return False

        # return False where move cannot be made if:
        # not player's turn
        # move is not legally available for piece based on class definition
        # game state is finished; either RED_WON or BLACK_WON
        if self._the_board[file.index(from_square[0])][from_square[1:]].get_color() != self._player_turn or \
                self._the_board[file.index(from_square[0])][from_square[1:]]. \
                        get_legal_move(from_square, to_square) or self._game_state != "UNFINISHED":
            return False

        # check for illegal moves in relation to other pieces and return False
        # pseudocode is written below for Advisor, Elephant, Horse, Chariot, Cannon, and Soldier and
        # checkmate conditions for each player until I write code for their illegal moves

        # return False when red piece tries to move to a space occupied by a red piece
        if self._the_board[file.index(from_square[0])][from_square[1:]].get_color() == "red" and \
                self._the_board[file.index(to_square[0])][to_square[1:]].get_color() == "red":
            return False
        # return False when black piece tries to move to a space occupied by a black piece
        if self._the_board[file.index(from_square[0])][from_square[1:]].get_color() == "black" and \
                self._the_board[file.index(to_square[0])][to_square[1:]].get_color() == "black":
            return False

        # return False if illegal move by General
        # return False when Generals cannot face each other along the same file with no intervening pieces
        if isinstance(self._the_board[file.index(from_square[0])][from_square[1:]], General):
            if self._the_board[file.index(from_square[0])][from_square[1:]].get_color() == "red":
                if (isinstance(self._the_board[9][to_square[1:]], General) and
                        self._the_board[8][to_square[1:]] == "" and self._the_board[7][to_square[1:]] == "" and
                        self._the_board[6][to_square[1:]] == "" and self._the_board[5][to_square[1:]] == "" and
                        self._the_board[4][to_square[1:]] == "" and self._the_board[3][to_square[1:]] == "" and
                        self._the_board[2][to_square[1:]] == "" and self._the_board[1][to_square[1:]] == "" or
                        (isinstance(self._the_board[8][to_square[1:]], General) and
                         self._the_board[7][to_square[1:]] == "" and self._the_board[6][to_square[1:]] == "" and
                         self._the_board[5][to_square[1:]] == "" and self._the_board[4][to_square[1:]] == "" and
                         self._the_board[3][to_square[1:]] == "" and self._the_board[2][to_square[1:]] == "" and
                         self._the_board[1][to_square[1:]] == "") or
                        (isinstance(self._the_board[7][to_square[1:]], General) and
                         self._the_board[6][to_square[1:]] == "" and self._the_board[5][to_square[1:]] == "" and
                         self._the_board[4][to_square[1:]] == "" and self._the_board[3][to_square[1:]] == "" and
                         self._the_board[2][to_square[1:]] == "" and self._the_board[1][to_square[1:]] == "")):
                    return False

            if self._the_board[file.index(from_square[0])][from_square[1:]].get_color() == "black":
                if (isinstance(self._the_board[0][to_square[1:]], General) and
                        self._the_board[1][to_square[1:]] == "" and self._the_board[2][to_square[1:]] == "" and
                        self._the_board[3][to_square[1:]] == "" and self._the_board[4][to_square[1:]] == "" and
                        self._the_board[5][to_square[1:]] == "" and self._the_board[6][to_square[1:]] == "" and
                        self._the_board[7][to_square[1:]] == "" and self._the_board[8][to_square[1:]] == "" or
                        (isinstance(self._the_board[8][to_square[1:]], General) and
                         self._the_board[2][to_square[1:]] == "" and self._the_board[3][to_square[1:]] == "" and
                         self._the_board[4][to_square[1:]] == "" and self._the_board[5][to_square[1:]] == "" and
                         self._the_board[6][to_square[1:]] == "" and self._the_board[7][to_square[1:]] == "" and
                         self._the_board[8][to_square[1:]] == "") or
                        (isinstance(self._the_board[7][to_square[1:]], General) and
                         self._the_board[3][to_square[1:]] == "" and self._the_board[4][to_square[1:]] == "" and
                         self._the_board[5][to_square[1:]] == "" and self._the_board[6][to_square[1:]] == "" and
                         self._the_board[7][to_square[1:]] == "" and self._the_board[8][to_square[1:]] == "")):
                    return False

        # return False if illegal move by Advsior
        if isinstance(self._the_board[file.index(from_square[0])][from_square[1:]], Advisor):

            # cannot put player's own General in check

        # return False if illegal move by Elephant
        if isinstance(self._the_board[file.index(from_square[0])][from_square[1:]], Elephant):
            # cannot put player's own General in check
            if self._the_board[file.index(from_square[0])][from_square[1:]].get_color() == "red" and \

            if self._the_board[file.index(from_square[0])][from_square[1:]].get_color() == "black" and \

            # Elephants cannot jump so return False if there is a piece blocking its first diagonal move
            if ((self._the_board[file.index(from_square[0]) + 1][from_square[1:] + 1] == ""  and
                 self._the_board[file.index(from_square[0]) + 2][from_square[1:] + 2] ==
                 self._the_board[file.index(to_square[0])][to_square[1:]]) or
                (self._the_board[file.index(from_square[0]) - 1][from_square[1:] - 1] == "" and
                 self._the_board[file.index(from_square[0]) - 2][from_square[1:] - 2] ==
                 self._the_board[file.index(to_square[0])][to_square[1:]]) or
                (self._the_board[file.index(from_square[0]) + 1][from_square[1:] - 1] == "" and
                 self._the_board[file.index(from_square[0]) + 2][from_square[1:] - 2] ==
                 self._the_board[file.index(to_square[0])][to_square[1:]]) or
                (self._the_board[file.index(from_square[0]) - 1][from_square[1:] + 1] == "" and
                 self._the_board[file.index(from_square[0]) - 2][from_square[1:] + 2] ==
                 self._the_board[file.index(to_square[0])][to_square[1:]])):
                    return False

        # return False if illegal move by Horse
        if isinstance(self._the_board[file.index(from_square[0])][from_square[1:]], Horse):
            # cannot put player's own General in check

            # Horses cannot jump so return False if there is a piece blocking its first orthogonal move
            if ((file.index(from_square[0]) - 2 == file.index(to_square[0]) and
                 from_square[1:] - 1 == to_square[1:] and
                 self._the_board[file.index(from_square[0]) - 1][from_square[1:]] != "") or
                (file.index(from_square[0]) - 2 == file.index(to_square[0]) and
                 from_square[1:] + 1 == to_square[1:] and
                self._the_board[file.index(from_square[0]) - 1][from_square[1:]] != "") or
                (file.index(from_square[0]) - 1 == file.index(to_square[0]) and
                 from_square[1:] + 2 == to_square[1:] and
                self._the_board[file.index(from_square[0])][from_square[1:] + 1] != "") or
                (file.index(from_square[0]) + 1 == file.index(to_square[0]) and
                 from_square[1:] + 2 == to_square[1:] and
                self._the_board[file.index(from_square[0])][from_square[1:] + 1] != "") or
                (file.index(from_square[0]) + 2 == file.index(to_square[0]) and
                 from_square[1:] + 1 == to_square[1:] and
                self._the_board[file.index(from_square[0]) + 1][from_square[1:]] != "") or
                (file.index(from_square[0]) + 2 == file.index(to_square[0]) and
                 from_square[1:] - 1 == to_square[1:] and
                self._the_board[file.index(from_square[0]) + 1][from_square[1:]] != "") or
                (file.index(from_square[0]) + 1 == file.index(to_square[0]) and
                 from_square[1:] - 2 == to_square[1:] and
                self._the_board[file.index(from_square[0])][from_square[1:] - 1] != "") or
                (file.index(from_square[0]) - 1 == file.index(to_square[0]) and
                 from_square[1:] - 2 == to_square[1:]) and
                self._the_board[file.index(from_square[0])][from_square[1:] - 1] != ""):
                return False

        # return False if illegal move by Chariot
        if isinstance(self._the_board[file.index(from_square[0])][from_square[1:]], Chariot):
            # cannot put player's own General in check

            # Chariots cannot jump so return False if there is a piece in its orthogonal path
            from_square_path = from_square
            to_square_path = to_square
            i = 1
            while file.index(from_square_path[0]) != file.index(to_square_path[0]):
                if self._the_board[file.index(from_square_path[0])] == self._the_board[file.index(to_square_path[0])] \
                    and (self._the_board[file.index(from_square_path[0]) + i][from_square_path[1:]] != "" or
                     self._the_board[file.index(from_square_path[0]) - i][from_square_path[1:]] != ""):
                    return False

                if self._the_board[from_square_path[1:]] == self._the_board[to_square_path[1:]] and \
                    (self._the_board[file.index(from_square_path[0])][from_square_path[1:] + i] != "" or
                     self._the_board[file.index(from_square_path[0])][from_square_path[1:] - i] != ""):
                    return False
                i += 1

        # return False if illegal move by Cannon
        if isinstance(self._the_board[file.index(from_square[0])][from_square[1:]], Cannon):
            # cannot put player's own General in check
            # Cannons move any distance orthogonally without jumping, so if square_to is empty,
            # return False if there is a piece in its path
              if square_to contains a piece of the opposite color, and there is ONLY ONE piece in the path between
              square_from and square_to, then the Cannon may jump to capture and return True

        # return False if illegal move by Soldier
        if isinstance(self._the_board[file.index(from_square[0])][from_square[1:]], Soldier):
            # cannot put player's own General in check

        # otherwise, make move and remove any captured piece
        self._the_board[file.index(to_square[0])][to_square[1:]] = \
            self._the_board[file.index(from_square[0])][from_square[1:]]
        self._the_board[file.index(from_square[0])][from_square[1:]] = ""

        # if red or black General moved, update rank and file
        if isinstance(self._the_board[file.index(from_square[0])][from_square[1:]], General):
            self._red_general_rank = to_square[0]
            self._red_general_file = from_square[1:]

        # if red General is in checkmate or red player is in stalemate, update _game_state to "BLACK WON"
        # if self.is_in_check("red") and (red General has no legal moves or all red pieces have no legal moves):
        #     self._game_state = "BLACK_WON"
        #
        # if black General is in checkmate or black player is in stalemate, update _game_state to "RED WON"
        # if self.is_in_check("black") and (black General has no legal moves or all black pieces have no legal moves):
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
                file.index(from_square[0]) < 3 and 6 > from_square[1:] > 2 and \
                ((file.index(to_square[0]) + 1 == file.index(from_square[0]) or
                  (file.index(to_square[0]) - 1 == file.index(from_square[0])) and
                  to_square[1:] - from_square[1:] == 0)) or \
                (file.index(to_square[0]) - file.index(from_square[0]) == 0 and
                 (to_square[1:] + 1 == from_square[1:] or to_square[1:] - 1 == from_square[1:])):
            return True

        if self._color == "black" and \
                file.index(from_square[0]) > 6 and 6 > from_square[1:] > 2 and \
                ((file.index(to_square[0]) + 1 == file.index(from_square[0]) or
                  (file.index(to_square[0]) - 1 == file.index(from_square[0])) and
                  to_square[1:] - from_square[1:] == 0)) or \
                (file.index(to_square[0]) - file.index(from_square[0]) == 0 and
                 (to_square[1:] + 1 == from_square[1:] or to_square[1:] - 1 == from_square[1:])):
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
                file.index(from_square[0]) < 3 and 6 > from_square[1:] > 2 and \
                (file.index(to_square[0]) == file.index(from_square[0]) + 1 and
                 to_square[1:] == from_square[1:] + 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 1 and
                 to_square[1:] == from_square[1:] - 1):
            return True

        if self._color == "black" and \
                file.index(from_square[0]) > 6 and 6 > from_square[1:] > 2 and \
                (file.index(to_square[0]) == file.index(from_square[0]) + 1 and
                 to_square[1:] == from_square[1:] + 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 1 and
                 to_square[1:] == from_square[1:] - 1):
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
                ((file.index(from_square[0]) == 0 and from_square[1:] == 2) or
                 (file.index(from_square[0]) == 0 and from_square[1:] == 6) or
                 (file.index(from_square[0]) == 2 and from_square[1:] == 0) or
                 (file.index(from_square[0]) == 2 and from_square[1:] == 4) or
                 (file.index(from_square[0]) == 2 and from_square[1:] == 9) or
                 (file.index(from_square[0]) == 4 and from_square[1:] == 2) or
                 (file.index(from_square[0]) == 4 and from_square[1:] == 7)) and \
                (file.index(to_square[0]) == file.index(from_square[0]) + 2 and
                 to_square[1:] == from_square[1:] + 2) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 2 and
                 to_square[1:] == from_square[1:] - 2) or \
                (file.index(to_square[0]) == file.index(from_square[0]) + 2 and
                 to_square[1:] == from_square[1:] - 2) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 2 and
                 to_square[1:] == from_square[1:] + 2):
            return True

        if self._color == "black" and \
                ((file.index(from_square[0]) == 9 and from_square[1:] == 2) or
                 (file.index(from_square[0]) == 9 and from_square[1:] == 6) or
                 (file.index(from_square[0]) == 7 and from_square[1:] == 0) or
                 (file.index(from_square[0]) == 7 and from_square[1:] == 4) or
                 (file.index(from_square[0]) == 7 and from_square[1:] == 9) or
                 (file.index(from_square[0]) == 5 and from_square[1:] == 2) or
                 (file.index(from_square[0]) == 5 and from_square[1:] == 7)) and \
                (file.index(to_square[0]) == file.index(from_square[0]) + 2 and
                 to_square[1:] == from_square[1:] + 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 1 and
                 to_square[1:] == from_square[1:] - 1) or \
                (file.index(to_square[0]) == file.index(from_square[0]) + 2 and
                 to_square[1:] == from_square[1:] - 2) or \
                (file.index(to_square[0]) == file.index(from_square[0]) - 2 and
                 to_square[1:] == from_square[1:] + 2):
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

        if ((file.index(from_square[0]) - 2 == file.index(to_square[0]) and from_square[1:] - 1 == to_square[1:]) or
            (file.index(from_square[0]) - 2 == file.index(to_square[0]) and from_square[1:] + 1 == to_square[1:]) or
            (file.index(from_square[0]) - 1 == file.index(to_square[0]) and from_square[1:] + 2 == to_square[1:]) or
            (file.index(from_square[0]) + 1 == file.index(to_square[0]) and from_square[1:] + 2 == to_square[1:]) or
            (file.index(from_square[0]) + 2 == file.index(to_square[0]) and from_square[1:] + 1 == to_square[1:]) or
            (file.index(from_square[0]) + 2 == file.index(to_square[0]) and from_square[1:] - 1 == to_square[1:]) or
            (file.index(from_square[0]) + 1 == file.index(to_square[0]) and from_square[1:] - 2 == to_square[1:]) or
            (file.index(from_square[0]) - 1 == file.index(to_square[0]) and from_square[1:] - 2 == to_square[1:])):
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

        if self._color == "red" and \
                file.index(to_square[0]) - file.index(from_square[0] == 0) or \
                to_square[1:] - from_square[1:] == 0:
            return True

        if self._color == "black" and \
                file.index(to_square[0]) - file.index(from_square[0] == 0) or \
                to_square[1:] - from_square[1:] == 0:
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

        if self._color == "red" and \
                file.index(to_square[0]) - file.index(from_square[0] == 0) or \
                to_square[1:] - from_square[1:] == 0:
            return True

        if self._color == "black" and \
                file.index(to_square[0]) - file.index(from_square[0] == 0) or \
                to_square[1:] - from_square[1:] == 0:
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
                  to_square[1:] - from_square[1:] == 0)) or \
                (file.index(from_square[0]) > 4 and file.index(to_square[0]) - file.index(from_square[0]) == 0 and
                 (to_square[1:] + 1 == from_square[1:] or to_square[1:] - 1 == from_square[1:])):
            return True

        if self._color == "black" and \
                file.index(from_square[0]) > file.index(to_square[0]) and \
                ((file.index(to_square[0]) + 1 == file.index(from_square[0]) or
                  (file.index(to_square[0]) - 1 == file.index(from_square[0])) and
                  to_square[1:] - from_square[1:] == 0)) or \
                (file.index(from_square[0]) < 5 and file.index(to_square[0]) - file.index(from_square[0]) == 0 and
                 (to_square[1:] + 1 == from_square[1:] or to_square[1:] - 1 == from_square[1:])):
            return True
        return False
