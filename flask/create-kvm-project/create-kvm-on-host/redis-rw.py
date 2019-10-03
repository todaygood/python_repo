#!/usr/bin/python3
#coding=utf-8
 
import redis
 
r = redis.Redis(host="127.0.0.1", port=6379, db=0)
# 新建一条键名为"123456"的数据, 包含属性attr_1
r.hset("123456", "attr_1", 100)
# 更改键名为"123456"的数据, 更改属性attr_1的值
r.hset("123456", "attr_1", 200)
 
# 取出属性attr_1的值
attr_1 = r.hget("123456", "attr_1")
 
# 输出看一下(发现属性值已经为str)
print ("-- get attr_1:", attr_1)
 
# 属性集合
attr_dict = {
    "name": "常成功",
    "alias": "常城",
    "sex": "male",
    "height": 175,
    "postal code": 100086,
    "Tel": 18680356499,
}
# 批量添加属性
r.hmset("123456", attr_dict)
 
# 取出所有数据(返回值为字典)
h_data = r.hgetall("123456")
 
# 输出看一下(取出来的时候都变成了str)
print( "-- get all attr:", h_data)
 
# 删除属性(可以批量删除)
r.hdel("123456", "Tel")
 
# 取出所有属性名
h_keys = r.hkeys("123456")
 
print( "-- get attr name:", h_keys)
 
