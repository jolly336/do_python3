#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 闭包
# @Time    : 2019/4/21 下午3:56
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

def a():
    pass

# <class 'function'> 类
print(type(a))


# 1. 什么是闭包
def curve_pre():
    def curve():
        print('This is a function')
        pass

    return curve


# curve()
# 返回 curve() 函数
f = curve_pre()
f()


# 闭包 = 函数 + 环境变量
def curve_pre():
    a = 25
    def curve(x):
        return a * x * x
    return curve
a = 10
f = curve_pre()
print(f(2))
# (<cell at 0x1006602e8: int object at 0x10028bf20>,)
print(f.__closure__)
# 25
print(f.__closure__[0].cell_contents)



