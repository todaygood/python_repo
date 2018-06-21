#!/usr/bin/python -tt 
import math

a=0xff
print("a=%x, a=%d,a=%o,%s"%(a,a,a,bin(a)))

strHello="the length of (%s) is %d" % ("hello,word",len("hello,world"))
print(strHello)

#precise = 3
print "%.3s " % ("jcodeer")
#precise = 4
print "%.*s" % (4,"jcodeer")
#width = 10,precise = 3
print "%10.3s" % ("jcodeer")

#default
print "PI = %f" % math.pi


for i in range(5):
    print i,

# in python3
for i in range(5):
    print (i,end=' ')


