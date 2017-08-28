#!/usr/bin/env python

fp = file('data.txt')
lines = []
for line in fp: # 内置的迭代器, 效率很高
    lines.append(line)
    fp.close()

lines.insert(1, 'a new line') # 在第二行插入
s = '\n'.join(lines)
fp = file('data.txt', 'w')
fp.write(s)
fp.close()
