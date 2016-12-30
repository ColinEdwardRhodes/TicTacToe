import random
import copy
import random


class GameLogic:
    """The logic for the game"""

    def __init__(self):
        """ Constructor """

    def deadlock(self, board):
        """No empty positions exist"""

        deadlock = True;

        for row in range(0, 3):
            for col in range(0, 3):
                if board.get(row, col) == board.empty():
                    deadlock = False

        return deadlock

    def solved(self, board):
        """Have we solved the board?"""

        """ Left corner """
        if board.get(0, 0) != board.empty() and (board.get(0, 0) == board.get(1, 1) == board.get(2, 2)):
            return True
        elif board.get(0, 0) != board.empty() and (board.get(0, 0) == board.get(1, 0) == board.get(2, 0)):
            return True
        elif board.get(0, 0) != board.empty() and (board.get(0, 0) == board.get(0, 1) == board.get(0, 2)):
            return True

        """ Right corner """
        if board.get(2, 2) != board.empty() and (board.get(2, 2) == board.get(1, 1) == board.get(0, 0)):
            return True
        elif board.get(2, 2) != board.empty() and (board.get(2, 2) == board.get(1, 2) == board.get(0, 2)):
            return True
        elif board.get(2, 2) != board.empty() and (board.get(2, 2) == board.get(2, 1) == board.get(2, 0)):
            return True

        """ cross in the middle """
        if board.get(1, 1) != board.empty() and (board.get(0, 1) == board.get(1, 1) == board.get(2, 1)):
            return True
        elif board.get(1, 1) != board.empty() and (board.get(1, 0) == board.get(1, 1) == board.get(1, 2)):
            return True

        """ last diagonal """
        if board.get(2, 0) != board.empty() and (board.get(2, 0) == board.get(1, 1) == board.get(0, 2)):
            return True

        return False

    def computerMove(self, board, cc):
        """The computer's turn!"""

        print "My move!"

        """ Start out by looking for winning positions """
        if self.winIfICan(board, cc):
            return

        """ Then blocking positions """
        if self.blockIfICan(board, cc):
            return

        """ Then pick any open position"""
        if self.pickAnyOpenPosition(board, cc):
            return

    def winIfICan(self, board, cc):
        """If there are two in a row of the current color I can win!"""

        # Copy the object
        boardCopy = copy.deepcopy(board)

        for row in range(0, 3):
            for col in range(0, 3):

                if boardCopy.get(row, col) == board.empty():

                    boardCopy.set(row, col, cc)

                    if self.solved(boardCopy):
                        board.set(row, col, cc)
                        print "Ta da! I win!"
                        return True
                    else:
                        """Put the empty value back"""
                        boardCopy.set(row, col, board.empty())

        return False

    def blockIfICan(self, board, cc):
        """If there are two in a row of the opposing color, pick a blocking spot"""

        opposite = board.oppositeColor(cc)

        boardCopy = copy.deepcopy(board)

        for row in range(0, 3):
            for col in range(0, 3):

                if boardCopy.get(row, col) == board.empty():

                    boardCopy.set(row, col, opposite)

                    if self.solved(boardCopy):
                        board.set(row, col, cc)
                        print "Blocked ya!"
                        return True
                    else:
                        """ Put the empty value back"""
                        boardCopy.set(row, col, board.empty())

        return False

    def pickAnyOpenPosition(self, board, cc):
        """Pick any open position"""

        values = []

        for row in range(0, 3):
            for col in range(0, 3):
                if board.get(row, col) == board.empty():
                    values.append((row, col))

        if len(values) > 0:
            """ pick a random value """

            pos = random.randint(0, len(values) - 1)
            value = values[pos];

            board.set(value[0], value[1], cc)
            return True

        return False
