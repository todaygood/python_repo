#!/usr/bin/env python

from functools import cmp_to_key

def cmp_ignore_case(s1,s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1 < u2:
        return -1
    elif u1 > u2:
        return 1
    else:
        return 0 

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=cmp_to_key(cmp_ignore_case)))

