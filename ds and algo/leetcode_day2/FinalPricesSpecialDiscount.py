'''Given the array prices where prices[i] is the price of the ith
 item in a shop. There is a special discount for items in the shop, 
 if you buy the ith item, then you will receive a discount 
 equivalent to prices[j] where j is the minimum index such that 
 j > i and prices[j] <= prices[i], otherwise, you will not receive 
 any discount at all.

Return an array where the ith element is the final price you 
will pay for the ith item of the shop considering the special 
discount.'''


'''Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation: 
For item 0 with price[0]=8 you will receive a discount equivalent to
 prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4. 
For item 1 with price[1]=4 you will receive a discount equivalent to
 prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2. 
For item 2 with price[2]=6 you will receive a discount equivalent to
 prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4. 
For items 3 and 4 you will not receive any discount at all.'''

def finalPrice(price_list):
    ## APPROACH : STACK ##
        ## LOGIC ## 
        ## 1. Use Monotonic Increasing Stack Concept
        ## 2. Main idea is to find the Next Smaller Element in O(N) using #1
    stack = []
    for i, num in enumerate(price_list):
        while(stack and price_list[stack[-1]] >= num):
            popIndex = stack.pop()
            price_list[popIndex] -= num
        stack.append(i)
    return price_list
        

