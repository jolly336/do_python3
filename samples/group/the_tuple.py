#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 元组 ( )
# @Time    : 2019/2/26 下午11:25
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

print((1, 2, 3, 4, 5))
print((1, '-1', True))
print((1, 2, 3, 4)[0])
print((1, 2, 3, 4)[0:2])
print((1, 2, 3) + (4, 5, 6))
print((1, 2, 3) * 3)

# tuple vs list???

# int str list
print(type((1, 2, 4)))  # <class 'tuple'>
print(type([1, 2, 4]))  # <class 'list'>
print(type('hello'))  # <class 'str'>

# 注意：tuple只有一个元素时，需要添加「,」，只有一个元素时，会进行算术运算
print(type((1)))  # <class 'int'>
print(type(('hello')))  # <class 'str'>
print(type((1,)))  # <class 'tuple'>

# 空元祖
print(type(()))  # <class 'tuple'>
print(type([1]))  # <class 'list'>

print(3 in [1, 2, 3, 4, 5, 6])  # True
print(3 not in [1, 2, 3, 4, 5, 6])  # False

# len
print(len("hello world"))

# max
print(max([1, 2, 3, 4, 5, 6]))
# 设计字符编码 ASCII
print(max('hello world')) # w
# ord 查看ASCII码
print(ord('w'))
print(ord(' '))

# min
print(min([1, 2, 3, 4, 5, 6]))
print(min('hello world')) # ' '



