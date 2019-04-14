#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 边界匹配
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

# qq = '100001'
# qq = '101'
qq = '100000001'

# 4~8位之间
r = re.findall('\d{4,8}', qq)
print(r)

# 边界匹配，匹配完整字符串
r = re.findall('^\d{4,8}$', qq)
print(r)

r = re.findall('000', qq)
print(r)

r = re.findall('^000', qq)
print(r)

r = re.findall('000$', qq)
print(r)

