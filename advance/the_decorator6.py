#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 装饰器-思想
# @Time    : 2019/4/21 下午5:16
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
装饰器六

内容：装饰器的思想 + 日常开发中哪些地方会用到装饰器

"""

# 代码复用性，不会破会代码结构，例如给函数增加打印时间的功能，@decorator
#

# 1. 打印函数执行时间
import time


# 1. 可变参数实现
def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

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
