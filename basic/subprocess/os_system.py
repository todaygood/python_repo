#!/usr/bin/python

import os 

cmd = "ls -al > /tmp/mycmd"

os.system(cmd)

print(open('/tmp/mycmd','r').read())
