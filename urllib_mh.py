#!/usr/bin/env python

import urllib3

data=urllib3.urlopen("http://www.baidu.com").read()

print data
