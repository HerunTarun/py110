# Write a function that returns True if 
# the string passed as an argument is a palindrome, False otherwise. 
# A palindrome reads the same forwards and backwards. 
# For this problem, the case matters and all characters matter.

# PEDAC

# Input
# String that may or may not be a palindrome

# Output
# Boolean True or False

# Boundaries/Assumptions
# Case matters
# All characters matter

# Data Structure
# Function, loop

# Algorithm
# obtain length of string n
# loop through n/2 characters using a range starting from 0
# each iteration will check string[n] and string[-(n+1)] for equality
# if any iteration is false, return False
# if loop successfully completes, return True

# Code
def is_palindrome(string):
    for num in range(len(string) // 2):
        if string[num] != string [-(num +1)]:
            return False
    return True

# Refactor
# another solution

def is_LS_solution(s):
    return s == s[::-1]

# Examples/Test Cases
# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)