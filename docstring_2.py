#!/usr/bin/env python
# -*- coding: utf-8 -*-
#模块的docstring
"""还是一个test模块，只针对rhel 6+、centos 6+平台
空一行
   公共返回值
   @return: status=INT, #执行状态，0=成功，非0=错误，错误信息在msgs中。
            msgs=STRING,#执行错误的时候，返回的错误信息
            results=INT/STRING/LIST/TUPLE/DICT, #执行结果
空一行
"""
__version__ = '0.1'
__author__ = [
    "Longgeek ",
]
TEST_CONF = "/etc/test.conf"
TEST_PID = "/var/test.pid"

def test_status(a='', b=''):
    #函数的docstring
    """查看test的状态
    a: 参数a
    b: 参数b
    空一行
    """
    print 'test only'

