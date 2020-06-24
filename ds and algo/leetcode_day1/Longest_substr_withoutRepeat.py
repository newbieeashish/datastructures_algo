
'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. '''

def longest_substring(self,s):
    dict = {}
    max_length = start = 0

    for i, char in enumerate(s):
        if char in dict:
            sums = dict[char] + 1
            if sums > start:
                start = sums
        num = i-start+1
        if num > max_length:
            max_length = num
        dict[char] = i
    return max_length
