#!/usr/bin/python3

import subprocess

res = subprocess.call("ls -al", shell=True) 

print(res)


