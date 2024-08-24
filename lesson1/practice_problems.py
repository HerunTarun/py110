# Problem 1

# given the following, how would you count the # of occurences of 'banana' 
# in the tuple?

fruits = ("apple", "banana", "cherry", "date", "banana")

print(fruits.count('banana'))

# Problem 2
# What is the length of the set, given the following code. Try answering
# without running the code. 

numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers)) # 5, only unique objects in a set

# Problem 3
# Given the following sets, how would you obtain a set that contains all 
# the unique values from both sets

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a | b
print(c)

# Problem 4
# Given the follwing code, what would the output be? Try answering without 
# running the code

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)

# I'd get a dictionary with the strings as names, and the indexes as values.
# {
#     'Fred': 0,
#     'Barney': 1,
#     'Wilma': 2,
#     'Betty': 3,
#     'Pebbles': 4,
#     'Bamban': 5
# }

# Problem 5
# Calculate the total age given the following dictionary:
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

total_age = 0

for names in ages:
    total_age += ages[names]

print(total_age)

# total_age = sum(ages.values())

# Problem 6
# Determine the minimum age from the above ages dictionary

minimum_age = min(ages.values())
print(minimum_age)