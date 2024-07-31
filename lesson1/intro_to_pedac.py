"""
PROBLEM:

Given a string, write a function `change_me` which returns the same
string but with all the words in it that are palindromes uppercased.
"""

# Comments show expected return values
change_me("We will meet at noon")       # "We will meet at NOON"
change_me("No palindromes here")        # "No palindromes here"
change_me("")                           # ""
change_me("I LOVE mom and dad equally") # "I LOVE MOM and DAD equally"

# Step 1 - Read the problem
# 2 - Check test cases

"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection should be case-sensitive.
"""

# Test cases:

# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]