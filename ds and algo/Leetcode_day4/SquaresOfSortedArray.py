'''Given an array of integers A sorted in non-decreasing order,
 return an array of the squares of each number, also in sorted 
non-decreasing order.'''

'''Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]'''

def SortedSquares(input):
    OutputList = sorted(number**2 for number in input)

    return OutputList

input = [-4,-1,0,3,10]
print(SortedSquares(input))
