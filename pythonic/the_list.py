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

# 1. 求 a的平方？
# for循环、高阶函数（map）、列表推导式
a = [1, 2, 3, 4, 5, 6, 7, 8]

# 列表推导式
b = [i * i for i in a]
b = [i ** 3 for i in a]
print(b)

# 推荐使用情况
# 选择性处理筛选处理
# map filter 也可以实现
b = [i ** 3 for i in a if i >= 5]
print(b)

# set 也可以被推导

a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {i ** 2 for i in a if i >= 5}
print(b)

# dict
