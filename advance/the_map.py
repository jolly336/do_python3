#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : map
# @Time    : 2019/4/21 下午4:49
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
* map-映射
> 推荐：多多使用！

map 不是一个函数，是一个类！

* map与lambda

map 结合 lambda 使用
"""

# map

# 问题：把列表中数字变成自己的平方
list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def square(x):
    return x * x


# 1. 之前循环调用实现
for x in list_x:
    square(x)

# 2. map 会对每个元素执行操作
r = map(square, list_x)
print(r)  # <map object at 0x101a4a6d8>
print(list(r))  # [1, 4, 9, 16, 25, 36, 49, 64]

# 3. map 与 lambda
# 输入参数只有 1个
r = map(lambda x: x * x, list_x)  # lambda 表达式 替换 square 函数
print(list(r))

# 4. 结果取决于较短集合元素长度
# 输入参数有多个
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6]

r = map(lambda x, y: x * x + y * y, list_x, list_y)
print(list(r))  # [2, 8, 18, 32, 50, 72]
# x 和 y 列表格式不一样，最后结果取决于最小个数列表！
