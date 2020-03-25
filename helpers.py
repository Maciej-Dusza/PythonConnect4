import numpy as np
import random

test_board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 2, 1, 0, 0],
    [0, 0, 2, 2, 1, 0, 2],
    [1, 2, 2, 1, 2, 0, 2]
]


def possible_moves(board):
    moves = []
    column = 0
    while column < 7:
        row = 5
        while board[row][column] > 0:
            if row < 0:
                break
            row -= 1
        if column < 7 and row >= 0:
            moves.append([row, column])
        column += 1
    # print("Possible Moves", moves)
    return moves


def pick_random(scores):
    A = np.array(scores)
    maximum_indices = np.where(A == max(scores))[0]
    index = random.choice(maximum_indices)
    print("Indexes: ", maximum_indices, "Picked index:", index)
    return index


def oponent(player):
    if player == 1:
        return 2
    return 1
