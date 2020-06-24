'''Implement function ToLowerCase() that has a string parameter 
str, and returns the same string in lowercase.'''

'''Input: "Hello"
Output: "hello"
'''

def ToLowerCase(s):
    new_str = ''

    for char in s:
        if 64<ord(char)<91:
            new_str += chr(ord(char)+32)
        
        else:
            new_str +=char

    return new_str
