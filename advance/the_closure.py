#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 闭包
# @Time    : 2019/4/21 下午3:56
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
函数式编程

* 闭包
函数，其他语言是一段可执行代码，并不是对象，函数是不能实例化的。
而 Python 函数是可以实例化的，一切皆对象。结构

a = 1
a = '2'
a = def # 可以把函数赋值给变量

- 另外一个函数的参数，传递到另外的函数里。
- 把一个函数当做另外一个函数的返回结果，返回给调用方。

* 什么是闭包？

闭包 = 函数 + 环境变量（定义的环境变量）

"""


def a():
    pass


# <class 'function'> 类
print(type(a))  # 打印函数 a 的类型，发现是 class 类，一切皆对象呐。。。


# 1. 什么是闭包
def curve_pre():
    def curve():  # 函数内部再定义一个函数，
        print('This is a function')
        pass

    return curve  # 函数作为一个返回结果返回


# curve() # 直接调用内部函数，不可以！
# 返回 curve() 函数
f = curve_pre()
f()  # 调用内部函数


# 闭包 = 函数 + 环境变量（定义的环境变量）
def curve_pre():
    a = 25

    def curve(x):
        return a * x * x

    return curve


a = 10
f = curve_pre()
print(f(2))  # 100
# (<cell at 0x1006602e8: int object at 0x10028bf20>,)
print(f.__closure__)  # 闭包
# 25
print(f.__closure__[0].cell_contents)  # 定义时的环境变量
