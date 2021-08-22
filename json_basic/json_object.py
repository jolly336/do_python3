#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 反序列化
# @Time    : 2019/4/14 下午11:55
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import json

"""
反序列化

JSON object -> dict 字典

"""

# JSON object array
# w3c 规定的，key 要使用字符串，双引号
json_str = '{"name": "qiyue", "age":18}'

# json_basic -> dict

student = json.loads(json_str)

# <class 'dict'>
print(type(student))  # 查看 student 类型
print(student)

print(student['name'])
print(student['age'])
