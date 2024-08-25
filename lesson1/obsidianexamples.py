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

numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(numbers[0:4])
# This will print ['a', 'b', 'c', 'd']
print(numbers[-4:-1])
# This will print ['g', 'h', 'i', 'j']
print(numbers[-1:-4])
# This will print []
print(numbers[:])
# This will print ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(numbers[::-1])
# This will print 
print(numbers[2::2])
# This will print ['c', 'e', 'g', 'i']


randoms = [1, 'dreamcatcher', (False, True, None)]
print(1 in randoms)
# True
print(7 in randoms)
# False
print((False, True, None) in randoms)
# True
print('catch' in randoms[1])
# True
print('acde' in randoms[1])
# False

numbers = [1, 2, 3, 5, 6, 6, 7, 8, 5, 3, 2, 5, 67]
print(sum(numbers))

guild = ['Sweets', 'Tricks', 'Cloak', 'Dagger', 'Style', 'Price']
print(guild.index('Cloak'))
# This will print 2
print(guild.index('Style'))
# This will print 4
# print(guild.index('Webs'))
# This will raise a ValueError
print(guild[0].index('t'))
# This will print 4


star_wars = "In a galaxy far far away"
print(star_wars.count('a'))
print(star_wars.count('z'))

numbers = [1, 2, 3, 5, 6, 6, 7, 8, 5, 3, 2, 5, 67]
print(numbers.count(5))
print(numbers.count(0))

names = ['Darling', 'Trissiny', 'Vandro', 'Principia']
tags = ['Sweets', 'Thorn', 'Webs', 'Keys']
affiliation = ['Eserion', 'Avei', 'Eserion', 'Avei']

zipped_characters = zip(names, tags, affiliation)
print(list(zipped_characters))

names = ['Darling', 'Trissiny', 'Vandro']
tags = ['Sweets', 'Thorn', 'Webs', 'Keys']
affiliation = ['Eserion', 'Avei', 'Eserion', 'Avei']

zipped_characters = zip(names, tags, affiliation, strict=True)
# print(list(zipped_characters))


classical_ratings = {
					'Magnus': 2832,
                    'Hikaru': 2802,
                    'Fabiano': 2793,
                    'Arjun': 2778
                    }

print(classical_ratings.keys())
print(classical_ratings.values())
print(classical_ratings.items())


lst = ['Cat', 'Hakram', 'Indrani']
lst.insert(2, 'Vivienne')
print(lst)
# ['Cat', 'Hakram', 'Vivienne', 'Indrani',]

lst = ['Cat', 'Hakram', 'Indrani']
lst.insert(200, 'Vivienne')
print(lst)
# ['Cat', 'Hakram', 'Indrani', 'Vivienne']

lst = ['Cat', 'Hakram', 'Indrani']
lst.insert(-2, 'Vivienne')
print(lst)

lst = ['Cat', 'Hakram', 'Indrani']
lst.extend(['Vivienne', 'Akua', 'Masego'])
print(lst)


names = ['Allan', 'Grace', 'Jeremy', 'Melody', 'Jimmy']
sorted_names = sorted(names)
print(sorted_names)

sorted_names = sorted(names, reverse=True)
print(sorted_names)

numbers = ['1', '5', '100', '15', '534', '53']
print(sorted(numbers))
#
print(sorted(numbers, key=int))
#

classical_ratings = {
					'Magnus': 2832,
                    'Hikaru': 2802,
                    'Fabiano': 2793,
                    'Arjun': 2778
                    }
print(sorted(classical_ratings))

gibberish = ['abc', 'DEF', 'xyz', '123']
gibberish.sort()
print(gibberish)
# ['123', 'DEF', 'abc', 'xyz']

gibberish.sort(key=str.lower)
print(gibberish)
# ['123', 'abc', 'DEF', 'xyz']

numbers = ['1', '5', '100', '15', '534', '53']
numbers.sort()
print(numbers)
# ['1', '100', '15', '5', '53', '534']

numbers.sort(key=int)
print(numbers)
# ['1', '5', '15', '53', '100', '534']

names = ['Allan', 'Grace', 'Jeremy', 'Melody', 'Jimmy']
reversed_names = list(reversed(names))
print(reversed_names)

import string
print(string.capwords("i cAn't belIEve it's already mid-july."))

idiom = 'Lions do not beget dogs'
print(idiom.startswith('do', 8)) # True
print(idiom.startswith('get', -9))
print(idiom.startswith('ion', 1, 10))
print(idiom.startswith('ion'))

idiom = 'Lions do not beget dogs'
print(idiom.endswith('dogs', 8)) # True
print(idiom.endswith('ion', 0, 4)) # True
print(idiom.endswith('ion')) # False

string_1 = 'is this a string?'
string_2 = ''
string_3 = 'is this 1 string?'
string_4 = 'dreamcatcher'

print(string_1.isalpha()) # True
print(string_2.isalpha()) # False
print(string_3.isalpha()) # False
print(string_4.isalpha()) # True

string_1 = '1234 1234'
string_2 = ''
string_3 = 'is this 1 string?'
string_4 = '1234'

print(string_1.isdigit()) # False, whitespace is not numeric
print(string_2.isdigit()) # False, empty string
print(string_3.isdigit()) # False, has alphabetic characters
print(string_4.isdigit()) # True

