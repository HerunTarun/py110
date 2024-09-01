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

# Problem 8

# Problem 9

# Problem 10

# Problem 11
