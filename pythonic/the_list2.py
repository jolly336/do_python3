#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 列表推导式（集合推导式）
# @Time    : 2019/4/21 下午7:38
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
 列表推导式
'''

# dict

students = {
    'Nelson': 20,
    'Jolly': 20,
    'Mandy': 1
}

# list
b = [key for key, value in students.items()]
print(b)

# dict
b = {value: key for key, value in students.items()}
print(b)

# tuple，不推荐使用元组
# key, value 是字典的，() 元组只能有一个值
b = (key for key, value in students.items())
# 为啥元组是 generator？因为元组是不可变的，其它是可变序列
print(b)  # <generator object <genexpr> at 0x106c1cf50>
for x in b:
    print(x)
