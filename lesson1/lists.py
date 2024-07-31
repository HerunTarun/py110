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
# This will print 90 + 10
print(rapid)
# This will print 15 + 10
print(blitz)
# This will print 5 + 3

chess_time_controls = ('classical', 'rapid', 'blitz', 'bullet')
print(chess_time_controls.count('classical'))
# This will print 1
print(chess_time_controls.index('blitz'))
# This will print 2

print(list('Likey'))
# This will print ['L', 'i', 'k', 'e', 'y']

print(tuple('Twice'))
# This will print ('T', 'w', 'i', 'c', 'e')

games = ['chess', 'checkers', 'go']
tuple_games = tuple(games)
print(tuple_games)
# This will print ('chess', 'checkers', 'go')
print(list(tuple_games))
# This will print ['chess', 'checkers', 'go']

food_types = { 
			 'protein': 'chicken',
			 'carbohydrate': 'bread',
			 'vegetable': 'carrot'
			 }
key_list = list(food_types.keys())
print(key_list)
# This will print ['protein', 'carbohydrate', 'vegetable']
key_tuple = tuple(food_types.keys())
print(key_tuple)
# This will print ('protein', 'carbohydrate', 'vegetable')

food_types = { 
			 'protein': 'chicken',
			 'carbohydrate': 'bread',
			 'vegetable': 'carrot'
			 }
values_list = list(food_types.values())
print(values_list)
# This will print ['chicken', 'bread', 'carrot')]
values_tuple = tuple(food_types.values())
print(values_tuple)
# This will print ('chicken', 'bread', 'carrot')

food_types = { 
			 'protein': 'chicken',
			 'carbohydrate': 'bread',
			 'vegetable': 'carrot'
			 }
pairs_list = list(food_types.items())
print(pairs_list)
# This will print [('protein', 'chicken'), ('carbohydrate', 'bread'), ('vegetable', 'carrot')]
pairs_tuple = tuple(food_types.items())
print(pairs_tuple)
# This will print (('protein', 'chicken'), ('carbohydrate', 'bread'), ('vegetable', 'carrot'))

vehicles = {'truck', 'sedan', 'carriage'}
print(list(vehicles))
# This will print ['truck', 'carriage', 'sedan']
print(tuple(vehicles))
# This will print ('truck', 'carriage', 'sedan')

frozen_fruits = frozenset(['apple', 'banana', 'cherry'])
print(list(frozen_fruits))
# This will print ['apple', 'banana', 'cherry']
print(tuple(frozen_fruits))
# This will print ('apple', 'banana', 'cherry')

games = ['chess', 'checkers', 'go']
for game in games:
	print(game)
# This will print each game on a new line

more_games = ('shogi', 'reversi', 'mancala')
for game in more_games:
	print(game)
# This will print each game on a new line

for index, game in enumerate(games):
	print(f'{game} is at index {index}')
# This will print 'chess is at index 0' for each game and index on a new line