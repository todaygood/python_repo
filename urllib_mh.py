#!/usr/bin/env python

import urllib3

http = urllib3.PoolManager()

r= http.request('GET','http://www.baidu.com')

#print r.data

import json
r = http.request('get','http://httpbin.org/ip')

print "r.data:",r.data
print "r.status:",r.status 
print "headers is:",r.headers

print json.loads(r.data.decode('utf-8'))['origin']





