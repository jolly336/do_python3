#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 正则表达式
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

a = 'C|C++|Java|C#|Python|Javascript'

# 1.简单判断可以用内置函数
print(a.index('Python') > -1)
print('Python' in a)

# 2.正则表达式

r = re.findall('Python', a)
# print(r)
if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')
