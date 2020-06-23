'''
Caching can be defined as the process of storing data into a temporary 
data storage to avoid recomputation or to avoid reading the data from a 
relatively slower part of memory again and again. Thus cachig serves as a 
fast "look-up" storage allowing programs to execute faster.

Let's use caching to chalk out an efficient solution for a problem.'''


'''
Problem Statement
A child is running up a staircase with and can hop either 1 step, 2 steps or 3 steps at a time. If the staircase has n steps, write a function to count the number of possible ways in which child can run up the stairs.

For e.g.

n == 1 then answer = 1

n == 3 then answer = 4

n == 5 then answer = 13'''

def staircase(n):
    if n == 0:
        return 1
    
    elif n<0:
        return 0 
    
    else:
        climb_ways = 0
        climb_ways += staircase(n-1)
        climb_ways += staircase(n-2)
        climb_ways += staircase(n-3)

        return climb_ways
    
def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")
    
test_case = [4, 7]
test_function(test_case)


'''
Problem Statement
While using recursion for the above problem, you might have noticed a small problem with efficiency.

Let's take a look at an example.

Say the total number of steps are 5. This means that we will have to call at (n=4), (n=3), and (n=2)

To calculate the answer for n=4, we would have to call (n=3), (n=2) and (n=1)

You can notice that even for a small number of staircases (here 5), we are calling n=3 and n=2 multiple times. Each time we call a method, additional time is required to calculate the solution. In contrast, instead of calling on a particular value of n again and again, we can calculate it once and store the result to speed up our program.

Your job is to use any data-structure that you have used until now to write a faster implementation of the function you wrote earlier while using recursion.'''


import functools



'''https://docs.python.org/3.3/library/functools.html'''
@functools.lru_cache(maxsize=None)
def staircase1(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        climb_ways = 0
        climb_ways += staircase1(n - 1)
        climb_ways += staircase1(n - 2)
        climb_ways += staircase1(n - 3)

        return climb_ways
    

test_case = [4, 7]
test_function(test_case)