lst = [[1, 2], 3, 4]
print(lst[0]) # [1, 2]
print(lst[0][0]) # 1

lst[0][1] = 5
print(lst[0]) # [1, 5]
print(lst[0][1]) # 5

lst = [[1], [2]]
lst[0].append(3)
print(lst) # [[1, 3], [2]]

lst = [[1], [2]]
lst[0].append([3, 4])
print(lst) #[[1, [3, 4]], [2]]
print(lst[0][1][1]) # 4

classical_ratings = [{'Magnus': 2832}, {'Hikaru': 2802}]
classical_ratings[0]['Fabiano'] = 2797
print(classical_ratings) 
# [{'Magnus': 2832, 'Fabiano': 2797}, {'Hikaru': 2802}]

groups = [
		  ('Tristan', 'Angharad'), 
		  {'Magnus': 2832, 'Hikaru': 2802},
		  {42, 666, 3.14},
		  frozenset(['water', 'fire', 'earth', 'wind'])
		  ]
# Accessing elements
print(groups[0][0]) # Tristan
print(groups[1]['Hikaru']) # 2802
print(groups[2]) # {42, 666, 3.14}
print(groups[3]) # frozenset({'water', 'fire', 'earth', 'wind'})

# Modifying mutable collections
groups[1]['Fabiano'] = 2797
groups[2].add(2.718)

# Reassigning immutable collections
groups[0] = ('Tristan', 'Angharad', 'Maryam')
groups[3] = frozenset(['ice', 'plasma', 'lava', 'space'])

print(groups)

groups = (
		  ('Tristan', 'Angharad'), 
		  {'Magnus': 2832, 'Hikaru': 2802},
		  {42, 666, 3.14},
		  frozenset(['water', 'fire', 'earth', 'wind'])
		  )
print(groups[0][0]) # Tristan
print(groups[1]['Hikaru']) # 2802
print(groups[2]) # {42, 666, 3.14}
print(groups[3]) # frozenset({'water', 'fire', 'earth', 'wind'})

# Modifying mutable collections
groups[1]['Fabiano'] = 2797
groups[2].add(2.718)

# Reassigning immutable collections
# groups[0] = ('Tristan', 'Angharad', 'Maryam')
# groups[3] = frozenset(['ice', 'plasma', 'lava', 'space'])

print(groups)

dict1 = {
    "numbers":     [42, 3.14],
    "coordinates": ('x', 'y'),
    "details":     {"age": 45, "weight": 140},
    "items":       {'tent', 'compass'},
    "triforce":     frozenset(['courage', 'power']),
}
dict1['numbers'].append(2.718)
dict1['coordinates'] = ('x', 'y', 'z')
dict1['details']['height'] = 170
dict1['items'].add('lantern')
dict1['triforce'] = frozenset(['courage', 'power', 'bravery'])
print(dict1)

valid_set = {1, 2, (3, 4), frozenset([5, 6])}
valid_set.add(7)
print(valid_set)

valid_frozenset = frozenset([8, 9, (10, 11), frozenset([13, 14])])

a = [1, 2]
b = [3]
lst = [a, b]
print(a) # [1, 2]
print(b) # [3]
print(lst) # [[1, 2], [3]]

a.append(5)
print(a) # [1, 2, 5]
print(lst) # [[1, 2, 5], 3]

lst[0][1] = 15
print(lst) # [[1, 15, 5], 3]
print(a) # [1, 15, 5]

word = str('twice')
another_word = str(word)
print(id(word) == id(another_word))

my_frozenset = frozenset(['water', 'fire', 'earth', 'wind'])
another_frozenset = frozenset(my_frozenset)
last_frozenset = frozenset(['water', 'fire', 'earth', 'wind'])
print(my_frozenset, another_frozenset, last_frozenset)
print(id(my_frozenset) == id(my_frozenset))
print(id(my_frozenset) == id(last_frozenset))

copy_frozenset = my_frozenset.copy()
print(copy_frozenset)
print(id(copy_frozenset) == id(my_frozenset))

ratings = {'Magnus': [2832, 2827, 2888],
					'Hikaru': [2802, 2746, 2874], 
					'Fabiano': [2793, 2738, 2777], 
					'Arjun': [2778, 2671, 2740]}

ratings_copy = ratings.copy()

print(id(ratings) == id(ratings_copy))

name = ['t', 'w', 'i', 'c', 'e']
new_name = list(name)
print(new_name) # ['t', 'w', 'i', 'c', 'e']
print(id(name) == id(new_name)) # False

name = ['t', 'w', 'i', 'c', 'e']
new_name = name[:]
print(new_name) # ['t', 'w', 'i', 'c', 'e']
print(id(name) == id(new_name)) # False

name = ['t', 'w', 'i', 'c', 'e']
new_name = name.copy()
print(new_name) # ['t', 'w', 'i', 'c', 'e']
print(id(name) == id(new_name)) # False

import copy
name = ['t', 'w', 'i', 'c', 'e']
new_name = copy.copy(name)
print(new_name) # ['t', 'w', 'i', 'c', 'e']
print(id(name) == id(new_name)) # False

top_3 = {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2797}
new_top_3 = dict(top_3)
print(new_top_3) 
# {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2797}
print(id(top_3) == id(new_top_3)) # False

top_3 = {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2797}
new_top_3 = top_3.copy()
print(new_top_3) 
# {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2797}
print(id(top_3) == id(new_top_3)) # False

top_3 = {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2797}
new_top_3 = copy.copy(top_3)
print(new_top_3) 
# {'Magnus': 2832, 'Hikaru': 2802, 'Fabiano': 2797}
print(id(top_3) == id(new_top_3)) # False