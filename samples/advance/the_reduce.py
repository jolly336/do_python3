#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : reduce
# @Time    : 2019/4/21 下午4:58
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

from functools import reduce

# reduce是个函数
# 连续计算，连续调用lambda
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
r = reduce(lambda x, y: x + y, list_x, 10)

# (((1 + 2) + 3) + 4) + 5
print(r)



list_x = ['1', '2', '3','4', '5', '6', '7', '8']
r = reduce(lambda x, y: x + y, list_x, 'aaa')

print(r)

# Google 大数据： map/reduce 编程模型：映射 归约 并行计算
# 借鉴于函数式编程