string_1 = '12 green frogs'
string_2 = ''
string_3 = '12greenfrogs'

print(string_1.isalnum()) # False, whitespace is not numeric or alphabetic
print(string_2.isalnum()) # False, empty string
print(string_3.isalnum()) # True

string_1 = '12 green frogs'
string_2 = ''
string_3 = 'twelve green frogs'

print(string_1.islower()) # False, whitespace is not numeric or alphabetic
print(string_2.islower()) # False, empty string
print(string_3.islower()) # True

string_1 = 'IS THIS LOWERCASE! WITH A 1'
string_2 = ''
string_3 = 'THIS IS NOT LOWERCASE'

print(string_1.isupper()) # True, numeric values are okay
print(string_2.isupper()) # False, empty string
print(string_3.isupper()) # True

string_1 = '   '
string_2 = ''
string_3 = 'This has whitespace characters, but not ONLY whitespace characters'

print(string_1.isspace()) # True, only whitespace characters
print(string_2.isspace()) # False, empty string
print(string_3.isspace()) # False, not just whitespace characters

text_input = '   The word is God   '
stripped_text = text_input.strip()
print(stripped_text)

text = 'aaabaacccabxyzabccba'
print(text.rstrip('a'))         # baacccabxyzabccb
print(text.rstrip('ab'))        # cccabxyzabcc
print(text.rstrip('ba'))        # cccabxyzabcc
print(text.rstrip('abc'))       # xyz

text = 'aaabaacccabxyzabccba'
print(text.lstrip('a'))         # aaabaacccabxyzabccb
print(text.lstrip('ab'))        # aaabaacccabxyzabcc
print(text.lstrip('ba'))        # aaabaacccabxyzabcc
print(text.lstrip('abc'))       # aaabaacccabxyz

text = 'With great power comes great responsibility'
split_text = text.split()
print(split_text)
split_text = text.split('great')
print(split_text)

text = 'With great power comes great responsibility'
split_text = text.split(' ', 3)
print(split_text)

quote = """A trusted companion who, after a string of personal 
disappointments, begins to dress in darker colours should no longer be 
considered a trusted companion."""
split_quote_by_line = quote.splitlines()
print(split_quote_by_line)

quote = ['Are', 'you', 'feeling', 'lucky', 'punk?']
print(' '.join(quote))
print(''.join(quote))
print(','.join(quote))

sentence = """A trusted companion who, after a string of personal 
disappointments, begins to dress in darker colours should no longer be 
considered a trusted companion."""

print(sentence.find('trusted')) # 2
print(sentence.find('trusted', 3)) # 138

print(sentence.rfind('trusted')) # 138
print(sentence.rfind('trusted', 0, 50)) # 2

squares = [number * number for number in range(5)]
print(squares)
# [0, 1, 5, 9, 16]


evens = [number for number in range(10) if number % 2 == 0]
print(evens)
# [0, 2, 4, 6, 8]

even_squares = [number * number for number in range(10) if number % 2 == 0]
print(even_squares)

squares = {f'{number}-squared': number * number 
		   for number in range(5)}
print(squares)

evens = {f'even {number}': number 
		 for number in range(10) if number % 2 == 0}
print(evens)

even_squares = {f'{number} squared': number * number 
				for number in range(10) if number % 2 == 0}
print(even_squares)

squares = {number * number for number in range(5)}
print(squares)

evens = {number for number in range(10) if number % 2 == 0}
print(evens)

even_squares = {number * number for number in range(10) if number % 2 == 0}
print(even_squares)

singular_number = 42
singular_number += 8
print(singular_number)           # 50

numbers = [1, 2, 3, 4]
numbers += [5, 6, 7, 8]
print(numbers)

import copy
my_list = [[1, 2,], 3, 4]
my_list2 = copy.copy(my_list)
print(my_list)
print(my_list2)
print(my_list == my_list2)
print(my_list is my_list2)
print(my_list[0] is my_list2[0])

my_list[0][1] = 'two'
print(my_list)
print(my_list2)


my_list = [[1, 2,], 3, 4]
my_list2 = copy.deepcopy(my_list)
print(my_list)                    # [[1, 2], 3, 4]
print(my_list2)                   # [[1, 2], 3, 4]
print(my_list == my_list2)        # True, they contain the same values
print(my_list is my_list2)        # False, they're different objects
print(my_list[0] is my_list2[0])  # False, nested objects are duplicated

my_list[0][1] = 'two'
print(my_list)                    # [[1, 'two'], 3, 4]
print(my_list2)                   # [[1, 2], 3, 4]

fruit = "apple"

def my_function():
    fruit = "banana"

    def nested_function():
        nonlocal fruit
        fruit = "cherry"

    nested_function()
    print(fruit)

my_function()
print(fruit)

names = frozenset(['Sweets', 'Cloak', 'Dagger'])
print(id(names))
# This will print a unique identity e.g. 140558144594528
names = frozenset(['Price', 'Cloak', 'Dagger'])
print(names)
# This will print something like {'Cloak', 'Dagger', 'Price'}
print(id(names))
# This will print a different unique identity e.g. 140558144594976