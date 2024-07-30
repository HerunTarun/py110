print(list(range(5)))
# This will print [0, 1, 2, 3, 4]

print(list(range(2, 5)))
# This will print [2, 3, 4]

print(list(range(1, 10, 2)))
# This will print [1, 3, 5, 7, 9]

print(list(range(10, 1, -2)))
# This will print [10, 8, 6, 4, 2]

for num in range(5):
	print(num)
# This will print 0, 1, 2, 3, 4, on separate lines

fruits = ['blueberry', 'blackberry', 'strawberry']
for (index, fruit) in enumerate(fruits):
	print(f'The {fruit} is at {index}')
# This will print:
# The blueberry is at 0
# The blackberry is at 1
# The strawberry is at 2

print(range(5).count(3))
# This will print 1

print(range(5).index(3))
# This will print 3

my_range = range(50, 10, -2)
print(my_range.start)
# This will print 50
print(my_range.stop)
# This will print 10
print(my_range.step)
# This will print -2

intro = "It was a dark and stormy night"
print(intro.index('dark'))
# This will print 9
# print(intro.index('cloudy'))
# This will raise a ValueError

intro = "It was a dark and stormy night"
print(intro.find('dark'))
# This will print 9
print(intro.find('cloudy'))
# This will print -1

star_wars = "In a galaxy far far away"
print(star_wars.count('far'))
# This will print 2

print(star_wars.count('dark'))
# This will print 0

intro = "The days were long, but the nights were longer"
print(len(intro))
print(intro.index('were', 15))
print(intro.index('were', 0, 15))

user_responses = "The first line is a mess.\nBut the second line is no better"
cleaned_responses = user_responses.replace('\n', ' ')
print(cleaned_responses)

string = 'Bonjour'
print(string.upper())
# This will print BONJOUR

string = 'WHAM'
print(string.lower())
# This will print wham

string = "Weiß"
casefolded = string.casefold()
print(casefolded)
# This will print weiss

home_city = 'berlin'
print(home_city.capitalize())
# This will print Berlin

color = 'Weiß'
print(color.swapcase())
# This will print wEISS
print(color.swapcase().swapcase())
# This will print Weiss

accessories = ['charger', 'phone', 'headphones']
print(', '.join(accessories))
# This will print charger, phone, headphones

numbers = [1, 2, 3, 4, 5]
new_numbers = ', '.join([str(num) for num in numbers])
print(new_numbers)
# This will print 1, 2, 3, 4, 5

statement = "Dreamcatcher is a kpop group  but so is Twice"
print(statement.split(' '))
print(statement.split())

statement = "Dreamcatcher is a kpop group  but so is Twice"
print(statement.split(' ', 4))
# This will print ['Dreamcatcher', 'is', 'a', 'kpop', 'group  but so is Twice']

kpop_group = 'Dreamcatcher'
print(list(kpop_group))
# This will print ['D', 'r', 'e', 'a', 'm', 'c', 'a', 't', 'c', 'h', 'e', 'r']

string = '   Blasted words    '
print(string.strip())
# This will print 'Blasted words'
print(string.rstrip())
# This will print '   Blasted words'
print(string.lstrip())
# This will print 'Blasted words   '

string = 'Duck and weave'
print(string.startswith('Duck'))
# This will print True
print(string.endswith('weave'))
# This will print True

print('straße'.isalpha())
# This will print True

print(str([1, 2, 3]))
# This will print [1, 2, 3]

print(str(123))
print(str(12.5))
print(str(None))
print(str((1, 2, 3)))
print(str({'name': 'John', 'age': 42}))

name = "Dreamcatcher"
for char in name:
	print(char)
# This will print each letter on a separate line
index = 0
while index < len(name):
	print(name[index])
	index += 1
# This will print each letter on a separate line