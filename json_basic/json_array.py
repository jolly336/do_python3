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

JSON array -> list 列表
"""

# JSON object array
# w3c 规定的，key要使用字符串，双引号
json_str = '[{"name": "qiyue", "age":18, "flag":false},{"name": "qiyue", "age":18}]'

# json_basic -> dict
# loads 把 json 转换为 Python 特定数据结构
student = json.loads(json_str)

# <class 'list'>
print(type(student))
# [{'name': 'qiyue', 'age': 18, 'flag': False}, {'name': 'qiyue', 'age': 18}]
print(student)  # json 字符串中的 false 被转化成了 Python 的 False
