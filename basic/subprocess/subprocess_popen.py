#!/usr/bin/python3


import subprocess

p = subprocess.Popen(['ls','-alh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE) 

out,err = p.communicate()

print(out)



