import requests
import json
import random
from copy import deepcopy

URL = 'https://agutowski.com/connect4/'
GLOBAL_GAME_STATE = None


def start_game():
    global GLOBAL_GAME_STATE
    GLOBAL_GAME_STATE = json.loads(requests.post(
        URL + 'create_game/', data={'bot': 'level4'}).text)
    print(GLOBAL_GAME_STATE)
    print('Gra rozpoczeta; link do informacji o grze: %s' %
          (URL + 'show_game/?game_id=%s' % GLOBAL_GAME_STATE['game_id']))


def make_move(col):
    global GLOBAL_GAME_STATE
    if game_ended():
        raise Exception('Nie można wykonać ruchu; gra się już skończyła')
    res = requests.post(
        URL + 'make_move/', data={'game_id': GLOBAL_GAME_STATE['game_id'], 'move': col}).text
    try:
        GLOBAL_GAME_STATE = json.loads(res)
        print('Wykonano ruch: %d.' % col)
        if game_won():
            print('Wygrałeś!')
        elif game_tied():
            print('Remis!')
        else:
            print('Odpowiedź bota: %d.' % GLOBAL_GAME_STATE['last_move'])
            if game_lost():
                print('Przegrałeś!')
            elif game_tied():
                print('Remis!')
    except:
        raise Exception(
            'Nie udało się wykonać ruchu; odpowiedź serwera: %s' % res)


def get_board():
    if GLOBAL_GAME_STATE is None:
        raise Exception(
            'Musisz rozpocząć grę przed wywołaniem funkcji get_board().')
    return deepcopy(GLOBAL_GAME_STATE['board'])


def print_board():
    board = get_board()
    print('Aktualny stan planszy:')
    for row in board:
        print(' '.join(map(str, row)))
    print('-'*20)


def game_won(): return GLOBAL_GAME_STATE['game_status'] == 'GAME_WON'
def game_lost(): return GLOBAL_GAME_STATE['game_status'] == 'GAME_LOST'
def game_tied(): return GLOBAL_GAME_STATE['game_status'] == 'GAME_TIED'
def game_in_progress(
): return GLOBAL_GAME_STATE['game_status'] == 'GAME_IN_PROGRESS'
def game_ended(): return not game_in_progress()
