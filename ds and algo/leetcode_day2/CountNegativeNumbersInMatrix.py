'''
Given a m * n matrix grid which is sorted in non-increasing 
order both row-wise and column-wise. 

Return the number of negative numbers in grid.'''

'''Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.'''

def NegativeNumberInMatrix(numbers_grid):
    total = 0

    for number_list in numbers_grid:
        for number in number_list:
            if number <0:
                total +=1
    
    return total

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(NegativeNumberInMatrix(grid))
