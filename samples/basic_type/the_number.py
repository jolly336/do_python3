#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 数字Number
# @Time    : 2019/2/26 下午10:27
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

print(True)  # True
print(False)  # False

print(type(True))  # <class 'bool'>

print(int(True))  # 1
print(int(False))  # 0

# python 中 bool 类型属于数字 Number 下的一种
print(bool(1))  # True
print(bool(0))  # False

print(bool(2))  # True
print(bool(2.2))  # True
print(bool(-1.1))  # True
print(bool(0b01))  # True
print(bool(0b0))  # False

# 其它类型可以和bool来转换
print(bool('abc'))  # True
print(bool(''))  # False

# 列表
print(bool([1, 2, 3]))  # True
print(bool([]))  # False

# 在 Python 中一系列空值会被认为是 false
print(bool({1, 1, 1}))  # True
print(bool({}))  # False

print(bool(None))  # False
