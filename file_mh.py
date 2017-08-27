#!/usr/bin/env python
# -*- encoding:utf-8 -*-

#logfile=open('/tmp/mylog.txt','a')
#print >> logfile,'Fatal Error: invalid input'
#
#logfile.close()

#data= open("/tmp/yesterday",'r').read()
#print data


f= open("/tmp/yesterday",'r')
#f.truncate(10)

f_new= open("/tmp/yesterday.bak",'w')
#print f.readline()
#print f.readline()

for line in f:
	if "When they played" in line:
		line=line.replace("When they played","When they played you")
	f_new.write(line)





#f.write('hello--diao--------\n')
#f.write('hello---diao--------\n')
#f.write('-------diao--------\n')
#f.write('-------diao--------\n')
#print f.tell()




#for i in range(5):
#	print f.readline()

#for line in f.readlines():
#	print line.strip()

#count=0
#for line in f:
#	count+=1
#	if count==9 :
#		print("------------")
#		continue
#	print line

#low loop
'''
for index,line in enumerate(f.readlines()):
	if index == 9:
		print('----------9--------------')
		continue
	print line.strip()
'''

#data= f.read()
#data2 = f.read()

#f.write("我爱北京天安门")

#print data
#print data2


f.close()

f_new.close()



