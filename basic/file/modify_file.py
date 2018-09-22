#!/usr/bin/env python
# coding: utf-8 

'''
Purpos: read a file , and insert a new line , write them into a new file
'''

fp = open('data.txt', 'r')
lines = []

for line in fp: # 内置的迭代器, 效率很高
    print(line)
    lines.append(line)

fp.close()

lines.insert(1, 'a new line\n') # 在第二行插入

# python合并list为字符串,ref https://blog.csdn.net/Zx_whu/article/details/61926655
s = ''.join(lines)

fp = open('data2.txt', 'w')

fp.write(s)

fp.close()

