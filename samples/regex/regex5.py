#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 数量词
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

s = 'python 1111java&___678\nphp'

r = re.findall('[a-z]', s)
print(r)

# []{} 数量词
r = re.findall('[a-z]{3}', s)
print(r)

r = re.findall('[a-z]{3,6}', s)
print(r)
