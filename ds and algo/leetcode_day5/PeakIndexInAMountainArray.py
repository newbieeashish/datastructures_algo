'''
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that
 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i 
such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].'''

'''Input: [0,1,0]
Output: 1'''

def peakIndexInMountainArray(A):
    indexs = A.index(max(A))
    
    return indexs+1


#solution 2

'''return [i for i in range(len(A)-1) if A[i+1] < A[i]][0]'''


