#!/usr/bin/env python

import urllib2

print("use urlopen")

f= urllib2.urlopen("http://www.python.org/")
print(f.read(100))


print("use Request")

req= urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(req)
the_page = response.read()
print (the_page)

