#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    else:
        maxN = my_list[0]
        for i in range(len(my_list)):
             if maxN < my_list[1]:
                 maxN = my_list[1]
        return maxN
