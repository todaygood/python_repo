#!/usr/bin/env python
import time


def timer(func):
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("run time is %s" %(stop_time-start_time))
        
    return deco


#bar=timer(bar)

@timer   # bar=timer(bar)
def bar():
    time.sleep(3)
    print("in bar")

@timer
def foo(name):
    time.sleep(3)
    print("in foo",name)

bar()
foo('alex')


