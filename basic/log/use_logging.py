#!/usr/bin/python 
import thread
import time 
import logging 
import logging.config 

logging.config.fileConfig('logging.conf') 

# create logger 
logger = logging.getLogger('simpleExample') 
# Define a function for the thread 

def print_time( threadName, delay): 
    logger.debug('thread %s call print_time function body'%(threadName)) 
    count = 0 
    logger.debug('count:%s',count)
    count = count+1
    time.sleep(delay)


for i in range(5):
    thread.start_new_thread(print_time,("thead-"+str(i),1))


time.sleep(20)



