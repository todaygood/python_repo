#!/usr/bin/env python

# 用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。


def f(x):
	return x%3 ==0 or x%5 ==0 

a=filter(f,range(2,35))
for i in a:
    print(i)


def odd(x):
    return x%2 !=0 

b=(filter(odd,range(1,100))) 
for i in b:
    print(i)
