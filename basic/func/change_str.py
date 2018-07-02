#!/bin/python


def func(string):
    string= "hello"
    print("in func",string)
    return id(string)
    
str="world"
print(str)

str = func(str)

print(str)

