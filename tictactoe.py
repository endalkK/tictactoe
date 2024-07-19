import math
import copy
"""
Tic Tac Toe Player
"""


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xCount += 1
            elif board[i][j] == O:
                oCount += 1
    """
    xCount = board[0].count(X) + board[1].count(X) + board[2].count(X)
    oCount = board[0].count(O) + board[1].count(O) + board[2].count(O)

    if xCount <= oCount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible.add((i, j))
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (len(actions(board)) < 5):
        if ((board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) or (board[0][2] == board[1][1]) and (board[1][1] == board[2][0])):  # diagonal
            return board[1][1]
        else:
            for i in range(3):
                if (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]):  # horizontal
                    return board[0][i]
                elif (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]):  # vertical
                    return board[i][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None) or (len(actions(board)) == 0):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (terminal(board)):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
