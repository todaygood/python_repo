#!/usr/bin/env python

import urllib2

f= urllib2.urlopen("http://www.python.org/")

print(f.read(100))
