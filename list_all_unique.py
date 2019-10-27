#!/usr/bin/python


def all_unique(list):
    return len(list) == len(set (list)) 


x = [1,2,3,4,5,6]
y = [1,2,2,3,4,5]

print(all_unique(x)) # True
print(all_unique(y)) # False

