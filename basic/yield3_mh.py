#!/usr/bin/env python

def gen():
    while True:
        s = yield
        print(s)

g=gen()
g.send("kissg")



