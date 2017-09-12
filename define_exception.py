#!/usr/bin/env python

def functionName(level):
    if level < 1:
        raise Exception("Invalid level!",level)

try:
    functionName(0) 
except "Invalid level!":
    print(1)
else :
    print(2)
