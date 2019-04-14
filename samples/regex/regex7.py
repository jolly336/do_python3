#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 数量词-匹配0次1次或者无线多次
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

s = 'pytho0python1pythonn2'

# * 匹配0次或者无线多次
r = re.findall('python*', s)
print(r)

# + 匹配1次或者无限多次
r = re.findall('python+', s)
print(r)

# ? 匹配0次或者1次
r = re.findall('python?', s)
print(r)

r = re.findall('python{1,2}', s)
print(r)

# 非贪婪模式，只会取最小值，一旦找到就不会再去寻找
r = re.findall('python{1,2}?', s)
print(r)
