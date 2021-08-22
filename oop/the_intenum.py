#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : Enum vs IntEnum
# @Time    : 2019/4/21 下午3:38
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

from enum import IntEnum, unique

"""
枚举注意事项

- 枚举数值相同

枚举转换

- 枚举存数据库

"""


@unique  # 装饰器：限制枚举取不同的值
class VIP(IntEnum):  # 继承 Enum 枚举里数值可以是 str，继承 IntEnum 就必须是 int
    # 常量
    YELLOW = 1
    # YELLOW_ALIAS = 1 # 枚举数值可以相同，但是第二个会被当做第一个的别名
    # 1. 只能 int
    # GREEN = "str"
    GREEN = 2
    # 2. 限制每个枚举不能取相同的值
    # GREEN = 1
    BLACK = 3
    RED = 4


for v in VIP:
    print(v)

# 这种可以遍历出枚举中有别名的，('YELLOW', <VIP.YELLOW: 1>) 返回来是元组，第一个是别名，第二个是标签对应的取值
for v in VIP.__members__.items():
    print(v)

for v in VIP.__members__:
    print(v)

# 枚举实现是单例，不能实例化
# 23 种设计模式
