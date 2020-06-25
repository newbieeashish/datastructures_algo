'''Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most 
one digit (6 becomes 9, and 9 becomes 6).'''

'''Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.'''

def Max69Number(num):
    a=[i for i in str(num).strip('[]')]
    list1=[]
    b="".join(a)
    list1.append(int(b))
    for i in range(len(a)):
        if a[i]=='6':
            a[i]='9'
            b="".join(a)
            if int(b) not in list1:
                list1.append(int(b))
            a[i]='6'
        elif a[i]=='9':
            a[i]='6'
            b="".join(a)
            if int(b) not in list1:
                list1.append(int(b))
            a[i]='9'
    return(max(list1))

    

