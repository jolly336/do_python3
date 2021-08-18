#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 反序列化
# @Time    : 2019/4/14 下午11:55
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import json

# JSON object array
# w3c 规定的，key要使用字符串，双引号
json_str = '[{"name": "qiyue", "age":18, "flag":false},{"name": "qiyue", "age":18}]'

# json_basic -> dict
# loads 把json转换为Python特定数据结构
student = json.loads(json_str)
# <class 'list'>
print(type(student))
print(student)
