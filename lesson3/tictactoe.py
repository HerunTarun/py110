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

def prompt(message):
    print(f'==> {message}')

def clear_screen():
    os.system('clear')

def display_welcome():
    prompt(messages['welcome'])
    prompt(messages['game_rules'].format(GAMES_TO_WIN = GAMES_TO_WIN))
    print()
    prompt(messages['opponent_intro'])
    prompt(messages['alexandra_intro'])
    prompt(messages['margaret_intro'])
    prompt(messages['cookie_intro'])
    print()

def choose_opponent():
    prompt(messages['choose_opponent'])
    while True:
        answer = input().lower().strip()
        if answer in ['cookie', 'margaret', 'alexandra', 'alex', 'marge']:
            break
        prompt(messages['invalid_opponent_choice'])
    
    match answer[0]:
        case 'a':
            return 'Alexandra'
        case 'c':
            return 'Cookie'
        case 'm':
            return 'Margaret'

def display_challenge(opponent):
    prompt(messages['computer_challenge'].format(opponent = opponent))

def display_board(board, opponent):
    prompt(messages['markers'].format(HUMAN_MARKER = HUMAN_MARKER,
                                      COMPUTER_MARKER = COMPUTER_MARKER,
                                      opponent = opponent))
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

def which_bot_chooses_square(board, opponent):
    match opponent:
        case 'Alexandra':
            return random.choice(empty_squares(board))
        case 'Margaret':
            return margaret_chooses_square(board)
        case 'Cookie':
            return cookie_chooses_square(board)

def margaret_chooses_square(board):
    player_choices = {square for square in board if board[square] == 'X'}
    computer_choices = {square for square in board if board[square] == 'O'}

    for combo in WINNING_COMBINATIONS:
        possible_win = set(combo) & computer_choices
        if len(possible_win) == 2:
            return list(set(combo) - possible_win)[0]

    for combo in WINNING_COMBINATIONS:
        best_defense = set(combo) & player_choices
        if len(possible_win) == 2:
            return list(set(combo) - best_defense)[0]
        
    if 5 in empty_squares(board):
        return 5

    return random.choice(empty_squares(board))

def cookie_chooses_square(board):
    return random.choice(empty_squares(board))

def computer_chooses_square(board, opponent):
    if len(empty_squares(board)) == 0:
        return
    square = which_bot_chooses_square(board, opponent)
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def is_game_over(board, opponent):
    return bool(detect_result(board, opponent))

def detect_result(board, opponent):
    for line in WINNING_COMBINATIONS:
        square1, square2, square3 = line
        if (board[square1] == HUMAN_MARKER
            and board[square2] == HUMAN_MARKER
            and board[square3] == HUMAN_MARKER):
            return 'Player'
        elif (board[square1] == COMPUTER_MARKER
              and board[square2] == COMPUTER_MARKER
              and board[square3] == COMPUTER_MARKER):
            return opponent
        elif board_full(board):
            return 'Draw'

    return None

def display_winner(winner, opponent):
    if winner == 'Player':
        display_player_win(opponent)
    elif winner in COMPUTER_OPPONENTS:
        display_computer_winner(winner)
    else:
        display_tie(opponent)

def display_player_win(opponent):
    match opponent:
        case 'Alexandra':
            prompt(messages['player_win_alexandra'])
        case 'Margaret':
            prompt(messages['player_win_margaret'])
        case 'Cookie':
            prompt(messages['player_win_cookie'])

def display_computer_winner(winner):
    match winner:
        case 'Alexandra':
            prompt(messages['alexandra_win'])
        case 'Margaret':
            prompt(messages['margaret_win'])
        case 'Cookie':
            prompt(messages['cookie_win'])

def display_tie(opponent):
    match opponent:
        case 'Alexandra':
            prompt(messages['alexandra_tie'])
        case 'Margaret':
            prompt(messages['margaret_tie'])
        case 'Cookie':
            prompt(messages['cookie_tie'])

def update_match_score(winner, scores):
    if winner == 'Player':
        scores['player_score'] += 1

    if winner in COMPUTER_OPPONENTS:
        scores['computer_score'] += 1

def display_match_score(scores):
    prompt(messages['match_score'].format(
                                    player_score = scores['player_score'],
                                    computer_score = scores['computer_score']
                                    ))

def is_match_over(scores):
    return bool(GAMES_TO_WIN in list(scores.values()))

def display_match_winner(scores, opponent):
    if scores['player_score'] == GAMES_TO_WIN:
        display_player_match_winner(opponent)

    if scores['computer_score'] == GAMES_TO_WIN:
        display_computer_match_winner(opponent)

def display_player_match_winner(opponent):
    match opponent:
        case 'Alexandra':
            prompt(messages['player_match_winner_alexandra'])
        case 'Margaret':
            prompt(messages['player_match_winner_margaret'])
        case 'Cookie':
            prompt(messages['player_match_winner_cookie'])

def display_computer_match_winner(opponent):
    match opponent:
        case 'Alexandra':
            prompt(messages['alexandra_match_winner'])
        case 'Margaret':
            prompt(messages['margaret_match_winner'])
        case 'Cookie':
            prompt(messages['cookie_match_winner'])

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
    answer = input().lower().strip()

    while answer not in ['y', 'n']:
        prompt(messages['invalid_input'])
        prompt(messages['replay_options'])
        answer = input().lower()

    return bool(answer == 'y')

def choose_square(board, current_player, opponent):
    if current_player == 'Player':
        player_chooses_square(board)
    else:
        computer_chooses_square(board, opponent)

def choose_player():
    prompt(messages['choose first player'])
    if is_yes():
        return 'Player'

    return 'Computer'

def switch_player(current_player):
    if current_player == 'Player':
        return 'Computer'

    return 'Player'

def is_new_game(scores):
    if (scores['player_score'] == 0) and (scores['computer_score'] == 0):
        return True
    return False

def play_tic_tac_toe():
    clear_screen()
    display_welcome()
    scores = {'player_score': 0, 'computer_score': 0}
    
    while True:
        if is_new_game(scores):
            opponent = choose_opponent()
            display_challenge(opponent)
        
        current_player = choose_player()
        clear_screen()
        board = initialize_board()

        while True:
            clear_screen()
            display_board(board, opponent)
            choose_square(board, current_player, opponent)
            current_player = switch_player(current_player)
            if detect_result(board, opponent):
                clear_screen()
                display_board(board, opponent)
                break

        if is_game_over(board, opponent):
            winner = detect_result(board, opponent)
            display_winner(winner, opponent)
            update_match_score(winner, scores)
            display_match_score(scores)

        if is_match_over(scores):
            display_match_winner(scores, opponent)
            clear_score(scores)
        
        if not replay_game():
            break

with open('ttt_messages.json', 'r') as file:
    messages = json.load(file)

play_tic_tac_toe()