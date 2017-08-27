#!/usr/bin/env python

# this is a program in python3.4

s="你好"  #unicode

print(s)

s_gbk=s.encode("gbk") #convert to gbk
print(s_gbk)

print(s.encode()) #convert to utf-8

gbk_to_utf8=s_gbk.decode("gbk").encode("utf-8")
print(gbk_to_utf8)



