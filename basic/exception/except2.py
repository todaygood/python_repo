#!/usr/bin/env python 

try:
    print ('try..')
    r = 10/int('0')
    print ('result=%d'%r)
except ValueError as e:
    print("ValueError",e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:",e)
else:
    print("no error")
finally:
    print("finally run")

print("end...")




    
