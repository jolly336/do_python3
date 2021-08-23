#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : reduce
# @Time    : 2019/4/21 下午4:58
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
reduce

reduce 在 Python3 已经不再全局命名空间里了，能直接引用 map，是因为 map 在全局命名空间里。reduce 需要从 functools 导入

reduce() 是个函数！

# Google 大数据： map/reduce 编程模型：映射 归约 并行计算
# 借鉴于函数式编程

"""

from functools import reduce

# reduce 是个函数
# 连续计算，连续调用 lambda
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
r = reduce(lambda x, y: x + y, list_x, 10)  # 10 初始值

# (((1 + 2) + 3) + 4) + 5
print(r)  # 46

'''
旅行者问题，变成二维的坐标点，计算移动后最后的坐标位置。涉及到连续计算，reduce 就比较合适
(x, y)
(0, 0)

[(1, 3), (2, -2), (-2, 3)...]
'''

list_x = ['1', '2', '3', '4', '5', '6', '7', '8']
r = reduce(lambda x, y: x + y, list_x, 'aaa')

print(r)  # aaa12345678

# Google 大数据： map/reduce 编程模型：映射 归约 并行计算
# 借鉴于函数式编程
