#!/usr/bin/env python

name = "Alex Li"
school = "oldboy"

list=['Alex','baby','boy']

def change_name(name):
    #global school
    print("before change:",name)
    name = "金角大王,一个有Tesla的男人"
    print("after change", name)
    print(school)
    #school="python.org"
    list[1]='baby2'
 
 
change_name(name)
 
print("在外面看看name改了么?",name)
print(list)
