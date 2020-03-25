from helpers import *
from calc_score import *
import copy


def next_move_score(board, row, column, player):
    new_board = copy.deepcopy(board)
    new_board[row][column] = player
    if row-1 in board_height_range:
        oponent_score = check_score(new_board, row-1, column, oponent(player))
    else:
        oponent_score = 0
    return oponent_score


def total_score(board, player):
    total_score = []
    posible_moves = possible_moves(board)
    for move in posible_moves:
        my_score = check_score(board, move[0], move[1], player)
        oponent_score = check_score(board, move[0], move[1], oponent(player))
        oponent_next_score = next_move_score(board, move[0], move[1], player)
        spot_score = attack_ratio*my_score+defense_ratio*oponent_score-oponent_next_score
        total_score.append(spot_score)
    score_summe = max(total_score)
    return score_summe


def deep_score(board, row, column, player, deep):
    new_board = copy.deepcopy(board)
    new_board[row][column] = player
    return calc_points(deep, new_board, player)


def check_score2(board, row, column, player):
    score = 0
    for i in range(4):
        # Direction in picked 4: len(directions)
        move = directions[i]
        #  Direction of moving picked 4:
        check_move = [move[0]*-1, move[1]*-1]

        for i in range(0, 4):
            picked_four = pick_four(
                board, row+check_move[0]*i, column+check_move[1]*i, move)
            if picked_four != 0:
                score = score+win_lose(picked_four, player)
    return score


def calc_points(deep, board, player):
    if deep > 0:
        deep -= 1
        moves = possible_moves(board)
        score = 0
        for move in moves:
            new_board = copy.deepcopy(board)
            new_board[move[0]][move[1]] = player
            player = oponent(player)
            if player == 2:
                score += calc_points(deep, new_board, player)
            else:
                score += calc_points(deep, new_board, player)
        return score
    else:
        score = 0
        moves = possible_moves(board)
        for move in moves:
            score = score+check_score2(board, move[0], move[1], player)
        return score
        # win_loose(board, player)
