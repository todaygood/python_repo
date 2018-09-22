#!/usr/bin/python

print(isinstance("foo",basestring))


print(isinstance(123,float))


class Foo: pass

class Bar(Foo): pass

b = Bar()

print (isinstance(b, Bar))
print (isinstance(b, Foo))
print (isinstance(Bar, Foo))
