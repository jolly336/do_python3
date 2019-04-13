#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 表达式：（expression）是运算符（operator）和操作数（operand）所构成的序列
# @Time    : 2019/4/7 下午4:44
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

a = 1
b = 2
c = 3

print(a + b * c)  # 7
print(a or b and c)  # 1
print(a or (b and c))  # 1 and 运算符优先级高于 or
print((a or b) and c)  # 3

print(not a or b + 2 == c)
print((not a) or ((b + 2) == c))



