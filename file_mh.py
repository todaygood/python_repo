#!/usr/bin/env python

logfile=open('/tmp/mylog.txt','a')
print >> logfile,'Fatal Error: invalid input'

logfile.close()

