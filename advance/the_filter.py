#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : filter
# @Time    : 2019/4/21 下午5:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""

"""

# filter
# 返回值为True or False
list_x = [1, 0, 1, 0, 0, 1]
r = filter(lambda x: True if x == 1 else False, list_x)
# 0 为False，简化写法
r = filter(lambda x: x, list_x)
print(list(r))

# 去除大写
list_u = ['a', 'B', 'c', 'F', 'e']
