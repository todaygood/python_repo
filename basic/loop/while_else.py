#!/usr/bin/env python


oldboy_age=56
count=0

'''
while count<3:
    age=int(input("old boy age=?"))

    if age > oldboy_age :
        print("smaller than", age)
    elif age < oldboy_age:
        print("greater than",age)
    else:
        print("right,it is ",age)

    count+=1
else:
    print("too many times!")
'''

for count in range(3):
    age=int(input("old boy age=?"))

    if age > oldboy_age :
        print("smaller than", age)
    elif age < oldboy_age:
        print("greater than",age)
    else:
        print("right,it is ",age)

else:
    print("too many times!")




    
