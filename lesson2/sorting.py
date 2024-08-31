print(sorted([5, 7, 3, 4, 1, 7, 4, 24]))

games = ['chess', 'checkers', 'go']
sorted_games = sorted(games, key=len)
print(sorted_games)

people = [("Jack", 30), ("John", 25), ("Betty", 25), ("Anna", 30)]
sorted_people = sorted(people)
print(sorted_people)
# Expected output: [('Betty', 25), ('John', 25), ('Anna', 30), ('Jack', 30)]
# Actual output:   [('Anna', 30), ('Betty', 25), ('Jack', 30), ('John', 25)]

def sort_by_age(people):
	name, age = people
	return (age, name)

sorted_people = sorted(people, key= sort_by_age)
print(sorted_people)