#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 匹配模式参数
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

a = 'PythonC#\nJavaPHP'

# re.I 或略字母大小写；re.S 匹配所有字符，包括换行
r = re.findall('c#.{1}', a, re.I)
print(r)
# 且，又要或略大小写，又要忽略对.行为的改变
r = re.findall('c#', a, re.I | re.S)
print(r)
