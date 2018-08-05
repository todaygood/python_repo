#!/usr/bin/python

import commands

err,output = commands.getstatusoutput("ls -alh") 
print (err,output) 

output = commands.getoutput("ls -alh") 
print (output) 

