#!/usr/bin/python

def list_make_group(list,filter):
    return [ [ x for i,x in enumerate(list) if filter[i] == True ],  [ x for i,x in enumerate(list) if filter[i] == False ] ]


print(list_make_group(['beep', 'boop', 'foo', 'bar'], [True, True, False, True]))
