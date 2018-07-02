#!/bin/python
#coding:utf-8 

'''
python中有可变对象和不可变对象，可变对象：list,dict.不可变对象有:int,string,float,tuple.
'''

def func(a):
    a["key"]= "hello"
    print("in func",a)
    
str={"key":"world"}
print(str)

func(str)

print(str)

