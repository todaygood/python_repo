#!/usr/bin/env python

class DistanceForm(object):
    def __init__(self,origin):
        self.origin= origin
        print("origin:" + str(origin))
    def __call__(self,x):
        print("x:"+str(x))


p = DistanceForm(10)

p(2000)




