#!/usr/bin/env python
import time

def log(func):
    def wapper(*args,**kw):
        print("call %s():"%func.__name__)
        return func(*args,**kw)
    return wapper
        
    
@log
def test1():
    time.sleep(3)
    print("in test1")
    return 3333



print(test1())



