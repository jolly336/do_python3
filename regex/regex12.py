#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 把函数作为参数传递
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
把函数作为参数传递

一个复杂的例子来学习

软件设计：一个函数作为一个函数的参数，开放一个接口，传递一个函数

"""

# 问题：找出字符串所有数字，大于等于 6的全部替换为9，小于 6的替换为 0
a = 'A8C3721D86'


# 找出数字判断大于等于6，替换为9，否则为0
def convert(value):
    # <_sre.SRE_Match object; span=(6, 8), match='C#'>
    # print(value)
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'


r = re.sub('\d', convert, a)
print(r)

# 思考：2个数为一组，凡是大于50的替换为100，小于50的替换为0
