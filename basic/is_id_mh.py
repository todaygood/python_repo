#!/usr/bin/env python

x=[2,5, 10]
y=x 
x[1]=8 

print("x is :",x)
print("y is :",y)
print("id(x)=",id(x))
print("id(y)=",id(y))

x=2
y=2

print("x is :",x)
print("y is :",y)
print("id(x)=",id(x))
print("id(y)=",id(y))

x=2000
y=2000
print("x is :",x)
print("y is :",y)
print("id(x)=",id(x))
print("id(y)=",id(y))
print(x is y)


x = [500, 501, 502]
y = x
y[1] = 600
y = [700, 800]
print("x is :",x)
print("y is :",y)
print("id(x)=",id(x))
print("id(y)=",id(y))
print(x is y)


'''
x , y 都是C语言的指针， 跟C语言的赋值机制不一样。 

'''
