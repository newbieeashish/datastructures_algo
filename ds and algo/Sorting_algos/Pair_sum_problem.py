'''
Given an input array and a target value (integer), find two values
 in the array whose sum is equal to the target value. Solve the 
 problem without using extra space. You can assume the array has
  unique values and will never have more than one solution.'''


def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    Return the two numbers in the form of a sorted list
    """

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                if arr[i] > arr[j]:
                    return [arr[j], arr[i]]
                else:
                    return [arr[i], arr[j]]

    return [None, None]

    
def test_function(test_case):
    input_list = test_case[0]
    target =test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")

input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)