#!/usr/bin/env python
# -*- coding:utf-8 -*-
def test0(x,y,z):
	'''function test0 '''
	print('x=%d,y=%d\n'%(x,y,z))

def test1(x,y,z):
	'''function test1 '''
	print('x=%d,y=%d,z=%d\n'%(x,y,z))

#位置参数调用
#test0(3,5)

# 关键字调用
a=3
b=5

#test0(y=a,x=b)
test0(3,y=a)

#test0(3,x=a)
#TypeError: test1() got multiple values for keyword argument 'x'

#test1(3,y=2,3)
# SyntaxError: non-keyword arg after keyword arg 


