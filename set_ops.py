#!/usr/bin/env python

a=[1,3,5,7,8,15]
b=[3,6,8,9,10]

set_a = set(a)
set_b = set(b) 

#print set_a.union(set_b)
#print set_a | set_b
#
#
#print set_a ^ set_b 



set_a.add(699)
print set_a

if 699 in set_a :
	set_a.remove(699)
	print set_a




