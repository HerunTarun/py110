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