'''A valid parentheses string is either empty (""), "(" + A + ")",
 or A + B, where A and B are valid parentheses strings, and + 
 represents string concatenation.  For example, "", "()", "(())()",
  and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and 
there does not exist a way to split it into S = A+B, with A and B
nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive 
decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive 
valid parentheses strings.

Return S after removing the outermost parentheses of every 
primitive string in the primitive decomposition of S.'''

'''Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive 
decomposition "(()())" + "(())".
After removing outer parentheses of each part, this 
is "()()" + "()" = "()()()".'''

def removeOuterParatheses(s):
    new_bracket_string = ''
    count = 0

    for bracket in s:
        if bracket == ')':
            count -=1

        if count:
            new_bracket_string += bracket

        if bracket == '(':
            count +=1
        
       
    return new_bracket_string

trying = "(()())(())"

print(removeOuterParatheses(trying))

