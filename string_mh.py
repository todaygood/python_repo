#!/usr/bin/env python

s='Hello,World'

#print (str(s))
#print repr(s)

s="let's go"
#print repr(s)

#print str(1.0/7.0)


for x in range(1,11):
	print repr(x).rjust(2),repr(x*x).rjust(3)
	print repr(x*x*x).rjust(4)


