#!/usr/bin/env python

s='Hello,World'
my_mail='jhu_com@163.com'
'''
print(s.center(50,'-'))
print(my_mail.endswith('@163.com'))
print(my_mail[my_mail.find('com'):])
'''

'''
print(s.lower())
print(s.upper())
print(s.replace('l','r',2))
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


'''
#print is a new line
for x in range(1,11):
	print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))
'''

#practise string concat 

if False:
    name=input("Name:")
    age=input("Age:")


    info1='''
    name={name}
    age={age}
    '''.format(name=name,age=age)

    info2='''
    name={_name}
    age={_age}
    '''.format(_name=name,_age=age)

    print(info1)
    print(info2)


print("Show strip usage")
str3="abc  "
str4="world"
print(str3.strip()+str4)
