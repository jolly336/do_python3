#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 列表和元组区别
# @Time    : 2019/4/7 下午2:06
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

a = [1, 2, 3]
print(id(a))
print(hex(id(a)))

a[0] = '1'

# a = (1, 2, 3)
# a[0] = '1'

b = [1, 2, 3]
b.append(4)
print(b)

c = (1, 2, 3)
# c.append(4)

a = (1, 2, 3, [1, 2, 4])
print(a[2])  # 3
print(a[3][2])  # 4'
a[3][2] = '4'
print(a)  # (1, 2, 3, [1, 2, '4']) 元组不能改变？？

a = (1, 2, 3, [1, 2, ['a', 'b', 'c']])
print(a[3][2][1])



