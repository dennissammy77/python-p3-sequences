#!/usr/bin/env python3

def print_fibonacci(length):
    int_list = list()
    
    # first two terms
    n1, n2 = 0, 1
    count = 0
    
    while count < length:
       int_list.append(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
    pass
    print(int_list)

print_fibonacci(9)