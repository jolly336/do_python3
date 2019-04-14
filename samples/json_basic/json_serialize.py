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

student = [
    {'name': 'qiyue', 'age': 18, 'flag': False},
    {'name': 'qiyue', 'age': 18}
]

json_str = json.dumps(student)
# <class 'str'>
print(type(json_str))
print(json_str)
