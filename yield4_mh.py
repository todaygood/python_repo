#!/usr/bin/env python

def echo(value=None):
    while 1:
        value = (yield value)
        print("The vlaue is ",value)
        if value:
            value +=1

g=echo(1)
next(g)

g.send(2)

g.send(5)

next(g)



