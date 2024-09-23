# Write another function that returns True if the string passed as an argument
# is a palindrome, or False otherwise. This time, however, your function 
# should be case-insensitive, and should ignore all non-alphanumeric 
# characters. If you wish, you may simplify things by calling the 
# is_palindrome function you wrote in the previous exercise.

# PEDAC

# Input
# string

# Output
# Boolean True or False

# Boundaries/Assumptions
# case insensitive
# ignore all non-alphanumeric characters

# Data Structure
# function, slicing

# Algorithm
# create a list of alphanumeric characters from the input string
# convert list into new string
# check for palindromic tendency using slicing

# Code
def is_real_palindrome(string):
    formatted_as_lst = [char.lower() for char in string 
                        if char.isalnum() == True]
    formatted_string = ''.join(formatted_as_lst)
    return formatted_string == formatted_string[::-1]

# Refactor
# use casefold() instead of .lower() to catch more languages


# Examples/Test Cases
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True