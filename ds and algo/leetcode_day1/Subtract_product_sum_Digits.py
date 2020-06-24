'''
Given an integer number n, return the difference between the 
product of its digits and the sum of its digits.'''

'''Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15'''


def SubractProductAndSum(n):
    product = 1
    add = 0

    for i in (str(n)):
        product *= int(i)
        add += int(i)
    
    return (product-add)


N = 234

print(SubractProductAndSum(N))

