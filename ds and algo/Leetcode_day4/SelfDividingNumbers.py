def SelfDividingNumbers(left,right):
    output_list = []

    for i in range(left,right+1):
        
        num = i
        flag = 0

        while i >0:
            last_digit = i%10
            

            if last_digit != 0:
                if num%last_digit != 0:
                    flag = 1
                    print(last_digit,num)
                    break
            else:
                flag = 1
                break
            i = i//10
        if flag == 0:    
            output_list.append(num)
                   
        
    return output_list


left = 1
right = 22

print(SelfDividingNumbers(left,right))            

