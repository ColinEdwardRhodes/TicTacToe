import numpy


class Board:
    """The board for the game"""

    def empty(self):
        """ The empty cell """
        return 'E';

    def __init__(self):
        """ Constructor """

        self.board = numpy.chararray((3, 3))
        self.board[:] = self.empty()

    def get(self, row, col):
        return self.board[row,col]

    def set(self, row, col, value):
        self.board[row,col] = value

    def oppositeColor(self, color):
        """Return the opposite color"""
        if color == 'B':
            return 'W'
        else:
            return 'B'

    def display(self):
        """Display the board"""
        for i in range(0, 3):
            for j in range(0, 3):
                print self.board[i][j],
            print

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

        if self.get(row - 1, col - 1) != self.empty():
            print "Position occupied by color", self.get(row-1, col-1)
            return False

        return True

    def makeMove(self, move, color):
        """set a board position to a color"""
        col = int(move[3])
        row = int(move[1])

        self.set(row - 1, col - 1, color)



