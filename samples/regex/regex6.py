#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 数量词-贪婪与非贪婪
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

s = 'python 1111java&___678\nphp'

r = re.findall('[a-z]{3,6}', s)
# 贪婪(默认) 与 非贪婪
print(r)

# 非贪婪
r = re.findall('[a-z]{3,6}?', s)
print(r)
