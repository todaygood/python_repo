#!/usr/bin/python3

import os 

print("use os.popen,return file object")

str1 = os.popen("ls -alh").read()

a = str1.split("\n")

print(a)
