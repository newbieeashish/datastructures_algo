'''
You are given the array paths, where paths[i] = [cityAi, cityBi]
 means there exists a direct path going from cityAi to cityBi. 
 Return the destination city, that is, the city without any path 
 outgoing to another city.

It is guaranteed that the graph of paths forms a line without any 
loop, therefore, there will be exactly one destination city.'''

'''
Input: paths = [["London","New York"],["New York","Lima"],
["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" 
city which is the destination city. Your trip consist 
of: "London" -> "New York" -> "Lima" -> "Sao Paulo".'''

def Destination(paths):
    cities = {}

    for path in paths:
        cities[path[0]] = path[1]
    
    for path in paths:
        if path[1] not in cities:
            return path[1]


paths = [["B","C"],["D","B"],["C","A"]]

print(Destination(paths))


