#!/usr/bin/python -tt 


def foo():
    x=1
    print("in foo",x)
    def bar():
        x=2
        print ("in bar",x)

        def bab():
            x=3
            print("in bab",x)

        bab()
    bar()

foo()
