#!/usr/bin/env python 

import sys
import fileinput

# 目标是删除listen monogdb段落中的第一行server开头的行。

listen=input("please input listen name:")

found_listen = False
listen_line="listen "+listen
i=0
for line in fileinput.input("haproxy.cfg",inplace=1):
    line = line.strip("\n")
    if "listen" in line:
        if listen_line in line:
            found_listen = True
        else:
            found_listen = False

    if found_listen:
        if "server" in line:
            i+=1
            if i == 1:   
                continue

    print(line)

