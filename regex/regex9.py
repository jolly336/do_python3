#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 组
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
组

(组){次数}(另外一个组)

思考：对比之前 [] 和 () 在逻辑上有啥不一样的？

[abc] 是或的关系
(abc) 是且的关系

"""

# 问题：判断 a 字符串是否包含 3个 Python？
a = 'PythonPythonPythonPythonPython'

# [abc] 中间字符是或的关系，() 是且的关系
# r = re.findall('PythonPythonPython', a) # 最直接的想法是写三个 Python，emmm 也可以。要判断 100次呢？写一百次？？？
# r = re.findall('Python{3}', a) # 这样写只是 n 显示 3次！！
r = re.findall('(Python){3}(JS)', a)  # 组，使用 () 就可以
print(r)
