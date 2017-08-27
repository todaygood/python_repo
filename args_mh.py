#!/usr/bin/env python
# -*- coding:utf-8 -*-

def test0(x,y):
	'''function test0 '''
	print('x=%d,y=%d\n'%(x,y))

def test1(x,y,z):
	'''function test1 '''
	print('x=%d,y=%d,z=%d\n'%(x,y,z))

#位置参数调用
#test0(3,5)

# 关键字调用
a=3
b=5

#test0(y=a,x=b)
#test0(3,y=a)

#test0(3,x=a)
#TypeError: test1() got multiple values for keyword argument 'x'

#test1(3,y=2,3)
# SyntaxError: non-keyword arg after keyword arg 


#def test2(x,y=2):
#	print("x=%d,y=%d\n"%(x,y)) 
#
#print test2(3,10)
#print test2(3)

# *args 参数组，把位置参数转化为tuple

def test5(*args):
	print(args)

def test6(x,*alex):
	print(x)
	print(alex)

#test5(1,2,5,6,7)
#test5(*[1,2,3,4,5,6])

#test6(1,2,3,4)

# **kwargs 参数组， 把关键字参数转化为字典
def test7(**kwargs):
	print(kwargs)
	print(kwargs['name'])

#test7(name='alex',age=8,sex='Female')

#test7(**{'name':'alex','age':8,'sex':'Female'})

def test8(name,**kwargs):
	print(name)
	print(kwargs)

#test8('alex')
#test8('alex',age=8,sex='Female')

def test9(name,age=18,**kwargs):
	print(name)
	print(age)
	print(kwargs)

#test9('alex',age=8,sex='Female',hobby='Telsna')
#test9('alex',sex='Female',hobby='Telsna',age=10)

def test10(name,age=18,*args,**kwargs):
	print(name)
	print(age)
	print(args)
	print(kwargs)

test10('alex',age=34,sex='Female',hobby='Telsna')







