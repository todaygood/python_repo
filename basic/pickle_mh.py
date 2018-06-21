#!/usr/bin/env python

import pickle

data=[{'a':'A','b':2,'c':3.0}]

data_string = pickle.dumps(data)

#print "DATA:"
#print data
#print "PICKLE:"
#print data_string

data_from_string=pickle.loads(data_string)

#print  data_from_string


#data_string_1 = pickle.dumps(data,1)
#data_string_2 = pickle.dumps(data,2)
#
#print data
#print 
#print data_string_1
#print 
#print data_string_2

with open("data.pkl","wb") as f:
	pickle.dump(data,f)

with open("data.pkl","r") as f:
	print pickle.load(f)



import os
os.remove("data.pkl")


