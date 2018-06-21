#!/usr/bin/env python

def yield_test(n): 
    for i in range(n):
        print("in i=",i)  
        yield call(i)  
        print("out i=",i)  
    #做一些其它的事情      
    print("do something.")      
    print("end.")  

def call(i):  
    return i*2  

#a = yield_test(5)
#print(a)

#使用for循环  
for i in yield_test(5):  
    print(i,",")





