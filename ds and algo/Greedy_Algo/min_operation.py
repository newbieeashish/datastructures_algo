'''Min Operations
Starting from the number 0, find the minimum number of operations 
required to reach a given positive target number. You can only use 
the following two operations:

1. Add 1
2. Double the number'''

'''For Target = 18, output = 6, because it takes at least 6 steps 
shown below to reach the target

start = 0
step 1 ==> 0 + 1 = 1
step 2 ==> 1 * 2 = 2 # or 1 + 1 = 2
step 3 ==> 2 * 2 = 4
step 4 ==> 4 * 2 = 8
step 5 ==> 8 + 1 = 9
step 6 ==> 9 * 2 = 18'''

def min_operation(target: int) -> int:
    steps = 0
    while target != 0:
        while (target/2) == (target//2):
            target = target //2 
            steps +=1
        
        target -=1
        steps +=1
    
    return steps


# Test Cases

def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operation(target)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


target = 18
solution = 6
test_case = [target, solution]
test_function(test_case)