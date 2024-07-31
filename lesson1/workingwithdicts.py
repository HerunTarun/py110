classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

print(classical_ratings['Magnus'])
# This will print 2832

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

del classical_ratings['Arjun']
print(classical_ratings)
# This will print {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2793}

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

print('Hikaru' in classical_ratings)
# This will print True
print('Gukesh' not in classical_ratings)
# This will print True

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

ratings_copy = classical_ratings.copy()
print(ratings_copy)
# This will print {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2793, 'Arjun': 2778}

print(id(classical_ratings) == id(ratings_copy))
# This will print False, since the two dictionaries are different objects in memory

ratings = {'Magnus': [2832, 2827, 2888],
					'Hikaru': [2802, 2746, 2874], 
					'Fabiano': [2793, 2738, 2777], 
					'Arjun': [2778, 2671, 2740]}

ratings_copy = ratings.copy()
ratings_copy['Arjun'][2] = 2741
print(ratings_copy)
# This will print {'Magnus': [2832, 2827, 2888], 'Hikaru': [2802, 2746, 2874], 'Fabiano': [2793, 2738, 2777], 'Arjun': [2778, 2671, 2741]}
print(ratings)
# This will print {'Magnus': [2832, 2827, 2888], 'Hikaru': [2802, 2746, 2874], 'Fabiano': [2793, 2738, 2777], 'Arjun': [2778, 2671, 2741]}
# Note that Arjun's rating changed in this dictionary as well. 

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}
print(classical_ratings.get('Fabiano'))
# This will print 2793
print(classical_ratings.get('Gukesh'))
# This will print None
print(classical_ratings.get('Gukesh', 'rating not found'))
# This will print 'rating not found'

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

classical_ratings.setdefault('Ian', 2767)
print(classical_ratings)
# This will print {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2793, 'Arjun': 2778, 'Ian': 2767}
classical_ratings.setdefault('Fabiano', 2900)
print(classical_ratings)
# This will print {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2793, 'Arjun': 2778, 'Ian': 2767}

word = 'armageddon'
letter_count = {}

for char in word:
	letter_count.setdefault(char, 0)
	letter_count[char] += 1

print(letter_count)
# This will print {'a': 2, 'r': 1, 'm': 1, 'g': 1, 'e': 1, 'd': 2, 'o': 1, 'n': 1}

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

chosen_rating = classical_ratings.pop('Fabiano')
print(chosen_rating)
# This will print 2793
print(classical_ratings)
# This will print {'Magnus': 2832, 'Hikaru': 2802, 'Arjun': 2778}

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

chosen_rating = classical_ratings.pop('Ian', 'rating not found')
print(chosen_rating)
# This will print 'rating not found'

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

last_rating = classical_ratings.popitem()
print(last_rating)
# This will print ('Arjun', 2778)

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

more_ratings = {'Arjun': 2780, 
					'Gukesh': 2766, 
					'Yi': 2762, 
					'Nodirbek': 2761}

classical_ratings.update(more_ratings)
print(classical_ratings)
# This will print {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2793, 'Arjun': 2780, 'Gukesh': 2766, 'Yi': 2762, 'Nodirbek': 2761}

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

more_ratings = {'Arjun': 2780, 
					'Gukesh': 2766, 
					'Yi': 2762, 
					'Nodirbek': 2761}

merged_ratings = classical_ratings | more_ratings
print(merged_ratings)
# This will print {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2793, 'Arjun': 2780, 'Gukesh': 2766, 'Yi': 2762, 'Nodirbek': 2761}
print(classical_ratings)
# This will print {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2793, 'Arjun': 2778}

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

more_ratings = {'Arjun': 2780, 
					'Gukesh': 2766, 
					'Yi': 2762, 
					'Nodirbek': 2761}

classical_ratings |= more_ratings
print(classical_ratings)
# This will print {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2793, 'Arjun': 2780, 'Gukesh': 2766, 'Yi': 2762, 'Nodirbek': 2761}

list_ratings = [['Magnus', 2832], ['Hikaru', 2802], ['Fabiano', 2793]]
print(dict(list_ratings))
# This will print {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2793}
tuple_ratings = (('Magnus', 2832), ('Hikaru', 2802), ('Fabiano', 2793))
print(dict(tuple_ratings))
# This will print {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2793}

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}

print('Caro Kann' in openings)
# This will print False

print('Sicilian' not in openings)
# This will print True

