fruits = ['berries', 'bananas', 'mangoes']
more_fruits = ['apples', 'lemons', 'pears']
vegetables = ('carrots', 'beetroots', 'leeks')
more_vegetables = ('onions', 'broccoli', 'spinach')

all_fruits = fruits + more_fruits
print(all_fruits)
# This will print 

all_vegetables = vegetables + more_vegetables
print(all_vegetables)
# This will print 

# mixed_greens = fruits + vegetables
# This will raise a TypeError, since you can't concatenate a list and a tuple

mixed_greens = fruits + list(vegetables)
print(mixed_greens)
# This will print ['berries', 'bananas', 'mangoes', 'carrots', 'beetroots', 'leeks']

fruits = ['berries', 'bananas', 'mangoes']
vegetables = ('carrots', 'beetroots', 'leeks')

mixed_greens_list = [*fruits, *vegetables]
print(mixed_greens_list)

mixed_greens_tuple = (*fruits, *vegetables)
print(mixed_greens_tuple)

mixed_greens_set = {*fruits, *vegetables}
print(mixed_greens_set)

def provoke_argument(object1, object2):
	print(f'A {object1} is obviously better than a {object2}!')

# While you could do this:
furniture = ['sectional', 'stool']
provoke_argument(furniture[0], furniture[1])

# The unary operator allows you to do this:
furniture = ['barstool', 'hammock']
provoke_argument(*furniture)

numbers = [1, [2, 3, 4], 5]
a, (b, c, d), e = numbers
print(a, b, c, d, e)
# This will print 1 2 3 4 5