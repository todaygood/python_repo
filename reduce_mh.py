#!/usr/bin/env python

from functools import reduce 

def add(x,y):
	return x+y

a=reduce(add,range(11))
print(a)


'''
reduce函数的定义：
reduce(function, sequence[, initial]) -> value
function参数是一个有两个参数的函数，reduce依次从sequence中取一个元素，和上一次调用function的结果做参数再次调用function。

'''




