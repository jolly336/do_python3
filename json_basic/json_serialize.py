#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 序列化
# @Time    : 2019/4/15 上午12:07
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# json        python
# object      dict
# array       list
# string      str
# number      int
# number      float
# true        True
# false       False
# null        None

# 序列化
# dict -> json

import json

"""
序列化

Python 数据 -> JSON

思考：如何把一个对象存储到数据库中？

数据库是二维表，没法表示对象的结构，对象序列化成 JSON 或者 HTML 字符串，把字符串存到数据库中。需要的时候读出来发序列化成对象即可。

效率太低了，应该把对象拆成二维表结果，把对象分成一个个属性存到数据库中比较合适。

非要使用，建议使用：NOSQL MongoDB

序列化的意义：

* 豆瓣 API https://developers.douban.com/wiki/?title=api_v2
* 豆瓣数据 Json 数据 https://api.douban.com/v2/book/27124852

比如豆瓣 API JSON 数据，调用服务拿到 JSON 变成 Python 数据结构，从而获得 JSON 中相关数据信息。

"""

# 这里没有使用 \ 来做换行，巧妙的使用 [ ] 括号特性来换行
student = [
    {'name': 'qiyue', 'age': 18, 'flag': False},
    {'name': 'qiyue', 'age': 18}
]

print(type(student))

json_str = json.dumps(student)
# <class 'str'>
print(type(json_str))
print(json_str)
