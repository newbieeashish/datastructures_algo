'''Given an integer n, return any array containing n unique
integers such that they add up to 0.'''

'''Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] ,
[-3,-1,2,-2,4].'''


def uniqueIntegers(n):

    mid = n//2
    result = list(range(-mid,mid+1))
        
    if n%2 == 0:
        result.remove(0)

    return result

    







