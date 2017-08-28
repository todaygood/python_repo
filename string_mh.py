#!/usr/bin/env python

s='Hello,World'
my_mail='jhu_com@163.com'
'''
print(s.center(50,'-'))
print(my_mail.endswith('@163.com'))
print(my_mail[my_mail.find('com'):])
'''

'''
print(''.join(['1','2','3']))
print('+'.join(['1','2','3']))
print(s.lower())
print(s.upper())
print(s.replace('l','r',2))
print('1+2+3+4'.split('+'))
print(s.swapcase())

print('1123'.zfill(30))

info="my name is {name},age is {age}"
print(info.format(name='Margin Hu',age=10))
print(info)

'''
#print(s.count('o'))
#print(s.capitalize())


#print (str(s))
#print repr(s)

#s="let's go"
#print repr(s)

#print str(1.0/7.0)

#print is a new line
for x in range(1,11):
	print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))


