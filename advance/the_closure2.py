#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 闭包的误区
# @Time    : 2019/4/21 下午3:56
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 闭包 = 函数 + 环境变量(函数定义时候)
# 现场

# 1
def f1():
    a = 10

    def f2():
        # a 此时被Python认为局部变量
        a = 20
        print(a)

    print(a)
    f2()
    print(a)


# 10 20 10
f1()


# 2
def f1():
    a = 10

    def f2():
        a = 20
        print(a)

    return f2


f = f1()
# <function f1.<locals>.f2 at 0x102a4d6a8>
print(f)
# None
print(f.__closure__)


# 3
def f1():
    a = 10

    def f2():
        # a 被Python认为是一个局部变量
        # a = 20
        print(a)

    return f2


f = f1()
# <function f1.<locals>.f2 at 0x102a4d6a8>
print(f)
# (<cell at 0x1005602e8: int object at 0x10028bd40>,)
print(f.__closure__)
