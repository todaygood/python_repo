#!/usr/bin/python3

import subprocess 

output = subprocess.run('ls -l' , shell = True , stdout= subprocess.PIPE, universal_newlines=True) 

print (output.stdout) 


