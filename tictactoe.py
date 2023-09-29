"""
Tic Tac Toe Player
"""

import math
import copy

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
    """
    x_player = 0
    o_player = 0

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                x_player += 1
            else:
                o_player += 1

    if x_player > o_player:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_action = set()

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possible_action.add((i, j))
    return possible_action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board) #new board
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][1] for i in board[1]):
        return board[1][1]
    elif all(i == board[2][2] for i in board[2]):
        return board[2][2]


    #columns
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]

    #diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][0]

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty = False
    for row in board:
        if EMPTY in row:
            empty = True
    if winner(board) is not None or (winner(board) is None and not empty ):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return 0
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        return max_value(board)
    else:
        return min_value(board)


def min_value(board):
    if terminal(board):
        return utility(board), None
    val = 9999999
    for action in actions(board):
        val = min(val, max_value(result(board, action)))
        return val, None

def max_value(board):
    if terminal(board):
        return utility(board), None
    val = -9999999
    for action in actions(board):
        val = max(val, min_value(result(board, action)))
        return val, None
