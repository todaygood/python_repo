#!/usr/bin/python

from __future__ import print_function 

string = 'abcdafg'
newstr = list(string)

newstr[4] = 'e'

print(string, ''.join(newstr), sep='\n')

# join 将interable对象变成string

