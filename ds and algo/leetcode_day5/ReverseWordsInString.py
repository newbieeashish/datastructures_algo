'''Given a string, you need to reverse the order of characters in each 
word within a sentence while still preserving whitespace and initial 
word order.'''

'''Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"'''

def ReverseWordsInString(s):
    
    return ' '.join([w[::-1] for w in s.split()])


Input = "Let's take LeetCode contest"
print(ReverseWordsInString(Input))