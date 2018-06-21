#!/usr/bin/env python 

import urllib2

request = urllib2.Request('http://www.centos1.org')

# see what output when not use try..except.
urllib2.urlopen(request)

print("continue or break")

try:
    urllib2.urlopen(request)
except urllib2.URLError,e:
    print e.reason

    
