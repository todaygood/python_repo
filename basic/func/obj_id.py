#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'ZhangHe'

def reverse(s):
    print id(s)
    t = ''
    r = len(s) - 1
    while r>=0:
        t = t + s[r]
        r -= 1
    return t

s = 'abasdfasdfcdabasdfasdfcd'

print(s)
print id(s)
print reverse(s)


