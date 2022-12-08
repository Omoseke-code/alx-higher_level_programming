#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    add, add2 = 0, 0
    for x, y in my_list:
        mul = x * y
        add += mul
        add2 += y
    result = add / add2
    return result
