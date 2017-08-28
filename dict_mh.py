#!/usr/bin/env python

student={'n001':'Hu Jun','n002':'Tian Jing','n003':'yuan aisha'}

#print(student)
#
#del(student['n002'])
#
#print(student)
#
#student['n004']='tian bin'
#
#print(student)
#
#student.pop('n004')
#
#print(student)
#
#print(student.get('n003'))
#print(student.get('n006'))
#
#
#print(student.values)
#
#playb={'p001':'we','p002':'you','n001':'Margin Hu'}
#student.update(playb)
#print(student)
#
#
#

for i in student:
    print(i,student[i])

# item(),convert dict to list
print(student.items())

for k,v in student.items():
    print(k,v)
