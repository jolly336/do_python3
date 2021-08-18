#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 组
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

a = 'PythonPythonPythonPythonPython'

# [abc] 中间字符是或的关系，() 是且的关系
r = re.findall('(Python){3}(JS)', a)
print(r)


