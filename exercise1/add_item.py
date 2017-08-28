#!/usr/bin/env python 

import sys
import fileinput


listen=input("please input listen name:")

#item=input("please input content (a dict):")
item='''
{
    'listen':'mongodb',
    'content':
    {
        'server': 'cloud-sz-control-b13-04 10.54.12.13:27017',
        'inter': 3000,
        'rise': 4,
        'fall': 5
    }
}
'''

item_dict=eval(item)
content_dict=item_dict['content']

last_item_str='  server '   + content_dict['server']
last_item_str+=' inter '  + str(content_dict['inter'])
last_item_str+=' rise '   + str(content_dict['rise'])
last_item_str+=' fall '   + str(content_dict['fall'])


print(last_item_str)

'''
with open("haproxy.cfg",'r+') as f:
    while 1:
        line = f.readline()
        if not line:
            break

        if listen in line:
            for i in range(5):
                print(f.readline())
             
            f.write(last_item_str) #always it is in the last line of the file
            break


# python file no line num
'''

for line in fileinput.input("haproxy.cfg",inplace=1):
    line = line.strip("\n")
    print(line)
    if listen in line:
        print(last_item_str)

