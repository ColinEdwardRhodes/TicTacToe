import numpy
import copy
import random


class Board:
    """The board for the game and the solver functions"""

    def __init__(self):
        """ Constructor """

        """ I found out later we can set the type of data in a numpy array
        and could have used strings natively - oh well """
        self.board = numpy.zeros((3, 3))

        """ The empty cell """
        self.empty = self.boardValue("E");

    def oppositeColor(self, color):
        """Return the opposite color"""
        if color == "B":
            return "W"
        else:
            return "B"

    def deadlock(self):
        """No empty positions exist"""

        deadlock = True;

        for row in range(0, 3):
            for col in range(0, 3):
                if self.board[row][col] == self.empty:
                    deadlock = False

        return deadlock

    def solved(self):
        """Have we solved the board?"""

        b = self.board

        """ Left corner """
        if b[0][0] != 0 and (b[0][0] == b[1][1] == b[2][2]):
            return True
        elif b[0][0] != 0 and (b[0][0] == b[1][0] == b[2][0]):
            return True
        elif b[0][0] != 0 and (b[0][0] == b[0][1] == b[0][2]):
            return True

        """ Right corner """
        if b[2][2] != 0 and (b[2][2] == b[1][1] == b[0][0]):
            return True
        elif b[2][2] != 0 and (b[2][2] == b[1][2] == b[0][2]):
            return True
        elif b[2][2] != 0 and (b[2][2] == b[2][1] == b[2][0]):
            return True

        """ cross in the middle """
        if b[1][1] != 0 and (b[0][1] == b[1][1] == b[2][1]):
            return True
        elif b[1][1] != 0 and (b[1][0] == b[1][1] == b[1][2]):
            return True

        """ last diagonal """
        if b[2][0] != 0 and (b[2][0] == b[1][1] == b[0][2]):
            return True

        return False

    def display(self):
        """Display the board"""
        for i in range(0, 3):
            for j in range(0, 3):
                print self.color(self.board[i][j]),
            print

    def color(self, number):
        """Translate to a color"""
        if number == 0:
            return "E"
        elif number == 2:
            return "B"
        elif number == 1:
            return "W"

    def boardValue(self, stringVal):
        if stringVal == "B":
            return 2
        elif stringVal == "W":
            return 1
        elif stringVal == "E":
            return 0

    def validate(self, move, color):
        """The move should be of the form [x,y] and must be over an empty space"""
        if move[0] != '[' or move[4] != ']' or move[2] != ',':
            print "Use the form [x,y] to enter moves!"
            return False

        col = int(move[3])
        row = int(move[1])

        if row > 3 or row < 1:
            print "Bad column value (must be between 1 and 3)"
            return False

        if col > 3 or col < 1:
            print "Bad row value (must be between 1 and 3)"
            return False

        if self.color(self.board[row-1][col-1]) != "E":
            print "Position occupied by color", self.color(self.board[row-1][col-1])
            return False

        return True

    def makeMove(self, move, color):
        """set a board position to a color"""
        col = int(move[3])
        row = int(move[1])
        boardVal = self.boardValue(color)

        self.board[row-1][col-1] = boardVal

    def computerMove(self, move, cc):
        """The computer's turn!"""

        print "My move!"

        """ Start out by looking for winning positions """
        if self.winIfICan(cc):
            return

        """ Then blocking positions """
        if self.blockIfICan(cc):
            return

        """ Then pick any open position"""
        if self.pickAnyOpenPosition(cc):
            return

    def winIfICan(self, cc):
        """If there are two in a row of the current color I can win!"""

        # Copy the object
        boardCopy = copy.deepcopy(self)

        for row in range(0, 3):
            for col in range(0, 3):

                if boardCopy.board[row][col] == self.empty:

                    boardCopy.board[row][col] = boardCopy.boardValue(cc)

                    if boardCopy.solved():
                        self.board[row][col] = self.boardValue(cc)
                        print "Ta da! I win!"
                        return True
                    else:
                        """Put the empty value back"""
                        boardCopy.board[row][col] = self.empty

        return False

    def blockIfICan(self, cc):
        """If there are two in a row of the opposing color, pick a blocking spot"""

        opposite = self.oppositeColor(cc)

        boardCopy = copy.deepcopy(self)

        for row in range(0, 3):
            for col in range(0, 3):

                if boardCopy.board[row][col] == self.empty:

                    boardCopy.board[row][col] = boardCopy.boardValue(opposite)

                    if boardCopy.solved():
                        self.board[row][col] = self.boardValue(cc)
                        print "Blocked ya!"
                        return True
                    else:
                        """ Put the empty value back"""
                        boardCopy.board[row][col] = self.empty

        return False

    def pickAnyOpenPosition(self, cc):
        """Pick any open position"""

        values = []

        for row in range(0, 3):
            for col in range(0, 3):
                if self.board[row][col] == self.empty:
                    values.append((row, col))

        if len(values) > 0:
            """ pick a random value """

            pos = random.randint(0, len(values) - 1)
            value = values[pos];

            self.board[value[0]][value[1]] = self.boardValue(cc)
            return True

        return False

