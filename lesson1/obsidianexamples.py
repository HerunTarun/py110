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
print('cent', 'dollar', 'quarter', sep=', ', end='<-\n')

# id examples
greeting = 'hello world'
print(id(greeting))

def remove_last_element(list):
	list.pop()
numbers = [1, 2, 3, 4, 5]
remove_last_element(numbers)
print(numbers)

name1 = None
name2 = 'Jerry'
is_name = name1 or name2
print(is_name)


numbers = (2, 3, 4, 5)
other_numbers = tuple(numbers)

print(numbers)
# This will print (2, 3, 4, 5)
print(other_numbers)
# This will print (2, 3, 4, 5)

print(numbers == other_numbers)
# This will print True
print(numbers is other_numbers)
# This will print False

numbers = {2, 3, 4, 5}
other_numbers = set(numbers)

print(numbers)
# This will print {2, 3, 4, 5}
print(other_numbers)
# This will print {2, 3, 4, 5}

print(numbers == other_numbers)
# This will print True
print(numbers is other_numbers)
# This will print False


numbers = frozenset([2, 3, 4, 5])
other_numbers = frozenset(numbers)

print(numbers)
# This will print frozenset(2, 3, 4, 5)
print(other_numbers)
# This will print frozenset(2, 3, 4, 5)

print(numbers == other_numbers)
# This will print True
print(numbers is other_numbers)
# This will print False

name = 'twice'
new_set = set(name)
print(new_set)