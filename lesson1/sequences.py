games = ['shogi', 'chess', 'go']
print(games[-2])
# This will print 'chess'

names = ['Warden', 'Heirarch', 'Champion']
names[2] = 'Valiant ' + names[2]
print(names)

numbers = [1, 2, 3, 4]
numbers[0] = numbers[0] + 1

for index in range(4):
    numbers[index] = numbers[index] + 1

print(numbers)

plants = ('jade', 'pothos', 'curry leaf')
print(plants[0])
# This will print jade

opening = "King's Gambit"
print(opening[1])
# This will print i
print(opening[-1])
# This will print t

numbers = range(100)
print(numbers[3])
# This will print 3
print(numbers[-4])
# This will print 95

numbers = range(5)
print(list(numbers))
# This will print [0, 1, 2, 3, 4]
numbers = range(5, 0, -1)
print(list(numbers))
# This will print [5, 4, 3, 2, 1]

quote = 'Unleash the Kraken'
print(quote[8:])

numbers = (1, 2, 3, 4)
print(numbers[::1])
# This will print (1, 2, 3, 4)
print(numbers[::-1])
# This will print (4, 3, 2, 1)

numbers = (1, 2, 3, 4, 5)
print(numbers[:3])
# This will print (1, 2, 3, 4)
print(numbers[2:])
# This will print (3, 4, 5)

numbers = [1, 2, 3, 4, 5, 6]
print(numbers[5:1])
# This will print []
print(numbers[5:1:-1])
# This will print [6, 5, 4, 3, 2]
print(numbers[1:3:-1])
# This will print []

numbers = (1, 2, 3, 4, 5, 6)
print(numbers[::2])
# This will print (1, 3, 5)

opening_for_white = 'Ponziani Opening'
print(len(opening_for_white))

games = ['chess', 'go', 'checkers']
for game in games:
	print(game)
# This will print chess, go, and checkers on separate lines

more_games = ('shogi', 'reversi', 'mancala')
for game in more_games:
	print(game)
# This will print shogi, reversi, and mancala on separate lines

checkmate = "Lolli's Mate"
for char in checkmate:
	print(char)
# This will print each character on a separate line.

for number in range(4):
	print(number)
# This will print 0, 1, 2, 3 on their own line

numbers = [1, 2, 3]
index = 0
while index < len(numbers):
	print(f'item {index}: {numbers[index]}')
	index += 1

# This will print:
# item 0: 1
# item 1: 2
# item 2: 3

numbers = [1, 2, 3] + [4, 5, 6]
print(numbers)
# This will print [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 2, 2, 3, 4]
print(numbers.count(2))
# This will print 3

numbers = [1, 2, 2, 2, 3, 4]
print(numbers.index(2))
# This will print 1

numbers = (1, 2, 3, 4, 5)
print(min(numbers))
# This will print 1
print(max(numbers))
# This will print 5

name = 'decalcomanie'
print(min(name))
print(max(name))

group_name = 'Red Velvet'
print(list(group_name))
# This will print ['R', 'e', 'd', ' ', 'V', 'e', 'l', 'v', 'e', 't']

meals = ('breakfast', 'lunch', 'dinner')
print(list(meals))
# This will print ['breakfast', 'lunch', 'dinner']

print(list(range(5)))
# This will print [0, 1, 2, 3, 4]

group_name = 'Red Velvet'
print(tuple(group_name))
# This will print ('R', 'e', 'd', ' ', 'V', 'e', 'l', 'v', 'e', 't')

meals = ['breakfast', 'lunch', 'dinner']
print(tuple(meals))
# This will print ('breakfast', 'lunch', 'dinner')

print(tuple(range(5)))
# This will print (0, 1, 2, 3, 4)


meals = ['breakfast', 'lunch', 'dinner']
print(str(meals))

meals = ('breakfast', 'lunch', 'dinner')
print(str(meals))

print(str(range(5)))

title = ['Sovereign', 'of', 'the', 'Three', 'Realms']
print(' '.join(title))
# This will print Sovereign of the Three Realms

numbers = [1, 2, 3, 4]
print(', '.join([str(num) for num in numbers]))
# This will print '1, 2, 3, 4'