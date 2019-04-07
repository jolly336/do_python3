#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 比较（关系）运算符
# @Time    : 2019/4/7 下午2:22
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

print(1 == 1)
print(1 > 1)

a = 1
b = 2
print(a != b)

# bool布尔类型：不只是数字才能做比较运算符
b = 1
b += b >= 1
print(int(True))  # 1
print(b)  # 2

# 字符串：比较字母的ASCII 码
print(ord('a'))
print(ord('b'))
print('a' > 'b')

# 列表

print([1, 2, 3] < [2, 3, 4])

# 元组

print((1, 2, 3) < (1, 3, 2))
