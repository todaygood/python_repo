#!/usr/bin/env python

#这段代码
def calc(n):
    return n**n

print(calc(10))
	 
#换成匿名函数

calc = lambda n:n**n
print(calc(10))
