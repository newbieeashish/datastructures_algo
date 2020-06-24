'''
Given a non-negative integer num, return the number of steps to 
reduce it to zero. If the current number is even, you have to divide
by 2, otherwise, you have to subtract 1 from it.'''


'''Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.'''

def Steps(num):
    total_step = 0
    while num!=0:
        if num%2 == 0:
            num = num/2
            total_step +=1
        else:
            num -=1
            total_step+=1
    
    return total_step

print(Steps(14))

