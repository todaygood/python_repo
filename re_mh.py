#!/usr/bin/env python

import re

#a= re.match(r'\d{3}\-\d{3,8}$','010-12346')
#
#if a :
#    print("ok")
#else:
#    print("failed")

'''
telephone_no_str=input("Please input your telephone number:")

print(telephone_no_str)
parse_res= re.match(r'(\d{3})\-(\d{3,8})',telephone_no_str)

if parse_res:
    print("all number:",parse_res.group(0))
    print("zone number:",parse_res.group(1))
    print("phone number:",parse_res.group(2))
else:
    print("input invalid")
'''




re_telephone=re.compile(r'(\d{3})\-(\d{3,8})') 

print(re_telephone.match('010-56781234').groups())
print(re_telephone.match('010-5678').groups())





