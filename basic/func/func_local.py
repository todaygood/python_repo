#!/usr/bin/python -tt 


def func(x):
	print 'x is', x
	x = 2 
	print 'change local x to', x

x = 5 
func(x)
print "x still is",x
