'''Balanced strings are those who have equal quantity of 'L' and 'R'
 characters.

Given a balanced string s split it in the maximum amount of 
balanced strings.

Return the maximum amount of splitted balanced strings.

'''
'''
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each
substring contains same number of 'L' and 'R'.'''

def balancedStringSplit(s):
    number_of_splits = 0
    word_count = 0

    for i in range(len(s)):
        if s[i] == 'L':
            word_count +=1
        else:
            word_count -=1
        
        if word_count ==0:
            number_of_splits +=1
        
    return number_of_splits

s = 'RLRRLLRLRL'

print(balancedStringSplit(s))


