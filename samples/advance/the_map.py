#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : map
# @Time    : 2019/4/21 下午4:49
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# map

list_x = [1, 2, 3, 4, 5, 6, 7, 8]

def square(x):
    return x * x


# 1. 之前循环调用实现
for x in list_x:
    square(x)

# 2. map 会对每个元素执行操作
r = map(square, list_x)
# <map object at 0x101a4a6d8>
print(r)
print(list(r))

# 3. map 与 lambda

r = map(lambda x: x * x, list_x)
print(list(r))


# 4. 结果取决于较短集合元素长度
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6]

r = map(lambda x, y: x * x + y * y, list_x, list_y)
print(list(r))
