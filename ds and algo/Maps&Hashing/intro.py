'''
In Python, the map concept appears as a built-in data type called a dictionary.
 A dictionary contains key-value pairs. Dictionaries might soon become your 
 favorite data structure in Python—they're extremely easy to use and useful.
 Here's a sample of setting up a dictionary.'''

dictionary = {}
dictionary['d'] = [1]
dictionary['i'] = [2]
dictionary['c'] = [3]
dictionary['t'] = [4]
dictionary['i'].append(5)
dictionary['o'] = [6]
dictionary['n'] = [7]
dictionary['a'] = [8]
dictionary['r'] = [9]
dictionary['y'] = [10]
print (dictionary)

# Code

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore'], 'China': ['Shanghai']}
locations['Africa'] = {'Egypt': ['Cairo']}

# TODO: Print a list of all cities in the USA in alphabetic order.
usa_loc = locations['North America']['USA']
usa_loc.sort()
print(usa_loc)

# TODO: Print all cities in Asia, in alphabetic order, next to the name of the country
asia_loc = locations['Asia']
asia_loc_list = [element + '-' + str(*asia_loc['India']) for element in asia_loc]
asia_loc_list.sort()
print(asia_loc_list)