'''
In a array A of size 2N, there are N+1 unique elements, and exactly 
one of these elements is repeated N times.

Return the element repeated N times.'''

'''Input: [1,2,3,3]
Output: 3'''

def RepeatedElements(num_list):
    n = int(len(num_list)/2)
    for i in range(len(num_list)):
        if num_list.count(num_list[i]) == n:
            return num_list[i]


i = [1,2,3,3]

print(RepeatedElements(i))


        


    
