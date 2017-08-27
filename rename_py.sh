#!/usr/bin/env bash 

for i in *.py ; do
	b=$(echo $i | awk -F. '{print $1}')
	mv $b.py  ${b}_mh.py 
done
