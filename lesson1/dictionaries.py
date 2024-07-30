food_types = { 
			 'protein': 'chicken',
			 'carbohydrate': 'bread',
			 'vegetable': 'carrot'
			 }

print(food_types['protein'])
# This will print 'chicken'

# winter_games = {
# 				['ice', 'snow']: 'skiing', 
# 				'ice': 'hockey'
# 				}
# This will raise a TypeError since lists are unhashable

food_types = { 
			 'protein': 'chicken',
			 'carbohydrate': 'bread',
			 'vegetable': 'carrot'
			 }
print(food_types['protein'][3])
# This will print c, which is the character indexed at 3 in the string chicken

# food_types = { 
# 			 'protein': 'chicken',
# 			 'carbohydrate': 'bread',
# 			 'vegetable': 'carrot'
# 			 }
# print(food_types['fats'])
# # This will raise a KeyError

food_types = { 
			 'protein': 'chicken',
			 'carbohydrate': 'bread',
			 'vegetable': 'carrot'
			 }
print(food_types.get('fats', "This key doesn't exist"))
# This will return 'This key doesn't exist

food_types = { 
			 'protein': 'chicken',
			 'carbohydrate': 'bread',
			 'vegetable': 'carrot'
			 }
print('fats' not in food_types)
# This will print True
print('protein' in food_types)
# This will print True

food_types = { 
			 'protein': 'chicken',
			 'carbohydrate': 'bread',
			 'vegetable': 'carrot'
			 }
food_types['protein'] = 'beef'
food_types['fats'] = 'avocado oil'
del food_types['carbohydrate']
print(food_types)

vehicles = {'truck', 'sedan', 'carriage'}
print('apple' in vehicles)
# This will print False
print('truck' in vehicles)
# This will print True

vehicles = {'truck', 'sedan', 'carriage'}
vehicles.add('suv')
print(vehicles)

vehicles = {'truck', 'sedan', 'carriage'}
vehicles.remove('truck')
print(vehicles)
# This will print{'sedan', 'carriage'}

vehicles.discard('suv')
print(vehicles)
# This will print {'sedan', 'carriage'}
# vehicles.remove('suv')
# This will riase a KeyError

tactics = frozenset(['pin', 'skewer', 'x-ray'])
print('pin' in tactics)
# This will print True
print('remove the defender' in tactics)
# This will print False

food_types = { 
			 'protein': 'chicken',
			 'carbohydrate': 'bread',
			 'vegetable': 'carrot'
			 }
print('protein' in food_types)
# This will print True

vehicles = {'truck', 'sedan', 'carriage'}
print('truck' in vehicles)
# This will print True

tactics = frozenset(['pin', 'skewer', 'x-ray'])
print('pin' in tactics)
# This will print True

food_types = { 
			 'protein': 'chicken',
			 'carbohydrate': 'bread',
			 'vegetable': 'carrot'
			 }
print(len(food_types))
# This will print 3

vehicles = {'truck', 'sedan', 'carriage'}
print(len(vehicles))
# This will print 3

tactics = frozenset(['pin', 'skewer', 'x-ray'])
print(len(tactics))
# This will print 3

food_types = { 
			 'protein': 'chicken',
			 'carbohydrate': 'bread',
			 'vegetable': 'carrot'
			 }
food_types.clear()
print(food_types)
# This will print {}

vehicles = {'truck', 'sedan', 'carriage'}
vehicles.clear()x
print(vehicles)
# This will print {}

tactics = frozenset(['pin', 'skewer', 'x-ray'])
# tactics.clear()
# # This will raise an Attribute Error

cards = [('heart', 'seven'), ('spade', 'four'), ('clubs', 'king')]
print(dict(cards))

suit = ['hearts', 'clubs', 'spades', 'diamonds']
value = ['seven', 'four', 'king', 'jack']
zipped = zip(suit, value)
print(dict(zipped))

numbers = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9, 9, 10]
print(set(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9, 9, 10]
print(frozenset(numbers))
# This will print frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})