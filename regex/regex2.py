#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 元字符与普通字符
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
元字符与普通字符

* 正则表达式
"""

a = 'C0|C++7|Java8|C#9|Python6Javascript'

# 问题：把 a 字符串里的所有数字提取出来？
# 用 for 循环遍历找出来？for in ... 太费事了吧

# 数字
# ['0', '7', '8', '9', '6']
r = re.findall('\d', a)  # \d 0-9
print(r)

# 'Python' : 普通字符，
# '\d': 元字符，正则就是学习各种元字符
# 可以混合使用，普通字符 + 元字符

# 问题：把 a 字符串里的所有非数字提取出来？
# \D 非数字
r = re.findall('\D', a)
print(r)
