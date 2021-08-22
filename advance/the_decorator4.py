#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 装饰器-语法糖
# @Time    : 2019/4/21 下午5:16
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""

"""

# 类库，框架里面使用了大量装饰器
# 装饰器是一种设计模式
# 特性 类似Java的注解

# 1. 打印函数执行时间
import time


# 1
# def decorator(func):
#     def wrapper(func_name):
#         print(time.time())
#         func(func_name)
#
#     return wrapper
#
#
# # 魔术-语法糖
# # AOP 编程思想
# # 带参数
# @decorator
# def f1(func_name):
#     print('This is a function named ' + func_name)
#
# # 和特定函数绑定是没有意义的
# @decorator
# def f2(func_name1, func_name2):
#     pass
#
#
# f1('test func')


# 2. 可变参数实现
def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)

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


f1('test func')
f2('test func1', 'test func2')
