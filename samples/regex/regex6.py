#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 数量词-贪婪与非贪婪
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
贪婪与非贪婪

* 默认：Python 默认是贪婪的，尽可能匹配更多！
* 非贪婪：[字符集]{数量词}? ，在数量词后面加上 ? 表示非贪婪
"""

s = 'python 1111java&___678\nphp'

r = re.findall('[a-z]{3,6}', s)  # ['python', 'java', 'php']
# 贪婪(默认) 与 非贪婪
print(r)

# 非贪婪
r = re.findall('[a-z]{3,6}?', s)  # ['pyt', 'hon', 'jav', 'php']
# r = re.findall('[a-z]{3}', s) # 等同于这种限制 3次
print(r)
