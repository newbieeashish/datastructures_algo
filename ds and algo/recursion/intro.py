#power of 2

def power_of_2(n):
    if n == 0:
        return 1
    
    return 2 * power_of_2(n-1)

print(power_of_2(5))

#factorial using rec

def fact(n):
    if n<=1:
        return 1
    
    return n*fact(n-1)

print (fact(5))