#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2021/8/15 6:47 下午
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 当导入 subpackages 包时，下面的 __init__.py 模块会被执行，
# __init__.py 模块用 __all__ 限制了导出的模块
from subpackages import *

print(submodule_1.a)
# print(submodule_2.e) # NameError: name 'submodule_2' is not defined
