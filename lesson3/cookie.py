import random
import json
import os
import pdb

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINNING_COMBINATIONS = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
COMPUTER_OPPONENTS = ['Alexandra', 'Margaret', 'Cookie']
GAMES_TO_WIN = 3
BOARD = {
    1: 'O', 
    2: ' ', 
    3: 'X', 
    4: 'X', 
    5: ' ', 
    6: 'X', 
    7: ' ', 
    8: 'O', 
    9: 'O'
    }

def cookie_chooses_square(BOARD, opponent):
    def score(BOARD, opponent):
        match detect_result(BOARD, opponent):
            case 'Player':
                return 10
            case 'Cookie':
                return -10
            case 'Draw':
                return 0
    scores = []
    moves = []
    if is_game_over():
        return score(BOARD, opponent)
    
    for square in empty_squares(BOARD):
        BOARD[square] = 

def empty_squares(BOARD):
    return [key for key, value in BOARD.items() if value == INITIAL_MARKER]

def margaret_chooses_square(BOARD):
    player_choices = {square for square in BOARD if BOARD[square] == 'X'}
    computer_choices = {square for square in BOARD if BOARD[square] == 'O'}

    for combo in WINNING_COMBINATIONS:
        possible_win = set(combo) & computer_choices
        if len(possible_win) == 2:
            return list(set(combo) - possible_win)[0]

    for combo in WINNING_COMBINATIONS:
        best_defense = set(combo) & player_choices
        if len(best_defense) == 2:
            return list(set(combo) - best_defense)[0]
        
    if 5 in empty_squares(BOARD):
        return 5

    return random.choice(empty_squares(BOARD))


def board_full(BOARD):
    return len(empty_squares(BOARD)) == 0

def is_game_over(BOARD, opponent):
    return bool(detect_result(BOARD, opponent))

def detect_result(BOARD, opponent):
    for line in WINNING_COMBINATIONS:
        square1, square2, square3 = line
        if (BOARD[square1] == HUMAN_MARKER
            and BOARD[square2] == HUMAN_MARKER
            and BOARD[square3] == HUMAN_MARKER):
            return 'Player'
        elif (BOARD[square1] == COMPUTER_MARKER
              and BOARD[square2] == COMPUTER_MARKER
              and BOARD[square3] == COMPUTER_MARKER):
            return opponent
        elif board_full(BOARD):
            return 'Draw'

    return None

def switch_player(current_player):
    if current_player == 'Player':
        return 'Computer'

    return 'Player'

def empty_squares(BOARD):
    return [key for key, value in BOARD.items() if value == INITIAL_MARKER]


    

print(cookie_chooses_square(BOARD))