import random
import json
import os
import pdb

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_TO_WIN = 3

def prompt(message):
    print(f'==> {message}')

def clear_screen():
    os.system('clear')

def display_welcome():
    prompt(messages['welcome'])
    prompt(messages['name_intro'])
    prompt(messages['game_rules'])

def display_board(board):
    prompt(messages['markers'].format(HUMAN_MARKER = HUMAN_MARKER,
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

def format_valid_choices(lst, sep=', ', conjunction='or'):
    if len(lst) < 2:
        result = ''
        for num in lst:
            result += str(num)
        return result
    elif len(lst) == 2:
        return f"{lst[0]} {conjunction} {lst[1]}"
    else:
        string_lst = [str(num) for num in lst]
        last_choice = string_lst.pop()
        return f"{sep.join(string_lst)}{sep}{conjunction} {last_choice}"

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        formatted_valid_choices = format_valid_choices(valid_choices)

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

def is_game_over(board):
    return bool(detect_result(board))

def detect_result(board):
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
            return 'Player'
        elif (board[square1] == COMPUTER_MARKER
              and board[square2] == COMPUTER_MARKER
              and board[square3] == COMPUTER_MARKER):
            return 'Alexandra'
        elif board_full(board):
            return 'Draw'

    return None

def display_winner(winner):
    match winner:
        case 'Player':
            prompt(messages['win'])
        case 'Alexandra':
            prompt(messages['lose'])
        case 'Draw':
            prompt(messages['tie'])

def update_match_score(winner, scores):
    if winner == 'Player':
        scores['player_score'] += 1

    if winner == 'Alexandra':
        scores['computer_score'] += 1

def display_match_score(scores):
    prompt(messages['match_score'].format(
                                    player_score = scores['player_score'],
                                    computer_score = scores['computer_score']
                                    ))

def is_match_over(scores):
    if GAMES_TO_WIN in list(scores.values()):
        return True

    return False

def display_match_winner(scores):
    if scores['player_score'] == GAMES_TO_WIN:
        prompt(messages['player_match_winner'])

    if scores['computer_score'] == GAMES_TO_WIN:
        prompt(messages['computer_match_winner'])

def clear_score(scores):
    scores['player_score'] = 0
    scores['computer_score'] = 0

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

    return bool(answer == 'y')

def choose_square(board, current_player):
    if current_player == 'Player':
        player_chooses_square(board)
    else:
        computer_chooses_square(board)

def choose_player():
    prompt(messages['choose first player'])
    if is_yes():
        return 'Player'

    return 'Computer'

def switch_player(current_player):
    if current_player == 'Player':
        return 'Alexandra'

    return 'Player'

def play_tic_tac_toe():
    clear_screen()
    display_welcome()
    scores = {'player_score': 0, 'computer_score': 0}
    while True:
        current_player = choose_player()
        clear_screen()
        board = initialize_board()

        while True:
            clear_screen()
            display_board(board)
            choose_square(board, current_player)
            current_player = switch_player(current_player)
            if detect_result(board):
                clear_screen()
                display_board(board)
                break

        if is_game_over(board):
            winner = detect_result(board)
            display_winner(winner)
            update_match_score(winner, scores)
            display_match_score(scores)

        if is_match_over(scores):
            display_match_winner(scores)
            clear_score(scores)
        else:
            pass

        if not replay_game():
            break

with open('ttt_messages.json', 'r') as file:
    messages = json.load(file)

play_tic_tac_toe()