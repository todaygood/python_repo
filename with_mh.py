#!/usr/bin/env python

import time

def logger():
	time_format='%Y-%m-%d %H:%M:%S'
	now = time.strftime(time_format,time.gmtime())
	with open('/tmp/a.txt','a+') as f:
		f.write('%s end action\n'% now)

def test1():
	print "in the test1"
	logger()

def test2():
	print "in the test2"
	logger()

def test3():
	print "in the test3"
	logger()


test1()
test2()
test3()
