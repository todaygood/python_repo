#!/usr/bin/python
# codeing: utf-8 


__author__ = 'Hujun'

def reverse(s):
    print(id(s))
    t= ''
    r=len(s)-1
    while(r>=0):
        t = t+s[r]
        r -= 1

    return t 

s = 'abcd'
print(id(s))
print(reverse(s))


'''
可以看出传入的参数实际上是字符串对象的地址，如果把参数换成list或dict，那么输出的id还是一样的，所以所，Python中传参的方式都是传入对象的地址，只不过数字，字符串和tuple是不可直接修改，而list和dict是可以直接修改。

'''
