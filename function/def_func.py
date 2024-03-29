#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 自定义函数
# @Time    : 2019/4/14 上午11:14
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
# 函数定义
def funcname(parameter_list):
    pass
'''


# 设置最大递归次数来更改系统最大次数，但即使你设置了，也达不到 1百万次，各个系统不一样，大概在 3000多次？
# import sys
# sys.setrecursionlimit(1000000)

def add(x, y):
    result = x + y
    return result


def print_code(code):
    # print_code(code) # 递归超次数了，995次，[Previous line repeated 995 more times]  RecursionError: maximum recursion depth exceeded
    # print函数没有返回值，结果为 None
    print(code)


# Python 解释性语言，递归栈深为 995 次
a = add(1, 2)
b = print_code('Python')
print(a, b)
