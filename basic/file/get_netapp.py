#!/usr/bin/env python

with open("netapp.txt",'r') as file:
    for line in file.readlines():
        if line.find("_sas") >=0 :
            print("line is",line)
            print(line.split(" ")[1])

