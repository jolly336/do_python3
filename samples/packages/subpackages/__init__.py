#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2021/8/15 6:45 下午
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

__all__ = ['submodule_1']

# 当十几个模块都要同时导入这三个包时，特别麻烦，所以可以在 __init__.py 里统一导入，在其它模块导入这个包时会自动导入这三个包
import sys
import datetime
import io

a = 'This is __init__.py file'
print(a)