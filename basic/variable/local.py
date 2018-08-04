#!/usr/bin/python

num = 100 

def func():
    num = 123 
    print ("in func:",num) 

print ("call func before", num) 
func()
print ("call func after", num) 

