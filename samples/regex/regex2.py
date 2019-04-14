#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 元字符与普通字符
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

a = 'C0|C++7|Java8|C#9|Python6Javascript'

# 数字
# ['0', '7', '8', '9', '6']
r = re.findall('\d', a)
print(r)

# 'Python' 普通字符，'\d' 元字符
# \D 非数字
r = re.findall('\D', a)
print(r)
