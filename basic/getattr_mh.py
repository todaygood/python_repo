#!/usr/bin/env python

class Xiaorui:
    def __init__(self):
        self.name = 'fengxue'

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello,I'm %s" % self.name)



foo=Xiaorui()

print(hasattr(foo,'setName'))

print(getattr(foo,'name','NA')) 

setattr(foo,'name','Margin')

print(getattr(foo,'name','NA')) 

delattr(foo,'name')

print(getattr(foo,'name','not found')) 
