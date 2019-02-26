#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 数字Number
# @Time    : 2019/2/26 下午10:27
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

print(True)

print(False)

print(type(True))

print(int(True))
print(int(False))

# python中bool类型属于数字Number下的一种
print(bool(1))
print(bool(0))


print(bool(2))
print(bool(2.2))
print(bool(-1.1))
print(bool(0b01))
print(bool(0b0))

# 其它类型可以和bool来转换

print(bool('abc'))
print(bool(''))

# 列表
print(bool([1, 2, 3]))
print(bool([]))

# 在Python中一系列空值会被认为是false
print(bool({1, 1, 1}))
print(bool({}))

print(bool(None))

