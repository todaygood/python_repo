#!/usr/bin/env python

import json

#print json.dumps(['foo',{'bar':('baz', None ,1.0,2)} ] )
#print json.dumps("\"foo\bar")

#print json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')


#student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},
#           "102":{"class":'V', "Name":'David',  "Roll_no":8},
#           "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}
#		   
#print(json.dumps(student, sort_keys=True))


tup1 = 'Red', 'Black', 'White';
print(json.dumps(tup1));

