from utils import *
from dictionary import *
from calc_score import *
from helpers import *
from move_prediction import *


def decide_where_to_move(board):
    total_score = []
    posible_moves = possible_moves(board)
    for move in posible_moves:
        my_score = check_score(board, move[0], move[1], 1)
        oponent_score = check_score(board, move[0], move[1], 2)
        oponent_next_score = next_move_score(board, move[0], move[1], 1)
        spot_score = attack_ratio*my_score+defense_ratio * oponent_score-oponent_next_score
        score = spot_score + deep_score(board, move[0], move[1], 1, 4)
        total_score.append(score)

    best_place = posible_moves[pick_random(total_score)]
    print("total score: ", total_score)
    return best_place[1]


def play():
    start_game()  # Musimy rozpocząć grę.
    # Pewnie będziemy chcieli mieć taką pętlę - dopóki gra się toczy, musimy zrobić jakiś ruch.
    while game_in_progress():
        board = get_board()
        decision = decide_where_to_move(board)
        make_move(decision)
        print_board()
    print_board()


# start_game()
# get_board()
# decide_where_to_move(test_board)
play()
