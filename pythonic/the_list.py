#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 列表推导式（集合推导式）
# @Time    : 2019/4/21 下午7:38
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
 列表推导式-根据一个已存在的列表创建一个新的列表

 集合推导式

 使用 for 循环
 * list
 * set
 * dict
'''

# 1. 求 a 的平方？
# 没有列表推导式的，有两种处理方式：1）for 循环；2）高阶函数（map）
# OR
# 列表推导式
# for 循环、高阶函数（map）、列表推导式
a = [1, 2, 3, 4, 5, 6, 7, 8]

# 列表推导式也可以完成 map 所能完成的功能，Python 特色。其它语言也有 map，使用 map 函数思维多点。也看个人使用习惯。
# r = map(lambda x: x * x, list_x)  # lambda 表达式 替换 square 函数
# print(list(r))

b = [i * i for i in a]
b = [i ** 3 for i in a]
print(b)

# 推荐使用情况
# 选择性处理筛选处理（注意：这种情况推荐使用列表推导式！if 筛选）
# map filter 也可以实现
b = [i ** 3 for i in a if i >= 5]
print(b)

# set 也可以被推导

a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {i ** 2 for i in a if i >= 5}
print(b)

# dict
