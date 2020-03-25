from dictionary import *
from helpers import *


def check_score(board, row, column, player):
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
                score = score+score_picked_four(picked_four, player)
    return score


def pick_four(board, row, column, move):
    picked_four = []
    for x in range(0, 4):
        spot_row = row+move[0]*x
        spot_column = column+move[1]*x

        if spot_row in board_height_range and spot_column in board_width_range:
            # print("Spot in Range")
            spot_value = board[spot_row][spot_column]
            picked_four.append(spot_value)
        else:
            picked_four = 0
            break
    # print("Picked four:", picked_four)
    return picked_four


def win_lose(picked_four, player):
    if picked_four.count(player) == 3:
        return 200000
    elif picked_four.count(oponent(player)) == 3:
        return 100000
    else:
        return 0


def score_picked_four(picked_four, player):
    score = 0
    bonus_count = 0
    if win_lose(picked_four, player) > 0:
        return win_lose(picked_four, player)
    elif picked_four.count(player) > 0:
        return 0
    else:
        for i in range(0, 4):
            if picked_four[i] == 0:
                score += 1
            elif picked_four[i] == player:
                score = score+bonus[bonus_count]
                bonus_count += 1
    return score
