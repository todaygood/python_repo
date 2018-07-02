#!/usr/bin/env python

file = open("score.txt")

for line in file.readlines():
    print(line.strip("\n"))
    value = line.split()
    #print(value)
    print ("%s's score is %s"%(value[0],value[1]))
