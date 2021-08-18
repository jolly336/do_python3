#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 成员运算符 in、not in
# @Time    : 2019/4/7 下午2:46
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

a = 1
print(a in [1, 2, 3, 4, 5])

b = 6
print(b not in [1, 2, 3, 4, 5])

b = 'h'
print(b in 'hello')

# 字典成员运算符 key:value 根据 key 来做判断
b = 'a'
print(b in {'c': 1})
b = 1
print(b in {'c': 1})
b = 'c'
print(b in {'c': 1})
