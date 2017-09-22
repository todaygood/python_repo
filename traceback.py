#!/usr/bin/python -tt 

import traceback

def f():
    g()

def g():
   f=open('a.log','w')
   traceback.print_stack(None,None,f)
   print "hello"



f()






