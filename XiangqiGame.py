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
            [["red_chariot_1", "red_horse_1", "red_elephant_1", "red_advisor_1", "red_general", "red_advisor_2", "red_elephant_2", "red_horse_2", "red_chariot_2"],
             ["", "", "", "", "", "", "", "", ""],
             ["", "red_cannon_1", "", "", "", "", "", "red_cannon_2", ""],
             ["red_soldier_1", "", "red_soldier_2", "", "red_soldier_3", "", "red_soldier_4", "", "red_soldier_5"],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["black_soldier_1", "", "black_soldier_2", "", "black_soldier_3", "", "black_soldier_4", "", "black_soldier_5"],
             ["", "black_cannon_1", "", "", "", "", "", "black_cannon_2", ""],
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


class GamePiece:
    """
    Represents a GamePiece with data member.
    """

    def __init__(self):


class General:
    """
    Represents a General with data member.
    The general starts the game at the midpoint of the back edge, within the palace.
    The general may move and capture one point orthogonally and may not leave the palace, with the following exception.
    The two generals may not face each other along the same file with no intervening pieces.
    If that happens, the "flying general" move may be executed, in which the general to
    move may cross the board to capture the enemy general.
    In practice, this rule means that creating this situation in the first place means
    moving into check, and is therefore not allowed
    """

    def __init__(self):


class Advisor:
    """
    Represents an Advisor with data member.
    The advisors start on either side of the general. They move and capture one point diagonally and
    may not leave the palace, which confines them to five points on the board.
    The advisor is like the queen in Western chess.
    """

    def __init__(self):


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

    def __init__(self):


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

    def __init__(self):


class Chariot:
    """
    Represents a Chariot with data member.
    The chariot moves and captures any distance orthogonally, but may not jump over intervening pieces.
    The chariots begin the game on the points at the corners of the board. The chariot is often
    considered to be the strongest piece in the game due to its freedom of movement and lack of restrictions.
    The chariot is sometimes known as the rook by English-speaking players, since it is like the rook in Western chess.
    """

    def __init__(self):


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

    def __init__(self):


class Soldier:

    """
    Represents a Soldier with data member.
    Each side starts with five soldiers. Soldiers begin the game located on every other point one row back
    from the edge of the river. They move and capture by advancing one point. Once they have crossed the river,
    they may also move and capture one point horizontally. Soldiers cannot move backward, and
    therefore cannot retreat; after advancing to the last rank of the board, however,
    a soldier may still move sideways at the enemy's edge.
    The soldier is sometimes called the "pawn" by English-speaking players, due to the pieces' similarities.
    Soldiers are able to move sideways after crossing the river
    """

    def __init__(self):