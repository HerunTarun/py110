numbers = [1, 5, 2, 5, 3, 2, 1, 5, 7, 2, 23, 1, 9]
ones = []

for num in numbers:
	if num == 1:
		ones.append(num)

print(ones)
# This will print [1, 1, 1]

vehicles = ['car', 'truck', 'suv', 'van']
pluralized_vehicles = []

for vehicle in vehicles:
	pluralized_vehicles.append(vehicle + 's')

print(pluralized_vehicles)
# This will print ['cars', 'trucks', 'suvs', 'vans']

def select_ones(numbers):
	ones = []
	for num in numbers:
		if num == 1:
			ones.append(num)
	return ones

def pluralize(words):
	pluralized = []
	for word in words:
		pluralized.append(word + 's')
	return pluralized

def select_fruit(produce):
	fruits = {}
	for key, value in produce.items():
		if value == 'Fruit':
			fruits[key] = value
	return fruits

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

def double_numbers(numbers):
    for index, num in enumerate(numbers):
        numbers[index] = num * 2
    return numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)   

def double_odd_numbers(numbers):
	doubled_numbers = []
	for index, num in enumerate(numbers):
		if index % 2 != 0:
			doubled_numbers.append(num * 2)
		else:
			doubled_numbers.append(num)
	return doubled_numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_numbers(my_numbers))  # [1, 8, 3, 14, 2, 12]

print(my_numbers)                      # [1, 4, 3, 7, 2, 6]

def select_type(produce_list, selection_criteria):
	items = {}
	for key, value in produce_list.items():
		if value == selection_criteria:
			items[key] = value
	return items

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_type(produce, 'Fruit'))
# This will print {'apple': 'Fruit', 'pear': 'Fruit'}

print(select_type(produce, 'Vegetable'))
# This will print {'carrot': 'Vegetable', 'broccoli': 'Vegetable'}

print(select_type(produce, 'Meat'))
# This will print {}

def double_numbers_modded(numbers, multiplier):
    doubled_numbers = []
    for num in numbers:
        doubled_numbers.append(num * multiplier)
    return doubled_numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers_modded(my_numbers, 2)) 
# This will print [2, 8, 6, 14, 4, 12]
print(double_numbers_modded(my_numbers, 3)) 
# This will print [3, 12, 9, 21, 6, 18]
print(my_numbers)                 
# This will print [1, 4, 3, 7, 2, 6]