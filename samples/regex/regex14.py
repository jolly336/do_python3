#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : group分组
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

# search与match一般用得少，findall好用一点

s = 'life is short,i use python, i love python'

# 截取life和python之间的字符串
r = re.search('life.*python', s)
print(r.group())

r = re.search('(life.*python)', s)
# group(0)永远返回完整匹配结果
print(r.group(0))

r = re.search('life(.*)python', s)
print(r.group(1))

# findall比较方便，建议使用findall！！！
r = re.findall('life(.*)python', s)
print(r)

r = re.search('life(.*)python(.*)python', s)
print(r.group(0))
print(r.group(1))
print(r.group(2))

# 以元组返回所有数据
# ('life is short,i use python, i love python', ' is short,i use ', ', i love ')
print(r.group(0, 1, 2))
# (' is short,i use ', ', i love ')
print(r.groups())
