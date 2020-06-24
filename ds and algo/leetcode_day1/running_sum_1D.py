'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].'''


def runningSum(self,nums):
    new_sum = 0
    for i in range(len(nums)):
        nums[i] += new_sum
        new_sum = nums[i]
    return nums



def runningSum2(self,nums):
    check = 0
    newlist = []
    for i in range(len(nums)):
        check += nums[i]
        newlist.append(check)
    return newlist


