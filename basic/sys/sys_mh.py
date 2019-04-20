#!/usr/bin/env python

import sys
import os

print(sys.platform) # which os 

print(sys.version) # python version


os.execl("/usr/bin/ls","/usr/bin/ls","/")

