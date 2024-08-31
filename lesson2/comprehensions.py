matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_matrix = []

for row in matrix:
    for cell in row:
        flattened_matrix.append(cell)

print(flattened_matrix)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

flattened_matrix = [num for row in matrix 
					    for num in row]
print(flattened_matrix) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = (1, 2, 3, 4, 5)
squared = [num ** 2 for num in numbers]
print(squared) # [1, 4, 9, 16, 25]

numbers = range(6)
squared = [num ** 2 for num in numbers]
print(squared) # [0, 1, 4, 9, 16, 25]

numbers = {1, 2, 3, 4, 5}
squared = [num ** 2 for num in numbers]
print(squared) # [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = [print(num) for num in numbers if num % 2 != 0]
print(odd_numbers) # [None, None, None, None]

name = 'twice'
name_list = [char for char in name]
print(name_list) # ['t', 'w', 'i', 'c', 'e']

name = 'twice'
name_list = list(name)
print(name_list) # ['t', 'w', 'i', 'c', 'e']
