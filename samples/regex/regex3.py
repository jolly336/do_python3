#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 字符集
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

s = 'abc, acc, adc, aec, afc, ahc'

# 找出中间字符是 c 或 f的单词
# 要抽象的字符集，用中括号，是或的关系
r = re.findall('a[cfd]c', s)
# ['acc', 'adc', 'afc']
print(r)

r = re.findall('a[^cfd]c', s)
# ['abc', 'aec', 'ahc']
print(r)

r = re.findall('a[c-f]c', s)
# ['abc', 'aec', 'ahc']
print(r)
