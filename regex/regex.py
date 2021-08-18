#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 正则表达式
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
初始正则表达式

* 内置函数
* findall()

"""

a = 'C|C++|Java|C#|Python|Javascript'

# 1.简单判断可以用内置函数，判断是否包含 Python
print(a.index('Python') > -1)
print('Python' in a)

# 2.正则表达式初始正则表达式
# findadll 使用的正则是常量字符串，失去了正则的意义，需要写有意义的规则：）
r = re.findall('Python', a)  # '正则表达式' = 'Python'
print(r)  # ['Python'] 返回来是个列表
if len(r) > 0:
    print('字符串中包含 Python')
else:
    print('No')
