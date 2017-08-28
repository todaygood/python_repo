#!/usr/bin/env python

def add(a,b,f):
	return f(a)+f(b)


print(add(3,-5,abs))

