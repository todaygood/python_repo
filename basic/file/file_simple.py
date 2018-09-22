#!/usr/bin/env python

fp = open('data.txt', 'r')
lines = []

for line in fp: # 内置的迭代器, 效率很高
    print(line)
    lines.append(line)

fp.close()

lines.insert(1, 'a new line') # 在第二行插入

s = '\n'.join(lines)

fp = open('data2.txt', 'w')

fp.write(s)

fp.close()
