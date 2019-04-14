#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 概括字符集
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

# \d \D
# \w 单词字符
# \W 非单词字符
# \s 空白字符
# . 匹配除换行符\n之外其他所有字符

s = 'python1111java&___678\nphp'

r = re.findall('\d', s)
print(r)

r = re.findall('[^0-9]', s)
print(r)

# 匹配字母和数字
r = re.findall('\w', s)
r = re.findall('[A-Za-z0-9_]]', s)
print(r)

r = re.findall('\W', s)
print(r)

r = re.findall('\s', s)
print(r)
