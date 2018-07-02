#!/bin/python
"""http://lazybios.com/2013/04/four-kinds-of-function-argment-pass-in-python/"""

def test(x,y=5,*a,**b):
    print x,y,a,b

test(1)
test(1,2)
test(1,2,3)
test(1,2,3,4)

test(x=1)
test(x=1,y=1)
test(x=1,y=1,a=1)
test(x=1,y=1,a=1,b=1)


test(1,y=1)
#test(1,2,y=1)
test(1,2,3,4,a=1)
test(1,2,3,4,k=1,t=2,o=3)


