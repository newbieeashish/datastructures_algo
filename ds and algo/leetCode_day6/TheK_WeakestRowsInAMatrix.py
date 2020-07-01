'''
Given a m * n matrix mat of ones (representing soldiers) and zeros 
(representing civilians), return the indexes of the k weakest rows in the 
matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less
than the number of soldiers in row j, or they have the same number of 
soldiers but i is less than j. Soldiers are always stand in the frontier 
of a row, that is, always ones may appear first and then zeros.'''

'''
Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]'''

def kweakestRow(mat,k):
    soldiers_count = []
    result = []
    for i in range(len(mat)):
        soldiers_count.append(sum(mat[i]))
    weakest = dict(zip((range(len(soldiers_count))),soldiers_count))
    weakest = sorted(weakest.items(), key = lambda x:x[1])
    for i in range(k):
        result.append(weakest[i][0])

    return result    


