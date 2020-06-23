'''
Given an input string, return all permutations of the string in an array.

Example 1:

string = 'ab'
output = ['ab', 'ba']
Example 2:

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
'''

def permutations(l):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    if len(l) <= 1:
        return [l]

    elif len(l) == 2:
        return [l, l[::-1]]

    else:
        output = []
        current_level = l[0]
        prev_level = permutations(l[1:])

        for element in prev_level:  # For each answer from previous level
            for pos in range(len(element) + 1):  # For each possible position to put this level value
                temp_list = ''
                temp_element = element
                for i in range(len(element) + 1):
                    if pos == i:
                        temp_list += current_level
                    else:
                        temp_list += temp_element[0]
                        temp_element = temp_element[1:]
                        
                output.append(temp_list)
        return output
    
def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")
    
string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)