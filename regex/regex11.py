#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : re.sub正则替换
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
re.sub正则替换

re 是个模块，底下不止有 findAll() 函数，还有其他...

"""

a = 'PythonC#JavaC#PHP'

# 1. 字符串替换，常量字符串替换
# (pattern, repl, string, count=0, flags=0)
# (匹配正则，替换的字符串，原字符串，匹配模式)
# 匹配模式：0 表示无限制匹配下去；1 表示能匹配最大次数
r = re.sub('C#', 'GO', a, 1)
print(r)


# 2. 内置函数，replace 用来字符串替换
# a.replace('C#', 'GO')
# print(a)  # 可以发现 a 字符串没有做替换，这是因为 a 字符串是不可变的，需要重新接收下结果

# a = a.replace('C#', 'GO')
# print(a)


# 内置函数无法实现的，正则可以实现；

# sub 比较强大，第二个参数可以是个函数。。。

# 3. 抽象匹配模式

def convert(value):
    # <_sre.SRE_Match object; span=(6, 8), match='C#'>
    print(value)  # value 是什么？不是字符串，是个对象，
    """
    <re.Match object; span=(6, 8), match='C#'>
    <re.Match object; span=(12, 14), match='C#'>
    """
    matched = value.group()  # 拿到匹配结果
    return '!!' + matched + '!!'


# 流程：当我们正则表达式匹配到一个结果时，会把匹配的结果传到 convert() 函数里，value 就是匹配到的结果，

r = re.sub('C#', convert, a)
print(r)
