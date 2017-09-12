#!/usr/bin/env python

import test
import multiprocessing

def run(func,*args):
    print(getattr(test,func)(*args))


pool=multiprocessing.Pool(processes=4)
for i in range(10):
    pool.apply_async(run,('hello','hello','world'))
    pool.apply_async(run,('test_sleep','hello','world'))

pool.close()
pool.join()

print("End...")

