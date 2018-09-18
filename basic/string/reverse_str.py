#!/usr/bin/python

__author__ = 'Hujun'

def reverse(s):
    t= ''
    r=len(s)-1
    while(r>=0):
        t = t+s[r]
        r -= 1

    return t 

s = 'abcd'

print(reverse(s))
