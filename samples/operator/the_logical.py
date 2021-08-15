#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 逻辑运算符
# @Time    : 2019/4/7 下午2:34
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# and 且（与）
print(True and True)  # True
print(True and False)  # False

# or 或
print(False or True)  # True

# not 非
print(not False)  # True
print(not True)  # False

print(not not True)  # True

print(1 and 1)  # 1
print('a' and 'b')  # 'b'
print(not 'a')  # False

print(not 1)  # False
print([1] or [])  # [1]
print([] or [1])  # [1]

print(1 or 0)  # 1
print(0 or 1)  # 1
