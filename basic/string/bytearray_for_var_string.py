#!/bin/python
'''
http://hgoldfish.com/blogs/article/61/
'''

ba=bytearray(b"fish is here")

print(ba)
ba[2]='5'
print(ba)


str="hello"
str2=str.replace('l','o')
print(id(str),id(str2))
print(str2)
