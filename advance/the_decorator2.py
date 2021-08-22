#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 装饰器
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


# 嵌套函数定义
# 装饰
def decorator(func):
    def wrapper():
        print(time.time())
        func()

    # 封装
    return wrapper


def f1():
    print('This is a function')

# 很难用
f = decorator(f1)
f()
