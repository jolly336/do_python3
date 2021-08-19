#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 匹配模式参数
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
匹配模式参数

"""

a = 'PythonC#\nJavaPHP'

r = re.findall('c#', a)
print(r)  # [] 啥也没匹配到，你是小写的 c#

# def findall(pattern, string, flags=0) 最后一个参数加模式
r = re.findall('c#', a, re.I)  # 忽略大小写
print(r)  # ['C#']

# re.I 或略字母大小写；re.S 匹配所有字符，包括换行
r = re.findall('c#.{1}', a, re.I)  # 要匹配 c# 再加一个任意字符
print(r)  # []

# 概括字符集 . 表示除 \n 换行符以外的所有字符，加上 re.S 模式之后，就可以匹配所有字符了
r = re.findall('c#.{1}', a, re.I | re.S)  # 说明：这里 | 不是我们理解的或关系，而是且关系。
# 且，又要或略大小写，又要忽略对.行为的改变
print(r)  # ['C#\n']