print('Berlin' in openings)
# This will print True

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings2 = {'Berlin', 'Ruy Lopez'}
print(openings2.issubset(openings))
# This will print True

print(openings2 <= openings)
# This will print True

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings2 = {'Berlin', 'Ruy Lopez'}
print(openings.issuperset(openings2))
# This will print True

print(openings >= openings2)
# This will print True

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings2 = {'Berlin', 'Ruy Lopez'}
openings3 = {'Ruy Lopez', 'Berlin'}

print(openings > openings2)
# This will print True

print(openings3 < openings)
# This will print True 

print(openings2 > openings3)
# This will print False, since the two sets are equal

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings2 = {'Berlin', 'Ruy Lopez', 'Sicilian', 'Caro Kann'}

all_openings_method = openings.union(openings2)
print(all_openings_method)
# This will print {'Caro Kann', 'Italian', 'London', 'Sicilian', 'Ruy Lopez', 'Berlin'}

all_openings_operator = openings | openings2
print(all_openings_operator)
# This will print {'Caro Kann', 'Italian', 'London', 'Sicilian', 'Ruy Lopez', 'Berlin'}

print(openings)
# This will print {'Ruy Lopez', 'London', 'Berlin', 'Italian'}
print(openings2)
# This will print {'Sicilian', 'Ruy Lopez', 'Berlin', 'Caro Kann'}
# Note that neither of these two sets were mutated. 

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings2 = {'Berlin', 'Ruy Lopez', 'Sicilian', 'Caro Kann'}

common_elements_method = openings.intersection(openings2)
print(common_elements_method)
# This will print 
common_elements_operator = openings & openings2
print(common_elements_operator)
# This will print 

print(openings)
# This will print {'Ruy Lopez', 'London', 'Berlin', 'Italian'}
print(openings2)
# This will print {'Sicilian', 'Ruy Lopez', 'Berlin', 'Caro Kann'}
# # Note that neither of these two sets were mutated. 

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings2 = {'Berlin', 'Ruy Lopez', 'Sicilian', 'Caro Kann'}

difference_method = openings.difference(openings2)
print(difference_method)
# This will print {'London', 'Italian'}

difference_operator = openings - openings2
print(difference_operator)
# This will print {'London', 'Italian'}

reversed_difference = openings2 - openings
print(reversed_difference)
# This will print {'Sicilian', 'Caro Kann'}

print(openings)
# This will print {'Ruy Lopez', 'London', 'Berlin', 'Italian'}
print(openings2)
# This will print {'Sicilian', 'Ruy Lopez', 'Berlin', 'Caro Kann'}
# Note that neither of these two sets were mutated. 

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings2 = {'Berlin', 'Ruy Lopez', 'Sicilian', 'Caro Kann'}
openings3 = {"Queen's Gambit", 'Dutch'}

print(openings.isdisjoint(openings2))
# This will print False

print(openings.isdisjoint(openings3))
# This will print True

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
copy_openings = openings.copy()
print(copy_openings)
# This will print {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
print(id(openings) == id(copy_openings))
# This will print False, since the two sets are distinct objects in memory

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings.add('Sicilian')
print(openings)
# This will print {'London', 'Berlin', 'Ruy Lopez', 'Sicilian', 'Italian'}

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings.remove('Berlin')
print(openings)
# This will print {'London', 'Ruy Lopez', 'Italian'}

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings.discard('Sicilian')
print(openings)
# This will print {'Berlin', 'London', 'Ruy Lopez', 'Italian'}

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings.clear()
print(openings)
# This will print set()

openings = {'Berlin', 'London', 'Ruy Lopez', 'Italian'}
openings.pop()
print(openings)
# You will get a random 3 element set, e.g. {'Italian', 'Ruy Lopez', 'Berlin'}

print(set('apple'))
# This will print {'a', 'p', 'l', 'e'}

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

print(set(classical_ratings))
# This wil print {'Magnus', 'Arjun', 'Hikaru', 'Fabiano'}

print(frozenset('apple'))
# This will print frozenset({'a', 'p', 'l', 'e'})

classical_ratings = {'Magnus': 2832, 
					'Hikaru': 2802, 
					'Fabiano': 2793, 
					'Arjun': 2778}

print(frozenset(classical_ratings))
# This wil print frozenset({'Magnus', 'Arjun', 'Hikaru', 'Fabiano'})