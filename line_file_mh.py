#!/usr/bin/env python

file = open('README.md','r')

for (num,value) in enumerate(file):
    print( "line number",num,"is:",value)



#compute total line of a file
print(len(file.readlines()))


file.close()
