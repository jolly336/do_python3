#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : Enum vs IntEnum
# @Time    : 2019/4/21 下午3:38
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

from enum import IntEnum, unique


@unique
class VIP(IntEnum):
    # 常量
    YELLOW = 1
    # 1. 只能int
    # GREEN = "str"
    GREEN = 2
    # 2. 限制每个枚举不能取相同的值
    # GREEN = 1
    BLACK = 3
    RED = 4

# 枚举是单例，不能实例化
