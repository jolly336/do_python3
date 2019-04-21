#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 枚举，Python3引入
# @Time    : 2019/4/20 下午7:29
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

from enum import Enum


class VIP(Enum):
    # 常量
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# 1. VIP.YELLOW
print(VIP.YELLOW)


# 2. 别名
class Common():
    YELLOW = 1


# AttributeError: Cannot reassign members.
# VIP.YELLOW = 6

# 3. 标签对应值
print(VIP.GREEN.name)
print(VIP.GREEN.value)
# <class 'str'>
print(type(VIP.GREEN.name))
# <enum 'VIP'>
print(type(VIP.GREEN))

# 4. 枚举类型、枚举名称与枚举值
# 获取名称对应的值
print(VIP['GREEN'])

# 5. 遍历
for v in VIP:
    print(v)

# 6. 比较

result = VIP.GREEN == VIP.BLACK
# Flase
print(result)

# 7. 不能做大小比较，可以做等值比较
# TypeError: '>' not supported between instances of 'VIP' and 'VIP'
# result = VIP.GREEN > VIP.BLACK
# print(result)

# 8. 身份比较
result = VIP.GREEN is VIP.GREEN
print(result)

# 9. 枚举转换
# 数据库存储枚举，存储枚举数值
a = 1
print(VIP(a))






