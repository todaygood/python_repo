#!/usr/bin/env python

import time

def logger():
#	time_format='%Y-%m-%d %H:%M:%S'
	time_format='%Y-%m-%d %X'
	now = time.strftime(time_format,time.gmtime())
	with open('/tmp/a.txt','a+') as f:
		f.write('%s end action\n'% now)

def test1():
	print "in the test1"
	logger()

def test2():
	print "in the test2"
	logger()
	return test1

def test3():
	print "in the test3"
	logger()
	return 0,'hello',['a','b','c'],{'name':'alex'}



test1()

print test2()

res_t3=test3()
print res_t3
