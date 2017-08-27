#!/usr/bin/env python

def f(x):
	return x%3 ==0 or x%5 ==0 

print filter(f,range(2,35))


