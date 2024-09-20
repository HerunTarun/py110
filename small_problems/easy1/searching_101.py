# Write a program that solicits six (6) numbers from the user and 
# prints a message that describes whether the sixth number 
# appears among the first five.

# PEDAC

# Input
# Numbers as a String

# Output
# A String that indicates whether the last number entered was among 
# the first five numbers given

# Boundaries/Assumptions
# negative numbers allowed
# infinity allowed
# only numbers allowed

# Examples/Test Cases
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.

# Data Structure
# list, while loop, functions

# Algorithm
# Ask for a number 
# Store number in list
# Repeat until list has six elements
# Use .pop() or slicing and in keyword to check whether 
# last element is in list without last element
# return answer string

# Code
def obtain_numbers():
    lst1 = []
    counter = 0
    while len(lst1) < 6:
        formatted_count = ['1st', '2nd', '3rd', '4th', '5th', 'last']
        number = input(f'Enter the {formatted_count[counter]} number: ')
        while True:
            try:
                float(number)
                break
            except ValueError:
                number = input("Please enter a valid number: ")
        lst1.append(number)
        counter += 1
    return lst1 

def display_result(numbers):
    last_num = numbers[-1]
    if last_num in numbers[:-1]:
        print(f'{last_num} is in {','.join(numbers[:-1])}')
    else:
        print(f"{last_num} isn't in {','.join(numbers[:-1])}")
    
def searching():
    numbers = obtain_numbers()
    display_result(numbers)

searching()

# Refactor
# Added Exception handling for validating user input
# used a float coercion in exception handling to allow infinity
# used slicing instead of .pop() to avoid mutation bugs
