#!/usr/bin/python -tt 

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int (s.strip())
except IOError as e:
    print "IO error ({0}):{1}".format(e.errno,e.strerror)
except ValueError:
    print "Could not convert data to Integer"
except:
    print "Unexcepted Error",sys.exc_info()[0]
    raise



