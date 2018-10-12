states = {
'Oregon': 'OR',
'Florida': 'FL', 'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}
# create a basic set of states and some cities in them
cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")