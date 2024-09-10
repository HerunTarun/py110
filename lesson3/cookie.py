INITIAL_MARKER = ' '

board = {
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

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def cookie_chooses_square(board):
    

print(cookie_chooses_square(board))