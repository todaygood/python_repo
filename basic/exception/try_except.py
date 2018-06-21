#!/usr/bin/env python

try:
    fh=open("testfile","r+")
    fh.write("测试文件，用于测试异常")
except IOError:
    print("Error:没有找到文件或者读取文件")
else:
    print("写入成功")
    fh.close()




