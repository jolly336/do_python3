#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 装饰器
# @Time    : 2019/4/21 下午5:16
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me


# 类库，框架里面使用了大量装饰器
# 装饰器是一种设计模式
# 特性 类似Java的注解

# 1. 打印函数执行时间
import time


def f1():
    print(time.time())
    print('This is a function')


# unix 时间戳，从格林威治时间1970年01月01日00时00分00秒起至现在的总秒数
# 数据库里面存储
f1()


# 「对修改是封闭的，对扩展是开放的」需要改变时，尽量不应该修改函数，类下面的具体实现
# 通过扩展类、函数来实现需求变更
def f2():
    print(time.time())
    print('This is a function')


# 2. 新增加一个函数
# 缺点：打印时间新增加的需求，是属于每个函数本身，并不属于新增加函数的
def print_current_time(func):
    print(time.time())
    func()


# 和之前实现本质上是一样的
# print(time.time())
# f1()
# print(time.time())
# f2()

print(print_current_time(f1))
print(print_current_time(f2))


