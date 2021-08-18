#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 变量
# @Time    : 2019/4/7 下午1:44
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 1.定义一个变量，= 赋值变量

A = [1, 2, 3, 4, 5, 6]
print(A)

B = [1, 2, 3]
print(A * 3 + B + A)

# 2.变量命令

type = 3  # 不建议使用系统保留关键字！！！
print(type)
# print(type(1))  # 由于上面定义了 type 变量，这里使用 type() 函数就会报错！TypeError: 'int' object is not callable

a = 1
b = a
a = 3
print(b)  # 1

a = [1, 2, 3, 4]
b = a
a[0] = '1'
print(b)  # ['1', 2, 3, 4]

# str 不可变? a + 'python' 生成了一个新的变量
# id() 求变量内存地址
a = 'hello'
print(id(a))
a = a + 'python'
print(id(a))
a = a + 'python'
print(a)
