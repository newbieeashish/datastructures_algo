def srting_rev(input_str):

    rev_string = ''

    for i in range(len(input_str)):
        rev_string += input_str[(len(input_str)-1)-i]

    return rev_string

# Test Cases

print ("Pass" if ('retaw' == srting_rev('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == srting_rev('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == srting_rev('The house code is: 2343')) else "Fail")
