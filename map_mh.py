#!/usr/bin/env python

#def cube(x):
#	return x*x*x
#
#print map(cube,range(1,5))


#seq = range(8)
#print(seq)
#
#def add(x,y):
#	return x+y
#
#a=(map(add,seq,seq))
#for i in a:
#    print(i)



my=map(lambda x: x*x, range(10))
for i in my:
    print(i)

'''
1.map函数
map函数会根据提供的函数对指定序列做映射。
map函数的定义：
map(function, sequence[, sequence, ...]) -> list
通过定义可以看到，这个函数的第一个参数是一个函数，剩下的参数是一个或多个序列，返回值是一个集合。
function可以理解为是一个一对一或多对一函数，map的作用是以参数序列中的每一个元素调用function函数，返回包含每次function函数返回值的list。
比如要对一个序列中的每个元素进行平方运算：
map(lambda x: x ** 2, [1, 2, 3, 4, 5])
返回结果为：
[1, 4, 9, 16, 25]
在参数存在多个序列时，会依次以每个序列中相同位置的元素做参数调用function函数。
比如要对两个序列中的元素依次求和。
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
map返回的list中第一个元素为，参数序列1的第一个元素加参数序列2中的第一个元素(1 + 2)，
list中的第二个元素为，参数序列1中的第二个元素加参数序列2中的第二个元素(3 + 4)，
依次类推，最后的返回结果为：
[3, 7, 11, 15, 19]
要注意function函数的参数数量，要和map中提供的集合数量相匹配。
如果集合长度不相等，会以最小长度对所有集合进行截取

'''



