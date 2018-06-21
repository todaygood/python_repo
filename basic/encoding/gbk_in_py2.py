#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

print sys.getdefaultencoding()

s="你好"

s_to_gbk=s.encode("gbk")

s_to_unicode=s.decode("utf-8")
print s_to_unicode,type(s_to_unicode)

#s_to_gbk=s.decode("utf-8").encode("gbk")
#print s_to_gbk
#print("你好")



