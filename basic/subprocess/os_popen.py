#!/usr/bin/python
#coding:utf-8

#Python 2和3中最有效的方法: cmdline是字符串的形式

import os 

print("use os.popen,return file object")

str1 = os.popen("ls -alh").read()

a = str1.split("\n")

for one in a:
    print(one)
