#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 装饰器-语法糖
# @Time    : 2019/4/21 下午5:16
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
装饰器五

进一步优化下装饰器

the_decorator4.py 使用 *args 可变参数可以解决函数拥有不同长度参数列表的问题。

支持：**kw 关键字参数
"""

# 类库，框架里面使用了大量装饰器
# 装饰器是一种设计模式
# 特性 类似Java的注解

# 1. 打印函数执行时间
import time


# 1. 可变参数实现
def decorator(func):
    def wrapper(*args, **kw):  # 兼容关键字参数
        print(time.time())
        func(*args, **kw)  # 在不知道如何传参时，抽象，可以使用 *args **kw

    return wrapper


# 魔术-语法糖
# AOP 编程思想
# 带参数
@decorator
def f1(func_name):
    print('This is a function named ' + func_name)


# 和特定函数绑定是没有意义的
@decorator
def f2(func_name1, func_name2):
    print('This is a function named ' + func_name1)
    print('This is a function named ' + func_name2)


# 关键字参数 key word
@decorator
def f3(func_name1, func_name2, **kw):
    print('This is a function named ' + func_name1)
    print('This is a function named ' + func_name2)
    print(kw)


f1('test func')
f2('test func1', 'test func2')
f3('test func1', 'test func2', a=1, b=2, c='123')
