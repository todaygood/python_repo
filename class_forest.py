#!/usr/bin/env python

class Forest(object):
    '''Forest demo class'''
    name="first tree"
    def grow(self):
        print("the tree is growing")

    def number(self,num=1):
        if num ==1 :
            print("there is 1 tree")
        else:
            print("there are", num,"trees")

forest=Forest()
forest.grow()
forest.number(12)
print(forest.name)

