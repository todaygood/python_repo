#!/usr/bin/env python

def fib(max):
    n,a,b=0,0,1
    while n < max:
        #print(b)
        yield b
        a,b=b,a+b
        n=n+1
    return '------done------'

#print(fib(10))

f=fib(100)

print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())


for i in f:
    print( i)

g=fib(6)
while True:
    try:
        x=next(g)
        print("g:",x)
    except StopIteration as e:
        print('Generator return value is',e.value)
        break






