#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 枚举，Python3引入
# @Time    : 2019/4/20 下午7:29
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

from enum import Enum

"""
* 枚举其实是一个类
* 枚举和普通类相比有什么优势
* 枚举类型、枚举名称与枚举值
* 枚举的比较运算 - Python 枚举可以做 = is 判断，不可以走 > < 比较
* 枚举注意事项
* 枚举小结


现实生活中的类型：

绿钻、黄钻、红钻、黑钻

1 绿钻
2 黄钻
3 红钻

数字不具备描述性，比如看到数字 2不知道表示啥，数字表示类型，破坏了代码可阅读行。

字典 枚举 (Python2 没有，Python3 新增)
"""


# 其它语言，Enum 单独是个类型，Enum 是个关键类。Python 是个类。
class VIP(Enum):
    # 常量
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# 1. 打印出来：VIP.YELLOW
print(VIP.YELLOW)  # 枚举重在它的标签，不在它的数值


# 2. 别名
class Common():
    YELLOW = 1  # 看似大写是个常量，其实是个变量！


# AttributeError: Cannot reassign members.
# VIP.YELLOW = 6

# 3. 获取某个标签对应值
print(VIP.GREEN.name)  # GREEN
print(VIP.GREEN.value)  # 2
# <class 'str'>
print(type(VIP.GREEN.name))
# <enum 'VIP'>
print(type(VIP.GREEN))

# 4. 枚举类型、枚举名称与枚举值
# 获取名称对应的值
print(VIP['GREEN'])

# 5. 枚举遍历
for v in VIP:
    print(v)

# 6. 枚举比较

result = VIP.GREEN == VIP.BLACK
# Flase
print(result)

# 7. 枚举之间不能做大小比较，但可以做等值比较 =
# TypeError: '>' not supported between instances of 'VIP' and 'VIP'
# result = VIP.GREEN > VIP.BLACK
# print(result)

# 8. 枚举身份比较
result = VIP.GREEN is VIP.GREEN
print(result)

# 9. 枚举转换
# 数据库存储枚举，存储枚举数值
# 如何把枚举类型转化为数字
a = 1
print(VIP(a))  # 这里不是真正的类型转化，像 int(str) 这种，理解成使用数值访问枚举的方式
