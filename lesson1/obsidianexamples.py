import time

word = 'dreamcatcher'
print(len(word))
# This will print 12

# range
print(len(range(5)))
# This will print 5

# tuple
fruit = ('apple', 'banana', 'cherry')
print(len(fruit))
# This will print 3

# list
games = ['chess', 'checkers', 'go']
print(len(games))
# This will print 3

# dictionary
classical_ratings = {'Magnus': 2832,'Hikaru': 2802,'Fabiano': 2793,'Arjun': 2778}
print(len(classical_ratings))
# This will print 4

# set
vehicles = {'truck', 'sedan', 'carriage'}
print(len(vehicles))
# This will print 3

# frozen set
tactics = frozenset(['pin', 'skewer', 'x-ray'])
print(len(tactics))
# This will print 3

# print function examples
print(time.asctime())
print('cent', 'dollar', 'quarter')
print('cent', 'dollar', 'quarter', sep=', ')
print('cent', 'dollar', 'quarter', sep=', ', end='<-')