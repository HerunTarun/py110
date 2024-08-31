# Problem 1
# Sort the following list of numbers first in ascending numeric order, then 
# in descending numeric order. Do not mutate the list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]
answer1 = [-16, -6, 7, 8, 9, 10, 11, 50]
answer2 = [50, 11, 10, 9, 8, 7, -6, -16]
print(sorted(lst) == answer1)
print(sorted(lst, reverse=True) == answer2)

# Problem 2
# Repeat the previous exercise but, this time, 
# perform the sort by mutating the original list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]
answer3 = [-16, -6, 7, 8, 9, 10, 11, 50]
answer4 = [50, 11, 10, 9, 8, 7, -6, -16] 
lst.sort()
print(lst == answer3)
lst.sort(reverse=True)
print(lst == answer4)

# Problem 3
# Repeat problem 2 but, this time, sort the list as string values. 
# Both the list passed to the sorting function and 
# the returned list should contain numbers, not strings.

lst = [10, 9, -6, 11, 7, -16, 50, 8]
answer5 = [-16, -6, 10, 11, 50, 7, 8, 9] 
answer6 = [9, 8, 7, 50, 11, 10, -6, -16]
lst.sort(key=str)
print(lst == answer5)
lst.sort(reverse=True, key=str)
print(lst == answer6)

# Problem 4

# How would you sort the following list of dictionaries 
# based on the year of publication of each book, 
# from the earliest to the most recent?

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

answer7 = [
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800'
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869'
    },
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967'
    }
]

def sort_by_year(book):
    age = book['published']
    return int(age)

sorted_books = sorted(books, key=sort_by_year)


print(sorted_books == answer7)
