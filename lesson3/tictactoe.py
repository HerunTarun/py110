import random
import json
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

def prompt(message):
    print(f'==> {message}')

def clear_screen():
    os.system('clear')

def display_welcome():
    prompt(messages['welcome'])
    prompt(messages['name_intro'])
    prompt(messages['games_rules'])

def display_board(board):
    clear_screen()

    prompt(messages['player_markers'].format(HUMAN_MARKER = HUMAN_MARKER, 
                                             COMPUTER_MARKER = COMPUTER_MARKER))
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----|-----|-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----|-----|-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        formatted_valid_choices = ', '.join(valid_choices)
        
        prompt(messages['player_input'].format(
            formatted_valid_choices = formatted_valid_choices))
        
        square = input().strip()
        if square in valid_choices:
            break
        
        prompt(messages['invalid_input'])

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for line in winning_combinations:
        square1, square2, square3 = line
        if (board[square1] == HUMAN_MARKER 
            and board[square2] == HUMAN_MARKER 
            and board[square3] == HUMAN_MARKER):
            return messages['win']
        elif (board[square1] == COMPUTER_MARKER 
              and board[square2] == COMPUTER_MARKER 
              and board[square3] == COMPUTER_MARKER):
            return messages['lose']
    
    return None

def replay_game():
    prompt(messages['replay'])

    if not is_yes():
        prompt(messages['goodbye'])
        return False

    return True

def is_yes():
    answer = input().lower()

    while answer not in ['y', 'n']:
        prompt(messages['invalid_input'])
        prompt(messages['replay_options'])
        answer = input().lower()
    
    if answer == 'y':
        return True
    else:
        return False

def play_tic_tac_toe():
    while True:
        board = initialize_board()

        while True:
            display_board(board)
            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                break
            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break
    
        if someone_won(board):
            prompt(f"{detect_winner(board)}")
        else:
            prompt(messages['tie'])
        
        if not replay_game():
            break

with open('ttt_messages.json', 'r') as file:
    messages = json.load(file)

play_tic_tac_toe()