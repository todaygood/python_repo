#!/usr/bin/python

num = 100 

def func():
    global num 

    num = 200 
    num += 25 

    print ("in func",num) 

func()
print("after func",num) 

