#!/usr/bin/env python

import sys

find_str=sys.argv[1]
replace_str=sys.argv[2]

with open("setting.ini",'r') as f,\
     open("setting2.ini",'w') as f_new:
	for line in f:
		if find_str in line:
			line=line.replace(find_str,replace_str) 
    	
	f_new.write(line)




