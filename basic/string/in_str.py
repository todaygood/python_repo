#!/usr/bin/python

str="hello,world"

if "hello" in str:
    print("yes ,in")
else:
    print("no")




str="hello,world"
if str.strip()=="":
    print("str is null")


if not str.strip():
    print("str is null")


str=" "
if str.strip()=="":
    print("str is null")
if str.strip():
    print("str is not null")
