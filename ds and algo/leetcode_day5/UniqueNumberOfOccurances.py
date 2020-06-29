'''
Given an array of integers arr, write a function that returns true if
 and only if the number of occurrences of each value in the array is 
unique.'''

'''Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1.
No two values have the same number of occurrences.'''
class Solution:
    def uniqueOccurrences(self, arr):
        nums = {}
        # Create and add to dictionary
        for index in arr:
            if index not in nums:
                nums[index] = 1
            else:
                nums[index] += 1

        """
        Add all values (number of occurences) of dictionary into an array.
        If there are duplicates, if statement will return false. If no
        duplicates, the else statement will never be executed. Thus we
        eventually return true.
        """
        check = []
        for key, value in nums.items():
            if value not in check:
                check.append(value)
            else:
                return False

        return True 



