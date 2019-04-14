#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : re.sub正则替换
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

a = 'PythonC#JavaC#PHP'

# 1. 替换，常量字符串替换
r = re.sub('C#', 'GO', a, 1)
print(r)


# 2.
# a = a.replace('C#', 'GO')
# print(a)


# 3. 抽象匹配模式

def convert(value):
    # <_sre.SRE_Match object; span=(6, 8), match='C#'>
    print(value)
    matched = value.group()
    return '!!' + matched + '!!'


r = re.sub('C#', convert, a)
print(r)
