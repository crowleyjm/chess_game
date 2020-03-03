# Author: Jillian Crowley
# Date: 03/02/2020
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
        Locations on the board will be specified using "algebraic notation",
        with columns labeled a-i and rows labeled 1-10, with row 1 being the Red side and row 10 the Black side
        """
        # creates empty board
        self._the_board = [["", "", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", "", ""]]

        self._red_chariot_1 = Chariot()

        # initializes board with red and black game pieces
        self._the_board[0][0] = self._red_chariot_1
        self._the_board[0][1] = "red_horse_1"
        self._the_board[0][2] = "red_elephant_1"
        self._the_board[0][3] = "red_advisor_1"
        self._the_board[0][4] = "red_general"
        self._the_board[0][5] = "red_advisor_2"
        self._the_board[0][6] = "red_elephant_2"
        self._the_board[0][7] = "red_horse_2"
        self._the_board[0][8] = "red_chariot_2"
        self._the_board[2][1] = "red_cannon_1"
        self._the_board[2][7] = "red_cannon_2"
        self._the_board[3][0] = "red_soldier_1"
        self._the_board[3][2] = "red_soldier_2"
        self._the_board[3][4] = "red_soldier_3"
        self._the_board[3][6] = "red_soldier_4"
        self._the_board[3][8] = "red_soldier_5"

        self._the_board[9][0] = "black_chariot_1"
        self._the_board[9][1] = "black_horse_1"
        self._the_board[9][2] = "black_elephant_1"
        self._the_board[9][3] = "black_advisor_1"
        self._the_board[9][4] = "black_general"
        self._the_board[9][5] = "black_advisor_2"
        self._the_board[9][6] = "black_elephant_2"
        self._the_board[9][7] = "black_horse_2"
        self._the_board[9][8] = "black_chariot_2"
        self._the_board[7][1] = "black_cannon_1"
        self._the_board[7][7] = "black_cannon_2"
        self._the_board[6][0] = "black_soldier_1"
        self._the_board[6][2] = "black_soldier_2"
        self._the_board[6][4] = "black_soldier_3"
        self._the_board[6][6] = "black_soldier_4"
        self._the_board[6][8] = "black_soldier_5"


        # Initialize row and column for each piece
        self._red_chariot_1_row = 0
        self._red_chariot_1_column = 0
        self._red_horse_1_row = 0
        self._red_horse_1_column = 1
        self._red_elephant_1_row = 0
        self._red_elephant_1_column = 2
        self._red_advisor_1_row = 0
        self._red_advisor_1_column = 3
        self._red_general_row = 0
        self._red_general_column = 4
        self._red_advisor_2_row = 0
        self._red_advisor_2_column = 5
        self._red_elephant_2_row = 0
        self._red_elephant_2_column = 6
        self._red_horse_2_row = 0
        self._red_horse_2_column = 7
        self._red_chariot_2_row = 0
        self._red_chariot_2_column = 8
        self._red_cannon_1_row = 2
        self._red_cannon_1_column = 1
        self._red_cannon_2_row = 2
        self._red_cannon_2_column = 7
        self._red_solider_1_row = 3
        self._red_solider_1_column = 0
        self._red_solider_2_row = 3
        self._red_solider_2_column = 2
        self._red_solider_3_row = 3
        self._red_solider_3_column = 4
        self._red_solider_4_row = 3
        self._red_solider_4_column = 6
        self._red_solider_5_row = 3
        self._red_solider_5_column = 8

        self._black_chariot_1_row = 9
        self._black_chariot_1_column = 0
        self._black_horse_1_row = 9
        self._black_horse_1_column = 1
        self._black_elephant_1_row = 9
        self._black_elephant_1_column = 2
        self._black_advisor_1_row = 9
        self._black_advisor_1_column = 3
        self._black_general_row = 9
        self._black_general_column = 4
        self._black_advisor_2_row = 9
        self._black_advisor_2_column = 5
        self._black_elephant_2_row = 9
        self._black_elephant_2_column = 6
        self._black_horse_2_row = 9
        self._black_horse_2_column = 7
        self._black_chariot_2_row = 9
        self._black_chariot_2_column = 8
        self._black_cannon_1_row = 7
        self._black_cannon_1_column = 1
        self._black_cannon_2_row = 7
        self._black_cannon_2_column = 7
        self._black_solider_1_row = 6
        self._black_solider_1_column = 0
        self._black_solider_2_row = 6
        self._black_solider_2_column = 2
        self._black_solider_3_row = 6
        self._black_solider_3_column = 4
        self._black_solider_4_row = 6
        self._black_solider_4_column = 6
        self._black_solider_5_row = 6
        self._black_solider_5_column = 8

        # initializes game state
        self._game_state = "UNFINISHED"

        # initializes player's turn
        self._player_turn = "red"


    def get_the_board(self):
        """Returns the board with labeled files and ranks."""
        printed_board = self._the_board
        printed_board.insert(0, ["", "a", "b", "c", "d", "e", "f", "g", "h", "i"])
        printed_board[1].insert(0, "1")
        printed_board[2].insert(0, "2")
        printed_board[3].insert(0, "3")
        printed_board[4].insert(0, "4")
        printed_board[5].insert(0, "5")
        printed_board[6].insert(0, "6")
        printed_board[7].insert(0, "7")
        printed_board[8].insert(0, "8")
        printed_board[9].insert(0, "9")
        printed_board[10].insert(0, "10")
        return print("\n".join(str(rank) for rank in printed_board))

    def get_game_state(self):
        """Returns the game state, either 'UNFINISHED', 'RED_WON' or 'BLACK_WON'."""
        return self._game_state


    def is_in_check(self, player):
        """
        Takes as a parameter either 'red' or 'black' and
        returns True if that player is in check, but returns False otherwise
        """
        if player == "red" and red_general_1 file equals file of a black piece with empty ranks in between:
            return True
        elif player == "black" and black_general_1 file equals file of a red piece with empty ranks in between:
            return True
        return False

    def make_move(self, from_square, to_square):
        """
        Takes two parameters - strings that represent the square moved from and
        the square moved to. For example, make_move('b3', 'b10').
        If the square being moved from does not contain a piece belonging to
        the player whose turn it is, or if the indicated move is not legal, or
        if the game has already been won, then it should just return False.
        Otherwise it should make the indicated move, remove any captured piece,
        update the game state if necessary, update whose turn it is, and return True

        If the general's player can make no move to prevent the general's capture, the situation is called "checkmate"
        Unlike in chess, in which stalemate is a draw, in xiangqi, it is a loss for the stalemated player.
        """

        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

        if self._player_turn not in self._the_board[letters.index(from_square[0])][from_square[1:]] or\
                legal_move == "no" or\
                self._game_state != "UNFINISHED":
            return False

        board_spaces[to_square] = board_spaces[from_square]

        board_spaces[from_square] = ""

        if self.is_in_check("red") and "red_general" has no legal moves:
            self._game_state = "BLACK_WON"

        if self.is_in_check("black") and "black_general" has no legal moves:
            self._game_state = "RED_WON"

        if self._player_turn == "red":
            self._player_turn = "black"

        if self._player_turn == "black":
            self._player_turn = "red"

        return True


class RedGamePiece:
    """
    Represents a GamePiece with data member.
    """


class BlackGamePiece:
    """
    Represents a GamePiece with data member.
    """


class General:
    """
    Represents a General.
    The general starts the game at the midpoint of the back edge, within the palace.
    The general may move and capture one point orthogonally and may not leave the palace, with the following exception.
    The two generals may not face each other along the same file with no intervening pieces.
    If that happens, the "flying general" move may be executed, in which the general to
    move may cross the board to capture the enemy general.
    In practice, this rule means that creating this situation in the first place means
    moving into check, and is therefore not allowed
    """
        # red general legal spaces if not occupied by red piece
        # [0][3], [0][4], [0][5], [1][3], [1][4], [1][5], [2][3], [2][4], [2][5]

        # red general illegal spaces
        # if red general square_to file is black general square_to file and ranks between them are empty

        # black general legal spaces if not occupied by black piece
        # [9][3], [9][4], [9][5], [8][3], [8][4], [8][5], [7][3], [7][4], [7][5]

        # black general illegal spaces
        # if black general square_to file is red general square_to file and ranks between them are empty


class Advisor:
    """
    Represents an Advisor.
    The advisors start on either side of the general. They move and capture one point diagonally and
    may not leave the palace, which confines them to five points on the board.
    The advisor is like the queen in Western chess.
    """
    # red advisor legal spaces if not occupied by red piece
    # [0][3], [0][5], [1][4], [2][3], [2][5]

    # black general legal spaces if not occupied by black piece
    # [9][3], [9][5], [8][4], [7][3], [7][5]


class Elephant:
    """
    Represents an Elephant with data member.
    These pieces move and capture exactly two points diagonally and may not jump over intervening pieces;
    If an elephant cannot move due to a diagonally adjacent piece, it is known as
    "blocking the elephant's eye"
    Elephants may not cross the river, and serve as defensive pieces. Because an elephant's movement is
    restricted to just seven board positions, it can be easily trapped or threatened.
    The two elephants are often used to defend each other.
    """
    # red elephant legal spaces if not occupied by red piece
    # [0][2], [0][6], [2][0], [2][4], [2][9], [4][2], [4][7]

    # black elephant legal spaces if not occupied by black piece
    # [9][2], [9][6], [7][0], [7][4], [7][9], [5][2], [5][7]


class Horse:
    """
    Represents a Horse with data member.
    Horses begin the game next to the elephants, on their outside flanks.
    A horse moves and captures one point orthogonally and then one point diagonally away from
    its former position. The horse does not jump as the knight does in Western chess, and
    can be blocked by a piece located one point horizontally or vertically adjacent to it.
    Blocking a horse is called "hobbling the horse's leg".
    Since horses can be blocked, it is sometimes possible to trap the opponent's horse.
    It is possible for one player's horse to have an asymmetric attack advantage if an opponent's horse is blocked.
    """
    # red elephant legal spaces if not occupied by red piece
    # one space orthogonal and one space diagonal, cannot move off board

    # black elephant legal spaces if not occupied by black piece
    # one space orthogonal and one space diagonal, cannot move off board


class Chariot:
    """
    Represents a Chariot with data member.
    The chariot moves and captures any distance orthogonally, but may not jump over intervening pieces.
    The chariots begin the game on the points at the corners of the board. The chariot is often
    considered to be the strongest piece in the game due to its freedom of movement and lack of restrictions.
    The chariot is sometimes known as the rook by English-speaking players, since it is like the rook in Western chess.
    """
    # red chariot legal moves
    # any distance orthogonal if no pieces in between, cannot move off board
    # if there is a red piece in between it stops one space short
    # if there is a black piece in between it moves to the space and captures piece

    # black chariot legal moves
    # any distance orthogonal if no pieces in between, cannot move off board
    # if there is a black piece in between it stops one space short
    # if there is a red piece in between it moves to the space and captures piece


class Cannon:
    """
    Represents a Cannon with data member.
    Each player has two cannons, which start on the row behind the soldiers, two points in front of the horses.
    Cannons move like chariots, any distance orthogonally without jumping,
    but can only capture by jumping a single piece, friend or foe, along the path of attack.
    The piece over which the cannon jumps is called the "cannon platform" or "screen".
    Any number of unoccupied spaces, including none, may exist between the cannon, screen, and
    the piece to be captured. Cannons can be exchanged for horses immediately from their starting positions.
    """
    # red cannon legal moves
    # any distance orthogonal if no pieces in between, cannot move off board
    # if there is any piece in its path, followed by a black piece, with any number of
    # empty spaces before or after the middle piece, it may jump that piece to capture the black piece.

    # black cannon legal moves
    # any distance orthogonal if no pieces in between, cannot move off board
    # if there is any piece in its path, followed by a red piece, with any number of
    # empty spaces before or after the middle piece, it may jump that piece to capture the red piece.


class Soldier:

    """
    Represents a Soldier with data member.
    Each side starts with five soldiers. Soldiers begin the game located on every other point one row back
    from the edge of the river. They move and capture by advancing one point. Once they have crossed the river,
    they may also move and capture one point horizontally. Soldiers cannot move backward, and
    therefore cannot retreat; after advancing to the last rank of the board, however,
    a soldier may still move sideways at the enemy's edge.
    The soldier is sometimes called the "pawn" by English-speaking players, due to the pieces' similarities.
    """
    # red soldier legal moves
    # cannot move off board, cannot move to space if occupied by another red piece
    # rank cannot decrease, so rank + 1
    # once rank > 5, rank + 1 or file + 1 or file - 1

    # black soldier legal moves
    # cannot move off board, cannot move to space if occupied by another black piece
    # rank cannot decrease, so rank + 1
    # once rank > 5, rank + 1 or file + 1 or file - 1
