#!/usr/bin/env python

def createGenerator():
    mylist=range(13)
    for i in mylist:
        yield i*i


myArray=createGenerator()
print(myArray)

for i in myArray:
    print(i)

#当你调用生成器函数的时候，如上例中的createGenerator()，程序并不会执行函数体内的代码，它仅仅只是返回生成器对象，这种方式颇为微妙。函数体内的代码只有直到每次循环迭代(for)生成器的时候才会运行。



