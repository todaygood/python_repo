#!/usr/bin/env python

class Forest(object):
    '''Forest demo class'''

    count = 0
    def grow(self):
        self.count += 1
        print("tree count is %d" % self.count)

    def number(self,num=1):
        if num == 1:
            print("there is 1 tree")
        else:
            print("there are", num,"trees")


forest = Forest()

forest.grow()

print("count=%d" % forest.count)

forest.number(12)

print("count=%d" % forest.count)
