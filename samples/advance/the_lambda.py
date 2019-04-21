#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 匿名函数 Lambda
# @Time    : 2019/4/21 下午4:39
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 表达式，不是代码块，代码块很大
# lambda parameter_list:expression

def add(x, y):
    return x + y

print(add(1, 2))
f = lambda x, y: x + y
print(f(1, 2))

# 三元表达式 x > y ? x : y
# 条件为真时返回的结果 if 条件判断 else 条件为假时的返回结果

x = 2
y = 3

r = x if x > y else y
print(r)
