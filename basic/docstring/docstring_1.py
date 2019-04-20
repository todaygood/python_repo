#!/usr/bin/env python
# -*- coding: utf-8 -*-
#模块的docstring
"""这是一个测试模块"""

import os


def this_test():
    #  函数的docstring
    """一个测试的方法"""
    print "this is a test!"


if __name__ == "__main__":
    this_test()

'''
hujun@jun:/Code/repository/python> python docstring_1.py 
this is a test!
hujun@jun:/Code/repository/python> python
Python 2.7.3 (default, Apr 14 2012, 08:58:41) [GCC] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import docstring_1
>>> help(docstring_1)

Help on module docstring_1:

NAME
    docstring_1 - 这是一个测试模块

FILE
    /Code/repository/python/docstring_1.py

FUNCTIONS
    this_test()
        一个测试的方法
'''
