# Problem 1
# Consider the following nested dictionary:
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
# Compute and display the total age of the family's male members. 
# Try working out the answer two ways: first with an ordinary loop, 
# then with a comprehension.
# The result should be 444.

collective_age = 0

for key, value in munsters.items():
    if value['gender'] == 'male':
        collective_age += value['age']

print(collective_age)

age_list = [person['age'] for person in munsters.values() 
                          if person['gender'] == "male"]

collective_age = sum(age_list)

print(collective_age)

# Problem 2
# Given the following, return a new list with the same structure, 
# but with the values in each sublist ordered in ascending order. 
# Use a comprehension if you can. (Try using a for loop first.)
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# Expected:  [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

new_lst = []
for element in lst:
    new_lst.append(sorted(element))

print(new_lst)

comprehension_list = [sorted(element) for element in lst]
print(comprehension_list)

# Problem 3
# Given the following data structure, return a new list with the same structure
# but with the values in each sublist ordered in ascending order as strings 
# (that is, the numbers should be treated as strings). 
# Use a comprehension if you can. (Try using a for loop first.)
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# Expected: [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]
new_lst = []

for sublist in lst:
    new_lst.append(sorted(sublist, key=str))

print(new_lst)

comprehension_list = [sorted(sublist, key=str) for sublist in lst]
print(comprehension_list)

# Problem 4
# Given the following data structure, write some code that defines a dictionary
# where the key is the first item in each sublist, and the value is the second.

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

dict1 = {element[0]: element[1] for element in lst}
print(dict1)

# Problem 5
# Given the following data structure, sort the list so that the sub-lists are 
# ordered based on the sum of the odd numbers that they contain. 
# You shouldn't mutate the original list.
lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
# Expected: [[1, 8, 3], [1, 6, 7], [1, 5, 3]]
def sort_by_odd(item):
    odd_numbers = [num for num in item if num % 2 != 0]
    return sum(odd_numbers)

new_lst = sorted(lst, key=sort_by_odd)
print(new_lst)

# Problem 6
# Given the following data structure, return a new list identical in structure 
# to the original but, with each number incremented by 1. 
# Do not modify the original data structure. Use a comprehension.
lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
# Expected: [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

new_lst = [{key: value + 1 for key, value in element.items()} 
                           for element in lst]
print(new_lst)


# WORK
# new_lst = []
# for element in lst:
#     for index, (key, value) in enumerate(element.items()):
#         new_lst[index] = {key: value + 1}
# print(new_lst)

# incremented_list = [item[key]: item[key] + 1 for item in lst
#                                    for key in item]
# print(incremented_list)

# Problem 7
# Given the following data structure 
# return a new list identical in structure to the original, 
# but containing only the numbers that are multiples of 3.
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
# Expected: [[], [3, 12], [9], [15, 18]]
def divisible_by_3(sublist):
    return [num for num in sublist if num % 3 == 0]

multiples_of_3 = [divisible_by_3(sublist) for sublist in lst]
print(multiples_of_3)

# Problem 8
# Given the following data structure, 
# write some code to return a list that contains 
# the colors of the fruits and the sizes of the vegetables. 
# The sizes should be uppercase, and the colors should be capitalized.
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}
# Expected: [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
def food_property(subdict):
    values = list(subdict.values())
    if values[0] == 'fruit':
        return [color.capitalize() for color in values[1]]
    else:
        return values[2].upper()

new_list = [food_property(subdict) for subdict in dict1.values()]
print(new_list)

## Another way
def transform_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()
new_list = [transform_item(subdict) for subdict in dict1.values()]
print(new_list)

# Problem 9
# Given the following data structure, write some code to return a list 
# that contains only the dictionaries where all the numbers are even.
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
#  Expected: [{e: [8], f: [6, 10]}]
# Input: 
# list of dictionaries that have lists as values

# Output: 
# a list that contains only dictionaries where ALL numbers are even

# Boundaries/Assumptions:
# Use a comprehension

# Data Structures
# Comprehension, helper function

# Algorithm
# Iterate through lst
# Iterate through values in nested lists of each dictionary
# While all values are even, return True
# Add dictionary to new_list 
# Return new_list
def add_even_dictionary(dict):
    if only_even_dictionaries(dict):
        return dict

def only_even_dictionaries(dict):
    for list in dict.values():
        for num in list:
            if num % 2 == 0:
                continue
            else:
                return False
    return True

def remove_None(list):
    clean_list = list
    while clean_list.count(None):
        clean_list.remove(None)
    return clean_list

new_list = [add_even_dictionary(dict) for dict in lst]
remove_None(new_list)
print(new_list)

# Another way

new_list = [dict for dict in lst if only_even_dictionaries(dict)]
print(new_list)

# Problem 10
# A UUID (Universally Unique Identifier) is a type of identifier often used to 
# uniquely identify items, even when some of those items were created 
# on a different server or by a different application. 
# That is, without any synchronization, two or more computer systems can 
# create new items and label them with a UUID with no significant risk of 
# stepping on each other's toes. 
# It accomplishes this feat through massive randomization. 
# The number of possible UUID values is approximately 3.4 X 10E38, 
# which is a huge number. The chance of a conflict, a "collision", is 
# vanishingly small with such a large number of possible values.

# Each UUID consists of 32 hexadecimal characters 
# (the digits 0-9 and the letters a-f) represented as a string. 
# The value is typically broken into 5 sections in an 8-4-4-4-12 pattern, 
# e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

# Write a function that takes no arguments and 
# returns a string that contains a UUID.

# Input
# No arguments

# Output
# A string that contains an UUID

# Boundaries/Assumptions
# Use a comprehension
# Clarify, is 'This is your UUID: <UUID>' acceptable as output?

# Data Structure
# Comprehension within function, possible helper function

# Algorithm
# define function
# create list of possible characters
# create list of UUID section lengths
# create 5 lists of UUID characters
# join lists into a string
# return the string as a f-string
import random
def create_UUID():
    def create_UUID_section(num):
        return [random.choice(UUID_characters) for _ in range(num)]

    UUID_characters = list('abcdef09123456789')
    UUID_section_lengths = [8, 4, 4, 4, 12]

    UUID_as_list = [create_UUID_section(num) for num in UUID_section_lengths]

    UUID = "-".join(["".join(section) for section in UUID_as_list])

    return f'This is your UUID: {UUID}'

print(create_UUID())
print(create_UUID())
print(create_UUID()) 

# Problem 11
# The following dictionary has list values that contains strings. 
# Write some code to create a list of every vowel (a, e, i, o, u) 
# that appears in the contained strings, then print it.
# Start by trying to write this using nested loops.

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = []
for words in dict1.values():
    for word in words:
        for char in word:
            if char in list('aeiou'):
                list_of_vowels.append(char)

answer = ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
print(list_of_vowels == answer)

# Extra Challenge: Once your nested loop code works, try to refactor the code 
# so it uses a single list comprehension. 
# (You can print the resulting list outside of the comprehension.)

list_of_vowels = [char for words in dict1.values()
                       for word in words
                       for char in word if char in list('aieou')]
print(list_of_vowels)
