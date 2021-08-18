#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 字符集
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
字符集

* 使用 [] 表示字符集 

"""

s = 'abc, acc, adc, aec, afc, ahc'

# 问题：找出单词中间字符是 c 或 f的单词

# 要抽象的字符集，用中括号，是或的关系
r = re.findall('a[cfd]c', s)  # 普通字符 ac 定界，[cfd] 是元字符集
# ['acc', 'adc', 'afc']
print(r)

r = re.findall('a[^cfd]c', s)  # 匹配中间不是 cfd 的单词
# ['abc', 'aec', 'ahc']
print(r)

r = re.findall('a[c-f]c', s)  # 要匹配的字符太多，可以使用顺序 c-f
# ['abc', 'aec', 'ahc']
print(r)
