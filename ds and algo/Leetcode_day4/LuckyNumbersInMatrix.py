'''Given a m * n matrix of distinct numbers, return all lucky 
numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the
minimum element in its row and maximum in its column.'''

'''Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum 
in its row and the maximum in its column'''

def luckyNumberInMatrix(Matrix):
    lucky_nums = []
    for i in range(len(matrix)):
        min_value = min(matrix[i])
        min_index = matrix[i].index(min_value)
        max_value = max(row[min_index] for row in matrix)
        if min_value == max_value:
            lucky_nums.append(max_value)   
        
    return lucky_nums
        









matrix = [[3,7,8],[9,11,13],[15,16,17]]

print(luckyNumberInMatrix(matrix))
        


