#!/usr/bin/python

a=[1,3,4]

def func():
    a.append(5)

    print("in func",a)

print("before func",a)
func()
print("after func",a)
