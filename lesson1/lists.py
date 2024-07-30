my_list = [1, 1, 2, 3, 4, 5, 5, 6, 1, 1, 2, 3, 4]
print(my_list.count(1))
# This will print 4

my_list = [1, 1, 2, 3, 4, 5, 5, 6, 1, 1, 2, 3, 4]
print(my_list.index(3))
# This will print 3, since that's where it appears first
print(my_list.index(2, 5))
# This will print 10, since that's where 2 appears first after index 5
print(my_list.index(2, 0, -4))
# This will print 2, since that's where 2 appears first before index -4

games = ['chess', 'checkers', 'go']
games.append('scrabble')
print(games)
# This will print ['chess', 'checkers', 'go', 'scrabble']

games = ['chess', 'checkers', 'go']
games.insert(1, 'scrabble')
print(games)
# This will print ['chess', 'scrabble', 'checkers', 'go']

games = ['chess', 'checkers', 'go']
games.insert(7, 'scrabble')
print(games)
# This will print ['chess', 'checkers', 'go', 'scrabble']

games = ['chess', 'checkers', 'go']
more_games = ['scrabble', 'catan', 'mancala']
games.extend(more_games)
print(games)
# This will print ['chess', 'checkers', 'go', 'scrabble', 'catan', 'mancala']

games = ['chess', 'checkers', 'go']
games.remove('checkers')
print(games)
# This will print ['chess', 'go']

games = ['chess', 'checkers', 'go', 'reversi', 'catan']
games.pop(1)
print(games)
# This will print ['chess', go', 'reversi', 'catan']
games.pop()
print(games)
# This will print ['chess', 'go', 'reversi']

games = ['chess', 'checkers', 'go']
games.reverse()
print(games)
# This will print ['go', 'checkers', 'chess']

numbers = ['61', '103', '525', '10100', '25', '3']
numbers.sort()
print(numbers)
# This will print ['10100', '103', '25', '3', '525', '61']

numbers = ['61', '103', '525', '10100', '25', '3']
numbers.sort(reverse=True)
print(numbers)
# This will print ['61', '525', '3', '25', '103', '10100']

numbers = ['61', '103', '525', '10100', '25', '3']
numbers.sort(key=int)
# This sorts the list as if all the elements were integers
print(numbers)
# This will print ['3', '25', '61', '103', '525', '10100']
numbers = ['61', '103', '525', 10100, '25', '3']
numbers.sort(key=str)
# This sorts the list as if all the elements were strings
print(numbers)
# This will print [10100, '103', '25', '3', '525', '61']

chess_time_controls = ('90 + 10', '15 + 10', '5 + 3')
classical, rapid, blitz = chess_time_controls
print(classical)
print(rapid)
print(blitz)