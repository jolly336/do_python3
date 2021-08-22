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



