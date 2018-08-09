#!/usr/bin/python
# coding:utf-8

# 使用这种方式进行字符串连接的操作效率低下，因为python中使用 + 拼接两个字符串时会生成一个新的字符串，生成新的字符串就需要重新申请内存，当拼接字符串较多时自然会影响效率。

s="hello"+ " world!"

print(s) 


