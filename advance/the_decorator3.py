#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 装饰器-语法糖
# @Time    : 2019/4/21 下午5:16
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
装饰器三

语法糖来解决定义函数和业务函数不关联问题

# 魔术-语法糖
# AOP 编程思想
@xxx

# 原则：定义时候可以复杂，调用要简单，调用随处可见！
"""

# 类库，框架里面使用了大量装饰器
# 装饰器是一种设计模式
# 特性 类似Java的注解

# 1. 打印函数执行时间
import time


def decorator(func):
    def wrapper():
        print(time.time())
        func()

    return wrapper


# 魔术-语法糖
# AOP 编程思想
@decorator
def f1():
    print('This is a function')


# 不改变原来函数调用方式
f1()

# JavaScript 标准 ES6 是个里程碑的标准，提供一种机制允许我们使用 class关键字来定义 JavaScript 类

# 原则：定义时候可以复杂，调用要简单，调用随处可见！
