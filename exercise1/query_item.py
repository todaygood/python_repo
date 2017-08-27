#!/usr/bin/env python 

import sys

listen=input("please input listen name:")


with open("haproxy.cfg",'r') as f:
    for line in f:
        if listen in line:
            #print(f.tell())
            for i in range(5):
                print(f.readline())



