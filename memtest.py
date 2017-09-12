#!/usr/bin/python
#-*-coding: utf8-*-

from datetime import datetime
import gc

d = {}
ck = 0

class O:
    def __init__(self, id):
        self.id = id
        self.v  = 1#range(10)

def log(func):
    def new_f(*args, **kwargs):
        header = "*[ OUTPUT][%s]:" 
        print header % datetime.now(), func(*args, **kwargs), memory()
    return new_f

@log
def err(*msg):
    return '[*ERROR*][%s]:' % msg

def memory():
    import os
    _cmd = 'ps u -p %s' % os.getpid()
    exec_result = os.popen(_cmd).readlines()
    mem_used = exec_result[1].split()[3]
    return 'Memory used: ' +  mem_used + '%', 'Objects:', len(gc.get_objects())

@log
def add(cnt, obj):
    global ck
    i = 0
    cnt = int(cnt)

    if d:
        max_key = max(d.keys())
    else:
        max_key = ck

    while i < cnt:
        i += 1
        c_key = max_key + i
        if obj:
            d[c_key] = O(c_key)
        else:
            d[c_key] = 'dictionary %s' % c_key

    ck = c_key

    return 'Dictionary length:', len(d)

@log
def clear():
    global d
    for k in d.keys():
        if isinstance(d[k], O):
            del d[k].v
        del d[k]

    gc.collect()
    del d
    d = {}

    return 'Dictionary length:', len(d)

@log
def display():
    return d

@log
def size():
    return 'Dictionary length:', len(d), 'Size:', d.__sizeof__()

def main():
    import sys

    while 1:
        try:
            line = raw_input('%[ INPUT ] >>> ')
        except (KeyboardInterrupt, IOError, EOFError):
            break
        if line.startswith('q'):
            break

        line = line.split()
        if line[0].startswith('a'):
            obj = 0
            cnt = 1
            l   = len(line)

            if l > 1:
                cnt = int(line[1])
                if l > 2:
                    obj = int(line[2])
            add(cnt, obj)
        elif line[0].startswith('c'):
            clear()
        elif line[0].startswith('d'):
            display()
        elif line[0].startswith('m'):
            memory()
        elif line[0].startswith('s'):
            size()
        else:
            err('Unknown command. re-try please:')


if __name__ == "__main__":
    main()
