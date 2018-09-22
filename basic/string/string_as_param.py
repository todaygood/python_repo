#!/usr/bin/python 

def do_something(str):
    print("in do_something:",id (str))
    str= str.upper()

a = "hello,world!"

print (id (a)) 
do_something(a)

print (id (a))

print (a) 


'''
在python 中，函数传参都是传object的引用， 要看这个object是可变对象还是不可变对象。

https://blog.csdn.net/zhuzuwei/article/details/80529712

不可变对象有： string 和tuple.

'''

