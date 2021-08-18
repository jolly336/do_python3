#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 数量词-匹配0次1次或者无线多次
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
匹配0次1次或者无限多次

[字符集]{数量词}

- * 匹配0次或者无限多次
- + 匹配1次或者无限多次
- ? 匹配0次或者1次 

比较：

r = re.findall('python?', s) vs r = re.findall('[a-z]{3,6}?', s) 

第一个 n 是一个固定的字符，不像后面存在一个 3-6 的范围。'python?' 的 ? 是作为数量词出现的，而{3,6}? 作为关键字出现，转换为非贪婪。

"""

s = 'pytho0python1pythonn2'

# * 匹配0次或者无线多次
r = re.findall('python*', s)  # * 号前面的字符(n)可以出现 0次或者无限多次 ['pytho', 'python', 'pythonn']
print(r)

# + 匹配1次或者无限多次
r = re.findall('python+', s)  # + 号前面的字符(n)可以至少要出现一次 ['python', 'pythonn']
print(r)

# ? 匹配0次或者1次
r = re.findall('python?', s)  # 这里的 ? 是作为数量词出现，区别于 regex6.py 的非贪婪，['pytho', 'python', 'python']
print(r)

r = re.findall('python{1,2}', s)  # 默认贪婪，会最大匹配2次n，['python', 'pythonn']
print(r)

# 非贪婪模式，只会取最小值，一旦找到就不会再去寻找
r = re.findall('python{1,2}?', s)  # 加了 ? 号就变成了非贪婪，取最小次数 1 作为 n 出现的次数，['python', 'python']
print(r)
