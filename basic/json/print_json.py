#!/usr/bin/env python

import json
import pprint


js = json.dumps(['foo',{'bar': ('baz', None, 1.0, 2)}])

print(js)

pprint.pprint(js)

#convert a python dict to "json" string
str1 = json.JSONEncoder().encode({"foo": ["bar", "baz"]})

print("str1=",str1)
