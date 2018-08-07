#!/usr/bin/python3


import subprocess 

cmd = ["ls", "-alh" ] 
res = subprocess.check_output(cmd, stderr=subprocess.STDOUT)

print(res.decode('utf-8'))

