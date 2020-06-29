'''
Given an array A of non-negative integers, half of the integers in A are 
odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] 
is even, i is even.

You may return any answer array that satisfies this condition.'''

'''Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been 
accepted.'''

def SortArrayByParity(A):
    arr1 = [x for x in A if x %2 ==0]
    arr2 = [x for x in A if x %2 ==1]
    answer = list()
    for i in range(int(len(A)/2)):
        answer.append(arr1[i])
        answer.append(arr2[i])
        
    return answer
