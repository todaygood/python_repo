#!/usr/bin/python

import fcntl  
import time  
  
fp = open('hello.txt','w')  

fcntl.flock(fp, fcntl.LOCK_EX)  

print 'file lock begin ...'  


time.sleep(100) 
 
fcntl.flock(fp, fcntl.LOCK_UN)  


fp.close()  



