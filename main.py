import gameBoard
import gameLogic


def run_loop():
    """The main run loop"""

    print "Welcome to ticTacToe"

    pc = choose_color()
    board = gameBoard.Board()
    game_logic = gameLogic.GameLogic();

    board.display()

    cc = pc

    while not game_logic.solved(board) and not game_logic.deadlock(board):

        if cc == pc:
            move = choose_move(board, cc)
            board.makeMove(move, cc)
        else:
            game_logic.computerMove(board, cc)

        board.display()

        cc = board.oppositeColor(cc)

    if game_logic.solved(board):
        print "We have a winner!"
    else:
        print "We have a deadlock!"

    return


def choose_move(board, cc):
    """Choose the next move for the current color"""
    move = raw_input("Please Choose a move as [r,c]> ")
    while not board.validate(move, cc):
        move = raw_input("Please Choose a move as [r,c]> ")

    return move


def choose_color():
    """Choose the player color"""

    color = raw_input("Please Choose a Color (B or W)> ")
    while color != "B" and color != "W":
        color = raw_input("Please Choose a Color (B or W)> ")

    return color[0]

run_loop()
